"""Couverture du provider OpenRouter (routeur vers ~430 modèles tiers).

Aucun appel réseau : le préflight (`urllib.request.urlopen`) et le client
OpenAI sont mockés. Les tests verrouillent ce qui a été MESURÉ sur l'API réelle
le 2026-09-05, et qu'aucune lecture de documentation n'aurait donné :

- un même slug est servi par des dizaines d'hébergeurs aux plafonds de sortie
  différents — 23 pour `z-ai/glm-5.3-flash`, dont un à 2 048 tokens ;
- `provider.only` sans `allow_fallbacks: false` n'est qu'une préférence ;
- couper le raisonnement quand le modèle l'autorise fait passer la même réponse
  de 107 à 2 tokens de complétion ;
- un modèle qui l'impose répond 400 « Reasoning is mandatory for this endpoint
  and cannot be disabled » ;
- `finish_reason=length` avec un texte vide n'est pas une troncature mais un
  budget mangé par le raisonnement : les deux cas appellent des gestes opposés.

Lancement : python -m unittest discover tests/ -v
"""

from __future__ import annotations

import argparse
import io
import json
import os
import sys
import unittest
from argparse import Namespace
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from aipmt import translate

_MARQUEUR = "jeton-de-test"


def _args(**kw):
    base = {
        "model": "z-ai/glm-5.2",
        "eco": False,
        "reasoning_effort": None,
        "use_openrouter": True,
        "target_lang": "en",
    }
    base.update(kw)
    return Namespace(**base)


def _choice(content="Bonjour", finish="stop", native=None):
    return SimpleNamespace(
        message=SimpleNamespace(content=content),
        finish_reason=finish,
        native_finish_reason=native,
    )


def _client(providers=("deepinfra/fp4",), max_tokens=32768, mandatory=False, efforts=()):
    return translate._OpenRouterClient(
        client=MagicMock(),
        providers=providers,
        max_tokens=max_tokens,
        reasoning_mandatory=mandatory,
        supported_efforts=efforts,
    )


def _endpoint(tag, max_out, status=0):
    return {"tag": tag, "max_completion_tokens": max_out, "status": status}


class TestModelValidation(unittest.TestCase):
    """`--model` est obligatoire et sa forme est vérifiée AVANT tout réseau :
    le slug est interpolé dans l'URL de préflight."""

    def test_model_absent_refuse(self):
        with self.assertRaises(ValueError) as ctx:
            translate._openrouter_validate_model(None)
        self.assertIn("fournisseur/modèle", str(ctx.exception))
        self.assertIn("openrouter.ai/models", str(ctx.exception))

    def test_model_sans_namespace_refuse(self):
        with self.assertRaises(ValueError):
            translate._openrouter_validate_model("glm-5.2")

    def test_segment_parent_refuse(self):
        """La regex commune aux providers namespacés accepte `a/b/..` ; ce slug
        détournerait l'URL de préflight, d'où le refus explicite."""
        with self.assertRaises(ValueError):
            translate._openrouter_validate_model("z-ai/glm/..")

    def test_slugs_reels_acceptes(self):
        for slug in ("z-ai/glm-5.2", "qwen/qwen3.8-flash", "moonshotai/kimi-k2.6"):
            translate._openrouter_validate_model(slug)


class TestPin(unittest.TestCase):
    """Épinglage des hébergeurs : le cœur du provider."""

    def test_ecarte_les_plafonds_trop_bas(self):
        """Mesuré : `sail-research/fp8` sert glm-5.3-flash avec 2 048 tokens de
        sortie. Sans ce filtre, une traduction sur 23 partait tronquée."""
        tags, ceiling = translate._openrouter_pin(
            [_endpoint("sail-research/fp8", 2048), _endpoint("deepinfra/fp4", 131072)]
        )
        self.assertEqual(tags, ("deepinfra/fp4",))
        self.assertEqual(ceiling, 131072)

    def test_ecarte_les_statuts_negatifs(self):
        tags, _ = translate._openrouter_pin(
            [_endpoint("a/fp8", 131072, status=-2), _endpoint("b/fp8", 131072, status=0)]
        )
        self.assertEqual(tags, ("b/fp8",))

    def test_plafond_non_declare_ecarte(self):
        """`None` est un inconnu ; l'objet de cette fonction est de ne rien
        laisser au hasard."""
        tags, _ = translate._openrouter_pin([_endpoint("a/fp8", None)])
        self.assertEqual(tags, ())

    def test_plafond_commun_est_le_minimum(self):
        _, ceiling = translate._openrouter_pin(
            [_endpoint("a/fp8", 16000), _endpoint("b/fp8", 131072)]
        )
        self.assertEqual(ceiling, 16000)

    def test_aucun_hebergeur_utilisable(self):
        tags, ceiling = translate._openrouter_pin([_endpoint("a/fp8", 2048)])
        self.assertEqual((tags, ceiling), ((), 0))


class TestExtraBody(unittest.TestCase):
    def test_allow_fallbacks_toujours_faux(self):
        """Sans lui, `only` n'est qu'une préférence et le routeur repart vers un
        hébergeur écarté — le préflight ne vaudrait plus rien."""
        body = translate._openrouter_extra_body(_client(), _args())
        self.assertIs(body["provider"]["allow_fallbacks"], False)
        self.assertEqual(body["provider"]["only"], ["deepinfra/fp4"])

    def test_raisonnement_coupe_par_defaut(self):
        body = translate._openrouter_extra_body(_client(mandatory=False), _args())
        self.assertEqual(body["reasoning"], {"enabled": False})

    def test_effort_le_plus_bas_quand_le_modele_impose(self):
        """Mesuré sur z-ai/glm-5.3-flash, dont le défaut est `max` : laisser ce
        défaut sature les 32 768 tokens AVANT la fin de la traduction. Monter
        `max_tokens` n'y changerait rien, l'effort en alloue un pourcentage."""
        body = translate._openrouter_extra_body(
            _client(mandatory=True, efforts=("max", "high", "low")), _args()
        )
        self.assertEqual(body["reasoning"], {"effort": "low"})

    def test_rien_envoye_si_le_modele_impose_sans_effort_connu(self):
        """Repli : un catalogue qui n'annonce aucun effort exploitable laisse le
        modèle à son réglage, plutôt que d'envoyer une valeur inventée."""
        body = translate._openrouter_extra_body(_client(mandatory=True), _args())
        self.assertNotIn("reasoning", body)

    def test_effort_le_plus_bas_ignore_les_valeurs_inconnues(self):
        self.assertEqual(translate._openrouter_lowest_effort(("ultra", "high", "medium")), "medium")
        self.assertIsNone(translate._openrouter_lowest_effort(("ultra",)))
        self.assertIsNone(translate._openrouter_lowest_effort(()))

    def test_effort_explicite_transmis(self):
        body = translate._openrouter_extra_body(_client(), _args(reasoning_effort="low"))
        self.assertEqual(body["reasoning"], {"effort": "low"})

    def test_effort_none_sur_modele_imposant_nenvoie_rien(self):
        body = translate._openrouter_extra_body(
            _client(mandatory=True), _args(reasoning_effort="none")
        )
        self.assertNotIn("reasoning", body)

    def test_aucun_avertissement_par_segment(self):
        """Cette fonction est appelée à CHAQUE segment : un avertissement ici
        se répéterait vingt fois sur un README. Il vit dans le préflight."""
        stderr = io.StringIO()
        with patch("sys.stderr", stderr):
            translate._openrouter_extra_body(
                _client(mandatory=True), _args(reasoning_effort="none")
            )
        self.assertEqual(stderr.getvalue(), "")

    def test_libelle_de_raisonnement_suit_ce_qui_est_envoye(self):
        """Le libellé du préflight disait « coupé » alors qu'un effort explicite
        partait dans la requête."""
        self.assertEqual(translate._openrouter_reasoning_label(_client(), _args()), "coupé")
        self.assertIn(
            "'low'",
            translate._openrouter_reasoning_label(_client(), _args(reasoning_effort="low")),
        )
        self.assertIn(
            "imposé",
            translate._openrouter_reasoning_label(_client(mandatory=True), _args()),
        )


class TestContratDeSortie(unittest.TestCase):
    def test_texte_normal(self):
        client = _client()
        client.client.chat.completions.create.return_value = SimpleNamespace(
            choices=[_choice("Hello")]
        )
        self.assertEqual(translate._call_openrouter(client, _args(), "p", "s"), "Hello")

    def test_end_turn_accepte(self):
        client = _client()
        client.client.chat.completions.create.return_value = SimpleNamespace(
            choices=[_choice("Hello", finish="end_turn")]
        )
        self.assertEqual(translate._call_openrouter(client, _args(), "p", "s"), "Hello")

    def test_erreur_dans_un_200(self):
        """Mesuré : le routeur répond 200 avec un corps qui ne porte qu'une
        erreur quand l'hébergeur amont échoue."""
        client = _client()
        client.client.chat.completions.create.return_value = SimpleNamespace(
            choices=None, error={"message": "upstream down", "code": 502}
        )
        with self.assertRaises(RuntimeError) as ctx:
            translate._call_openrouter(client, _args(), "p", "s")
        self.assertIn("upstream down", str(ctx.exception))

    def test_aucun_choix(self):
        client = _client()
        client.client.chat.completions.create.return_value = SimpleNamespace(choices=[])
        with self.assertRaises(RuntimeError) as ctx:
            translate._call_openrouter(client, _args(), "p", "s")
        self.assertIn("aucun choix", str(ctx.exception))

    def test_page_blanche_distinguee_de_la_troncature(self):
        """Budget consommé par le raisonnement : relancer à l'identique ne
        changerait rien, le message doit le dire."""
        client = _client()
        client.client.chat.completions.create.return_value = SimpleNamespace(
            choices=[_choice("", finish="length")]
        )
        with self.assertRaises(RuntimeError) as ctx:
            translate._call_openrouter(client, _args(), "p", "s")
        message = str(ctx.exception)
        self.assertIn("raisonnement", message)
        self.assertNotIn("tronquée", message)

    def test_vraie_troncature(self):
        client = _client()
        client.client.chat.completions.create.return_value = SimpleNamespace(
            choices=[_choice("début de trad", finish="length")]
        )
        with self.assertRaises(RuntimeError) as ctx:
            translate._call_openrouter(client, _args(), "p", "s")
        self.assertIn("tronquée", str(ctx.exception))

    def test_hebergeur_interrompt_la_generation(self):
        """Mesuré : deux segments coupés à 750 s, finish_reason normalisé à
        `error` et natif à None. C'est une panne amont, le message doit le dire
        pour ne pas envoyer chercher un défaut dans le document."""
        client = _client()
        client.client.chat.completions.create.return_value = SimpleNamespace(
            choices=[_choice("", finish="error")]
        )
        with self.assertRaises(RuntimeError) as ctx:
            translate._call_openrouter(client, _args(), "p", "s")
        self.assertIn("hébergeur", str(ctx.exception))
        self.assertIn("pas côté", str(ctx.exception))

    def test_finish_reason_anormal(self):
        client = _client()
        client.client.chat.completions.create.return_value = SimpleNamespace(
            choices=[_choice("x", finish="content_filter", native="blocked")]
        )
        with self.assertRaises(RuntimeError) as ctx:
            translate._call_openrouter(client, _args(), "p", "s")
        self.assertIn("content_filter", str(ctx.exception))
        self.assertIn("blocked", str(ctx.exception))

    def test_content_none(self):
        client = _client()
        client.client.chat.completions.create.return_value = SimpleNamespace(
            choices=[_choice(None)]
        )
        with self.assertRaises(RuntimeError) as ctx:
            translate._call_openrouter(client, _args(), "p", "s")
        self.assertIn("empty content", str(ctx.exception))

    def test_max_tokens_transmis(self):
        client = _client(max_tokens=16000)
        client.client.chat.completions.create.return_value = SimpleNamespace(
            choices=[_choice("ok")]
        )
        translate._call_openrouter(client, _args(), "p", "s")
        self.assertEqual(
            client.client.chat.completions.create.call_args.kwargs["max_tokens"], 16000
        )


class TestPreflight(unittest.TestCase):
    """Le préflight est fail-closed : pas de catalogue, pas de traduction."""

    def _urlopen(self, payloads):
        def reponse(payload):
            body = json.dumps(payload).encode("utf-8")
            return MagicMock(
                __enter__=MagicMock(return_value=SimpleNamespace(read=lambda: body)),
                __exit__=MagicMock(return_value=False),
            )

        def fake(url, timeout=None):
            for fragment, payload in payloads.items():
                if fragment in url:
                    return reponse(payload)
            raise AssertionError(f"URL inattendue : {url}")

        return fake

    def test_slug_absent_du_catalogue(self):
        with (
            patch(
                "urllib.request.urlopen", self._urlopen({"models": {"data": [{"id": "autre/x"}]}})
            ),
            self.assertRaises(ValueError) as ctx,
        ):
            translate._openrouter_catalog_entry(None, "z-ai/glm-5.2")
        self.assertIn("inconnu", str(ctx.exception))

    def test_reseau_injoignable_leve(self):
        with (
            patch("urllib.request.urlopen", side_effect=OSError("nom introuvable")),
            self.assertRaises(ValueError) as ctx,
        ):
            translate._openrouter_http_get(None, "models")
        self.assertIn("injoignable", str(ctx.exception))

    def test_base_url_non_https_refusee(self):
        with self.assertRaises(ValueError) as ctx:
            translate._openrouter_http_get("http://openrouter.ai/api/v1", "models")
        self.assertIn("https://", str(ctx.exception))

    def test_init_renseigne_la_fenetre_de_contexte(self):
        """DEFAULT_TOKEN_LIMIT est faux pour 44 modèles du catalogue : la vraie
        fenêtre vient du préflight, pas d'une constante."""
        catalogue = {
            "data": [
                {"id": "z-ai/glm-5.2", "context_length": 1048576, "reasoning": {"mandatory": False}}
            ]
        }  # `supported_efforts` absent : le repli doit donner un tuple vide, pas None
        endpoints = {"data": {"endpoints": [_endpoint("deepinfra/fp4", 131072)]}}
        args = _args()
        limits_avant = dict(translate.MODEL_TOKEN_LIMITS)
        try:
            with (
                patch.dict(os.environ, {"OPENROUTER_API_KEY": _MARQUEUR}),
                patch(
                    "urllib.request.urlopen",
                    self._urlopen({"/endpoints": endpoints, "models": catalogue}),
                ),
                patch("aipmt.translate.OpenAI") as fake_openai,
            ):
                client = translate._init_openrouter_client(args)
            self.assertEqual(translate.MODEL_TOKEN_LIMITS["z-ai/glm-5.2"], 1048576)
            self.assertEqual(client.providers, ("deepinfra/fp4",))
            self.assertEqual(client.supported_efforts, ())
            self.assertEqual(client.max_tokens, 32768)
            self.assertFalse(client.reasoning_mandatory)
            self.assertEqual(
                fake_openai.call_args.kwargs["base_url"], translate.OPENROUTER_BASE_URL
            )
        finally:
            translate.MODEL_TOKEN_LIMITS.clear()
            translate.MODEL_TOKEN_LIMITS.update(limits_avant)

    def test_init_refuse_si_aucun_hebergeur_sain(self):
        catalogue = {"data": [{"id": "z-ai/glm-5.2", "context_length": 100}]}
        endpoints = {"data": {"endpoints": [_endpoint("sail-research/fp8", 2048)]}}
        with (
            patch.dict(os.environ, {"OPENROUTER_API_KEY": _MARQUEUR}),
            patch(
                "urllib.request.urlopen",
                self._urlopen({"/endpoints": endpoints, "models": catalogue}),
            ),
            self.assertRaises(ValueError) as ctx,
        ):
            translate._init_openrouter_client(_args())
        self.assertIn("troncature", str(ctx.exception))

    def test_init_sans_cle(self):
        with (
            patch.dict(os.environ, {"OPENROUTER_API_KEY": ""}),
            self.assertRaises(ValueError) as ctx,
        ):
            translate._init_openrouter_client(_args())
        self.assertIn("OPENROUTER_API_KEY", str(ctx.exception))


class TestIntegrationCLI(unittest.TestCase):
    def test_dispatch(self):
        with patch.object(translate, "_call_openrouter", return_value="traduit") as appel:
            texte = translate._dispatch_provider_call(
                _client(), _args(), "p", "s", "openrouter", False
            )
        self.assertEqual(texte, "traduit")
        appel.assert_called_once()

    def test_resolve_provider(self):
        self.assertEqual(translate._resolve_provider(_args()), "openrouter")

    def test_flag_exclusif(self):
        """Deux flags provider simultanés partaient jusqu'ici en facturation
        silencieuse : argparse doit refuser la combinaison."""
        parser = argparse.ArgumentParser()
        translate._add_provider_args(parser)
        self.assertTrue(parser.parse_args(["--use_openrouter"]).use_openrouter)
        for autre in ("--use_codex", "--use_mistral", "--use_grok", "--use_opencode"):
            with patch("sys.stderr", io.StringIO()), self.assertRaises(SystemExit):
                parser.parse_args(["--use_openrouter", autre])

    def test_libelle_du_provider(self):
        self.assertEqual(translate._PROVIDER_LABELS["openrouter"], "OpenRouter")

    def test_nom_de_fichier_sans_separateur(self):
        """`--include_model` avec un slug ne doit pas fabriquer de sous-chemin."""
        self.assertEqual(translate._model_filename_label("z-ai/glm-5.2"), "z-ai-glm-5.2")


if __name__ == "__main__":
    unittest.main()
