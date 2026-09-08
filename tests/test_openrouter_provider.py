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

from openai._models import construct_type
from openai.types.chat import ChatCompletion

from aipmt import naming, segmentation
from aipmt.providers import openai as openai_provider
from aipmt.providers import openrouter, registry

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


def _choice(content="Bonjour", finish="stop", native=None, **extra):
    """Un choix de réponse ; `error=` pose l'erreur que `NonStreamingChoice`
    autorise à côté du contenu, `message=None` le choix sans message du tout."""
    message = SimpleNamespace(content=content) if content is not None else None
    return SimpleNamespace(
        message=message,
        finish_reason=finish,
        native_finish_reason=native,
        **extra,
    )


def _client(providers=("deepinfra/fp4",), max_tokens=32768, mandatory=False, efforts=()):
    return openrouter._OpenRouterClient(
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
            openrouter._openrouter_validate_model(None)
        self.assertIn("fournisseur/modèle", str(ctx.exception))
        self.assertIn("openrouter.ai/models", str(ctx.exception))

    def test_model_sans_namespace_refuse(self):
        with self.assertRaises(ValueError):
            openrouter._openrouter_validate_model("glm-5.2")

    def test_segment_parent_refuse(self):
        """La regex commune aux providers namespacés accepte `a/b/..` ; ce slug
        détournerait l'URL de préflight, d'où le refus explicite."""
        with self.assertRaises(ValueError):
            openrouter._openrouter_validate_model("z-ai/glm/..")

    def test_slugs_reels_acceptes(self):
        for slug in ("z-ai/glm-5.2", "qwen/qwen3.8-flash", "moonshotai/kimi-k2.6"):
            openrouter._openrouter_validate_model(slug)


class TestPin(unittest.TestCase):
    """Épinglage des hébergeurs : le cœur du provider."""

    def test_ecarte_les_plafonds_trop_bas(self):
        """Mesuré : `sail-research/fp8` sert glm-5.3-flash avec 2 048 tokens de
        sortie. Sans ce filtre, une traduction sur 23 partait tronquée."""
        tags, ceiling = openrouter._openrouter_pin(
            [_endpoint("sail-research/fp8", 2048), _endpoint("deepinfra/fp4", 131072)]
        )
        self.assertEqual(tags, ("deepinfra/fp4",))
        self.assertEqual(ceiling, 131072)

    def test_ecarte_les_statuts_negatifs(self):
        tags, _ = openrouter._openrouter_pin(
            [_endpoint("a/fp8", 131072, status=-2), _endpoint("b/fp8", 131072, status=0)]
        )
        self.assertEqual(tags, ("b/fp8",))

    def test_plafond_non_declare_ecarte(self):
        """`None` est un inconnu ; l'objet de cette fonction est de ne rien
        laisser au hasard."""
        tags, _ = openrouter._openrouter_pin([_endpoint("a/fp8", None)])
        self.assertEqual(tags, ())

    def test_plafond_commun_est_le_minimum(self):
        _, ceiling = openrouter._openrouter_pin(
            [_endpoint("a/fp8", 16000), _endpoint("b/fp8", 131072)]
        )
        self.assertEqual(ceiling, 16000)

    def test_aucun_hebergeur_utilisable(self):
        tags, ceiling = openrouter._openrouter_pin([_endpoint("a/fp8", 2048)])
        self.assertEqual((tags, ceiling), ((), 0))


class TestHelpersDuPreflight(unittest.TestCase):
    """Les trois helpers nés de la scission de `_openrouter_pin` et
    `_init_openrouter_client` pour Codacy, testés seuls en plus des tests de
    bout en bout : le filtre d'hébergeur, les contraintes de raisonnement lues
    au catalogue, la clé."""

    def test_endpoint_usable(self):
        usable = openrouter._openrouter_endpoint_usable
        self.assertTrue(usable(_endpoint("a/fp8", 131072)))
        self.assertFalse(usable(_endpoint("a/fp8", 131072, status=-1)))
        self.assertFalse(usable(_endpoint("a/fp8", None)))
        self.assertFalse(usable(_endpoint("a/fp8", 2048)))
        # Statut absent = sain ; le plancher lui-même est accepté.
        self.assertTrue(
            usable({"max_completion_tokens": openrouter.OPENROUTER_MIN_COMPLETION_TOKENS})
        )

    def test_reasoning_constraints(self):
        constraints = openrouter._openrouter_reasoning_constraints
        self.assertEqual(constraints({}), (False, ()))
        self.assertEqual(constraints({"reasoning": None}), (False, ()))
        self.assertEqual(
            constraints({"reasoning": {"mandatory": True, "supported_efforts": ["low", "high"]}}),
            (True, ("low", "high")),
        )

    def test_api_key(self):
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": _MARQUEUR}):
            self.assertEqual(openrouter._openrouter_api_key(), _MARQUEUR)
        with patch.dict(os.environ):
            os.environ.pop("OPENROUTER_API_KEY", None)
            with self.assertRaises(ValueError) as ctx:
                openrouter._openrouter_api_key()
            self.assertIn("OPENROUTER_API_KEY", str(ctx.exception))
        for valeur in ("", openrouter.DEFAULT_OPENROUTER_API_KEY):
            with (
                patch.dict(os.environ, {"OPENROUTER_API_KEY": valeur}),
                self.assertRaises(ValueError),
            ):
                openrouter._openrouter_api_key()


class TestExtraBody(unittest.TestCase):
    def test_allow_fallbacks_toujours_faux(self):
        """Sans lui, `only` n'est qu'une préférence et le routeur repart vers un
        hébergeur écarté — le préflight ne vaudrait plus rien."""
        body = openrouter._openrouter_extra_body(_client(), _args())
        self.assertIs(body["provider"]["allow_fallbacks"], False)
        self.assertEqual(body["provider"]["only"], ["deepinfra/fp4"])

    def test_raisonnement_coupe_par_defaut(self):
        body = openrouter._openrouter_extra_body(_client(mandatory=False), _args())
        self.assertEqual(body["reasoning"], {"enabled": False})

    def test_effort_le_plus_bas_quand_le_modele_impose(self):
        """Mesuré sur z-ai/glm-5.3-flash, dont le défaut est `max` : laisser ce
        défaut sature les 32 768 tokens AVANT la fin de la traduction. Monter
        `max_tokens` n'y changerait rien, l'effort en alloue un pourcentage."""
        body = openrouter._openrouter_extra_body(
            _client(mandatory=True, efforts=("max", "high", "low")), _args()
        )
        self.assertEqual(body["reasoning"], {"effort": "low"})

    def test_rien_envoye_si_le_modele_impose_sans_effort_connu(self):
        """Repli : un catalogue qui n'annonce aucun effort exploitable laisse le
        modèle à son réglage, plutôt que d'envoyer une valeur inventée."""
        body = openrouter._openrouter_extra_body(_client(mandatory=True), _args())
        self.assertNotIn("reasoning", body)

    def test_effort_le_plus_bas_ignore_les_valeurs_inconnues(self):
        self.assertEqual(
            openrouter._openrouter_lowest_effort(("ultra", "high", "medium")), "medium"
        )
        self.assertIsNone(openrouter._openrouter_lowest_effort(("ultra",)))
        self.assertIsNone(openrouter._openrouter_lowest_effort(()))

    def test_effort_explicite_transmis(self):
        body = openrouter._openrouter_extra_body(_client(), _args(reasoning_effort="low"))
        self.assertEqual(body["reasoning"], {"effort": "low"})

    def test_effort_none_sur_modele_imposant_nenvoie_rien(self):
        body = openrouter._openrouter_extra_body(
            _client(mandatory=True), _args(reasoning_effort="none")
        )
        self.assertNotIn("reasoning", body)

    def test_aucun_avertissement_par_segment(self):
        """Cette fonction est appelée à CHAQUE segment : un avertissement ici
        se répéterait vingt fois sur un README. Il vit dans le préflight."""
        stderr = io.StringIO()
        with patch("sys.stderr", stderr):
            openrouter._openrouter_extra_body(
                _client(mandatory=True), _args(reasoning_effort="none")
            )
        self.assertEqual(stderr.getvalue(), "")

    def test_libelle_de_raisonnement_suit_ce_qui_est_envoye(self):
        """Le libellé du préflight disait « coupé » alors qu'un effort explicite
        partait dans la requête."""
        self.assertEqual(openrouter._openrouter_reasoning_label(_client(), _args()), "coupé")
        self.assertIn(
            "'low'",
            openrouter._openrouter_reasoning_label(_client(), _args(reasoning_effort="low")),
        )
        self.assertIn(
            "imposé",
            openrouter._openrouter_reasoning_label(_client(mandatory=True), _args()),
        )


class TestContratDeSortie(unittest.TestCase):
    def test_texte_normal(self):
        client = _client()
        client.client.chat.completions.create.return_value = SimpleNamespace(
            choices=[_choice("Hello")]
        )
        self.assertEqual(openrouter._call_openrouter(client, _args(), "p", "s"), "Hello")

    def test_end_turn_accepte(self):
        client = _client()
        client.client.chat.completions.create.return_value = SimpleNamespace(
            choices=[_choice("Hello", finish="end_turn")]
        )
        self.assertEqual(openrouter._call_openrouter(client, _args(), "p", "s"), "Hello")

    def test_erreur_dans_un_200(self):
        """Mesuré : le routeur répond 200 avec un corps qui ne porte qu'une
        erreur quand l'hébergeur amont échoue."""
        client = _client()
        client.client.chat.completions.create.return_value = SimpleNamespace(
            choices=None, error={"message": "upstream down", "code": 502}
        )
        args = _args()
        with self.assertRaises(RuntimeError) as ctx:
            openrouter._call_openrouter(client, args, "p", "s")
        self.assertIn("upstream down", str(ctx.exception))

    def _refus(self, **kw):
        """Appelle le provider sur un choix donné et rend le message d'erreur."""
        client = _client()
        client.client.chat.completions.create.return_value = SimpleNamespace(
            choices=[_choice(**kw)]
        )
        args = _args()
        with self.assertRaises(RuntimeError) as ctx:
            openrouter._call_openrouter(client, args, "p", "s")
        return str(ctx.exception)

    def test_erreur_dans_le_choix_refuse_le_contenu_partiel(self):
        """Type documenté `NonStreamingChoice.error` : l'erreur amont peut être
        portée par le choix, à côté d'un contenu partiel, que `finish_reason`
        soit `error`, `stop` ou nul."""
        for finish in ("error", None, "stop"):
            with self.subTest(finish=finish):
                message = self._refus(
                    content="partial translation",
                    finish=finish,
                    error={"code": 502, "message": "Provider disconnected mid-stream"},
                )
                self.assertIn("disconnected mid-stream", message)
                self.assertIn("partiel", message)
                # Le conseil du cas `finish_reason=error` ne doit pas disparaître
                # parce que l'erreur est aussi portée par le choix.
                self.assertIn("restreindre les hébergeurs", message)

    def test_erreur_presente_mais_vide_refuse_aussi(self):
        """`if choice_error:` laissait passer le contenu partiel sur un objet
        présent mais faux — mesuré sur `{}`, `""`, `0` et `False`."""
        for vide in ({}, "", 0, False, []):
            with self.subTest(erreur=repr(vide)):
                message = self._refus(content="partial", finish=None, error=vide)
                self.assertIn("interrompu la génération", message)

    def test_le_detail_reste_diagnosticable_si_le_message_est_vide(self):
        """`.get("message", error)` rendait une chaîne vide ou `None` : le
        message d'erreur ne nommait plus aucune cause."""
        for erreur in ({"message": ""}, {"message": None}, {"code": 502}):
            with self.subTest(erreur=erreur):
                message = self._refus(content="partial", finish=None, error=erreur)
                self.assertIn("502" if "code" in erreur else "message", message)
                self.assertNotIn(" : . ", message)

    def test_aucun_contenu_perdu_nest_annonce_quand_il_ny_en_a_pas(self):
        """Sur un choix en échec, le SDK laisse `message` à None : annoncer un
        contenu partiel refusé enverrait chercher une troncature inexistante."""
        message = self._refus(content=None, finish="error", error={"message": "boom"})
        self.assertIn("boom", message)
        self.assertNotIn("partiel", message)

    def test_le_champ_error_survit_au_sdk_verrouille(self):
        """La garde ne tient que parce que le modèle du SDK accepte les champs
        supplémentaires : `error` n'appartient pas au schéma d'OpenAI, il vient
        d'OpenRouter. Une version qui les rejetterait rendrait la garde muette
        sans faire rougir un seul test à base de doublures — d'où cette
        construction par le SDK lui-même."""
        raw = {
            "id": "gen-1",
            "object": "chat.completion",
            "created": 0,
            "model": "z-ai/glm-5.2",
            "choices": [
                {
                    "index": 0,
                    "finish_reason": None,
                    "native_finish_reason": None,
                    "message": {"role": "assistant", "content": "partial"},
                    "error": {"code": 502, "message": "Provider disconnected mid-stream"},
                }
            ],
        }
        response = construct_type(value=raw, type_=ChatCompletion)
        choice = response.choices[0]
        self.assertEqual(getattr(choice, "error", None), raw["choices"][0]["error"])
        client = _client()
        client.client.chat.completions.create.return_value = response
        args = _args()
        with self.assertRaises(RuntimeError) as ctx:
            openrouter._call_openrouter(client, args, "p", "s")
        self.assertIn("disconnected mid-stream", str(ctx.exception))

    def test_aucun_choix(self):
        client = _client()
        client.client.chat.completions.create.return_value = SimpleNamespace(choices=[])
        args = _args()
        with self.assertRaises(RuntimeError) as ctx:
            openrouter._call_openrouter(client, args, "p", "s")
        self.assertIn("aucun choix", str(ctx.exception))

    def test_page_blanche_distinguee_de_la_troncature(self):
        """Budget consommé par le raisonnement : relancer à l'identique ne
        changerait rien, le message doit le dire."""
        client = _client()
        client.client.chat.completions.create.return_value = SimpleNamespace(
            choices=[_choice("", finish="length")]
        )
        args = _args()
        with self.assertRaises(RuntimeError) as ctx:
            openrouter._call_openrouter(client, args, "p", "s")
        message = str(ctx.exception)
        self.assertIn("raisonnement", message)
        self.assertNotIn("tronquée", message)

    def test_vraie_troncature(self):
        client = _client()
        client.client.chat.completions.create.return_value = SimpleNamespace(
            choices=[_choice("début de trad", finish="length")]
        )
        args = _args()
        with self.assertRaises(RuntimeError) as ctx:
            openrouter._call_openrouter(client, args, "p", "s")
        self.assertIn("tronquée", str(ctx.exception))

    def test_hebergeur_interrompt_la_generation(self):
        """Mesuré : deux segments coupés à 750 s, finish_reason normalisé à
        `error` et natif à None. C'est une panne amont, le message doit le dire
        pour ne pas envoyer chercher un défaut dans le document."""
        client = _client()
        client.client.chat.completions.create.return_value = SimpleNamespace(
            choices=[_choice("", finish="error")]
        )
        args = _args()
        with self.assertRaises(RuntimeError) as ctx:
            openrouter._call_openrouter(client, args, "p", "s")
        self.assertIn("hébergeur", str(ctx.exception))
        self.assertIn("pas côté", str(ctx.exception))

    def test_finish_reason_anormal(self):
        client = _client()
        client.client.chat.completions.create.return_value = SimpleNamespace(
            choices=[_choice("x", finish="content_filter", native="blocked")]
        )
        args = _args()
        with self.assertRaises(RuntimeError) as ctx:
            openrouter._call_openrouter(client, args, "p", "s")
        self.assertIn("content_filter", str(ctx.exception))
        self.assertIn("blocked", str(ctx.exception))

    def test_content_none(self):
        client = _client()
        client.client.chat.completions.create.return_value = SimpleNamespace(
            choices=[_choice(None)]
        )
        args = _args()
        with self.assertRaises(RuntimeError) as ctx:
            openrouter._call_openrouter(client, args, "p", "s")
        self.assertIn("empty content", str(ctx.exception))

    def test_max_tokens_transmis(self):
        client = _client(max_tokens=16000)
        client.client.chat.completions.create.return_value = SimpleNamespace(
            choices=[_choice("ok")]
        )
        openrouter._call_openrouter(client, _args(), "p", "s")
        self.assertEqual(
            client.client.chat.completions.create.call_args.kwargs["max_tokens"], 16000
        )


def _fake_urlopen(payloads):
    """`urlopen` simulé : la réponse est choisie par fragment d'URL."""

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


class TestPreflight(unittest.TestCase):
    """Le préflight est fail-closed : pas de catalogue, pas de traduction."""

    def _urlopen(self, payloads):
        return _fake_urlopen(payloads)

    def test_slug_absent_du_catalogue(self):
        with (
            patch(
                "urllib.request.urlopen", self._urlopen({"models": {"data": [{"id": "autre/x"}]}})
            ),
            self.assertRaises(ValueError) as ctx,
        ):
            openrouter._openrouter_catalog_entry(None, "z-ai/glm-5.2")
        self.assertIn("inconnu", str(ctx.exception))

    def test_reseau_injoignable_leve(self):
        with (
            patch("urllib.request.urlopen", side_effect=OSError("nom introuvable")),
            self.assertRaises(ValueError) as ctx,
        ):
            openrouter._openrouter_http_get(None, "models")
        self.assertIn("injoignable", str(ctx.exception))

    def test_base_url_non_https_refusee(self):
        with self.assertRaises(ValueError) as ctx:
            openrouter._openrouter_http_get("http://openrouter.ai/api/v1", "models")
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
        limits_avant = dict(segmentation.MODEL_TOKEN_LIMITS)
        try:
            with (
                patch.dict(os.environ, {"OPENROUTER_API_KEY": _MARQUEUR}),
                patch(
                    "urllib.request.urlopen",
                    self._urlopen({"/endpoints": endpoints, "models": catalogue}),
                ),
                patch("aipmt.providers.openrouter.OpenAI") as fake_openai,
            ):
                client = openrouter._init_openrouter_client(args)
            self.assertEqual(segmentation.MODEL_TOKEN_LIMITS["z-ai/glm-5.2"], 1048576)
            self.assertEqual(client.providers, ("deepinfra/fp4",))
            self.assertEqual(client.supported_efforts, ())
            self.assertEqual(client.max_tokens, 32768)
            self.assertFalse(client.reasoning_mandatory)
            self.assertEqual(
                fake_openai.call_args.kwargs["base_url"], openrouter.OPENROUTER_BASE_URL
            )
        finally:
            segmentation.MODEL_TOKEN_LIMITS.clear()
            segmentation.MODEL_TOKEN_LIMITS.update(limits_avant)

    def test_init_refuse_si_aucun_hebergeur_sain(self):
        catalogue = {"data": [{"id": "z-ai/glm-5.2", "context_length": 100}]}
        endpoints = {"data": {"endpoints": [_endpoint("sail-research/fp8", 2048)]}}
        args = _args()
        urlopen = self._urlopen({"/endpoints": endpoints, "models": catalogue})
        with (
            patch.dict(os.environ, {"OPENROUTER_API_KEY": _MARQUEUR}),
            patch("urllib.request.urlopen", urlopen),
            self.assertRaises(ValueError) as ctx,
        ):
            openrouter._init_openrouter_client(args)
        self.assertIn("troncature", str(ctx.exception))

    def test_init_sans_cle(self):
        args = _args()
        with (
            patch.dict(os.environ, {"OPENROUTER_API_KEY": ""}),
            self.assertRaises(ValueError) as ctx,
        ):
            openrouter._init_openrouter_client(args)
        self.assertIn("OPENROUTER_API_KEY", str(ctx.exception))


class TestIntegrationCLI(unittest.TestCase):
    def test_dispatch(self):
        with patch.object(registry, "_call_openrouter", return_value="traduit") as appel:
            texte = registry._dispatch_provider_call(
                _client(), _args(), "p", "s", "openrouter", False
            )
        self.assertEqual(texte, "traduit")
        appel.assert_called_once()

    def test_resolve_provider(self):
        self.assertEqual(registry._resolve_provider(_args()), "openrouter")

    def test_flag_exclusif(self):
        """Deux flags provider simultanés partaient jusqu'ici en facturation
        silencieuse : argparse doit refuser la combinaison."""
        parser = argparse.ArgumentParser()
        registry._add_provider_args(parser)
        self.assertTrue(parser.parse_args(["--use_openrouter"]).use_openrouter)
        for autre in ("--use_codex", "--use_mistral", "--use_grok", "--use_opencode"):
            with patch("sys.stderr", io.StringIO()), self.assertRaises(SystemExit):
                parser.parse_args(["--use_openrouter", autre])

    def test_libelle_du_provider(self):
        self.assertEqual(registry._PROVIDER_LABELS["openrouter"], "OpenRouter")

    def test_nom_de_fichier_sans_separateur(self):
        """`--include_model` avec un slug ne doit pas fabriquer de sous-chemin."""
        self.assertEqual(naming._model_filename_label("z-ai/glm-5.2"), "z-ai-glm-5.2")


class TestRequeteReelle(unittest.TestCase):
    """Ce que reçoit le SDK, pas ce que produisent les helpers : retirer
    `extra_body=` de l'appel laissait 42 tests verts (mesuré par mutation)."""

    def _create_kwargs(self, client, args):
        client.client.chat.completions.create.return_value = SimpleNamespace(
            choices=[_choice("Hello")]
        )
        self.assertEqual(openrouter._call_openrouter(client, args, "p", "s"), "Hello")
        return client.client.chat.completions.create.call_args.kwargs

    def test_epinglage_et_raisonnement_coupe_partent_dans_la_requete(self):
        client = _client(providers=("deepinfra/fp4", "novita/fp8"), max_tokens=16000)
        args = _args()
        kwargs = self._create_kwargs(client, args)
        self.assertEqual(kwargs["model"], "z-ai/glm-5.2")
        self.assertEqual(kwargs["max_tokens"], 16000)
        self.assertEqual(kwargs["messages"], openai_provider._build_openai_messages(args, "p", "s"))
        self.assertEqual(
            kwargs["extra_body"],
            {
                "provider": {"only": ["deepinfra/fp4", "novita/fp8"], "allow_fallbacks": False},
                "reasoning": {"enabled": False},
            },
        )

    def test_effort_le_plus_bas_part_dans_la_requete_quand_le_modele_impose(self):
        kwargs = self._create_kwargs(
            _client(mandatory=True, efforts=("high", "low", "max")), _args()
        )
        self.assertEqual(kwargs["extra_body"]["reasoning"], {"effort": "low"})
        self.assertFalse(kwargs["extra_body"]["provider"]["allow_fallbacks"])

    def test_effort_explicite_part_dans_la_requete(self):
        kwargs = self._create_kwargs(_client(), _args(reasoning_effort="high"))
        self.assertEqual(kwargs["extra_body"]["reasoning"], {"effort": "high"})


class TestBudgetDeContexteParAppel(unittest.TestCase):
    """`context_length` couvre l'entrée ET la sortie. Une réserve fixe calibrée
    sur du texte latin ne borne rien : mesuré au tokenizer `o200k_base`,
    16 000 caractères valent 3 200 tokens en français, 12 300 en japonais et
    17 500 en emoji. Le budget est donc recalculé sur le texte réellement
    envoyé, et l'invariant entrée + sortie ≤ contexte tient par construction."""

    PROMPT = "P" * 6064  # taille mesurée du prompt système, cible anglaise

    def _budget(self, segment, context_length, max_tokens=32768):
        client = _client(max_tokens=max_tokens)
        client.context_length = context_length
        return openrouter._openrouter_call_budget(client, _args(), self.PROMPT, segment)

    def test_l_estimation_majore_sur_toutes_les_ecritures(self):
        estime = openrouter._openrouter_estimated_tokens
        # Comptes relevés au tokenizer o200k_base sur ces échantillons exacts.
        for texte, reels in (
            ("Le découpage d'un module exige une preuve mécanique. ", 12),
            ("モジュールをパッケージに分割するには機械的な証明が必要です。", 30),
            ("将模块拆分为包需要机械证明。", 12),
            ("🇫🇷 🇯🇵 ✅ ⚠️ 🔥 ", 15),
        ):
            with self.subTest(texte=texte[:20]):
                self.assertGreaterEqual(estime(texte), reels)

    def test_entree_plus_sortie_tiennent_dans_la_fenetre(self):
        for label, segment, contexte in (
            ("français", "é" * 8000 + "a" * 8000, 32768),
            ("japonais", "モ" * 16000, 1048576),
            ("latin court", "a" * 2000, 32768),
        ):
            with self.subTest(label=label):
                budget = self._budget(segment, contexte)
                entree = openrouter._openrouter_estimated_tokens(
                    self.PROMPT
                ) + openrouter._openrouter_estimated_tokens(segment)
                self.assertLessEqual(entree + budget, contexte)

    def test_un_segment_dense_en_tokens_est_refuse_avant_l_appel(self):
        """Le cas que la réserve fixe laissait passer : 16 000 caractères
        japonais dans une fenêtre de 32 768."""
        for label, segment in (("japonais", "モ" * 16000), ("emoji", "🇫🇷" * 4000)):
            with self.subTest(label=label):
                with self.assertRaises(RuntimeError) as ctx:
                    self._budget(segment, 32768)
                self.assertIn("trop courte pour ce segment", str(ctx.exception))

    def test_le_plafond_du_preflight_reste_un_maximum(self):
        """Une immense fenêtre ne fait pas dépasser l'enveloppe du projet."""
        self.assertEqual(self._budget("a" * 100, 1048576, max_tokens=24368), 24368)

    def test_le_budget_part_bien_dans_la_requete(self):
        client = _client(max_tokens=32768)
        client.context_length = 32768
        client.client.chat.completions.create.return_value = SimpleNamespace(
            choices=[_choice("Hello")]
        )
        args = _args()
        segment = "a" * 4000
        openrouter._call_openrouter(client, args, self.PROMPT, segment)
        envoye = client.client.chat.completions.create.call_args.kwargs["max_tokens"]
        self.assertEqual(
            envoye, openrouter._openrouter_call_budget(client, args, self.PROMPT, segment)
        )
        self.assertLess(envoye, 32768)


class TestRaisonDeFinAbsente(unittest.TestCase):
    """`finish_reason` est `string | null` dans le type documenté de la réponse
    non streamée, sans condition : nul, la raison brute de l'amont fait foi ;
    absentes toutes deux, le contenu est accepté — le contenu vide, lui, est
    refusé par le dispatch."""

    def _call(self, finish, native, content="Hello"):
        client = _client()
        client.client.chat.completions.create.return_value = SimpleNamespace(
            choices=[_choice(content, finish=finish, native=native)]
        )
        return openrouter._call_openrouter(client, _args(), "p", "s")

    def test_nul_avec_natif_stop_accepte(self):
        self.assertEqual(self._call(None, "stop"), "Hello")

    def test_nul_avec_natif_end_turn_accepte(self):
        self.assertEqual(self._call(None, "end_turn"), "Hello")

    def test_nul_sans_natif_accepte(self):
        self.assertEqual(self._call(None, None), "Hello")

    def test_nul_avec_natif_max_tokens_est_une_troncature(self):
        with self.assertRaises(RuntimeError) as ctx:
            self._call(None, "max_tokens", content="début")
        self.assertIn("tronquée", str(ctx.exception))

    def test_nul_avec_natif_error_est_une_panne_amont(self):
        with self.assertRaises(RuntimeError) as ctx:
            self._call(None, "error")
        self.assertIn("hébergeur", str(ctx.exception))

    def test_nul_avec_natif_inconnu_refuse(self):
        with self.assertRaises(RuntimeError) as ctx:
            self._call(None, "content_filter")
        self.assertIn("anormal", str(ctx.exception))


_CATALOGUE = {
    "data": [{"id": "z-ai/glm-5.2", "context_length": 1048576, "reasoning": {"mandatory": False}}]
}
_ENDPOINTS = {"data": {"endpoints": [_endpoint("deepinfra/fp4", 131072)]}}


class TestPreflightDeBoutEnBout(unittest.TestCase):
    """L'initialisation exercée comme le CLI l'exerce, avec des valeurs qui
    DISCRIMINENT : un plafond sous 32 768, un modèle qui impose le raisonnement,
    une clé et un timeout précis. Mesuré par mutation avant ces tests : un
    plafond ignoré, un `mandatory` en dur ou un slug validé après les GET
    laissaient 42 tests verts."""

    def setUp(self):
        self._limits = dict(segmentation.MODEL_TOKEN_LIMITS)
        self.addCleanup(self._restore)

    def _restore(self):
        segmentation.MODEL_TOKEN_LIMITS.clear()
        segmentation.MODEL_TOKEN_LIMITS.update(self._limits)

    def _init(self, catalogue=_CATALOGUE, endpoints=_ENDPOINTS, args=None):
        with (
            patch.dict(os.environ, {"OPENROUTER_API_KEY": _MARQUEUR}),
            patch(
                "urllib.request.urlopen",
                _fake_urlopen({"/endpoints": endpoints, "models": catalogue}),
            ),
            patch("aipmt.providers.openrouter.OpenAI") as fake_openai,
        ):
            client = openrouter._init_openrouter_client(args or _args())
        return client, fake_openai

    def test_cle_url_et_timeout_transmis_au_client(self):
        with (
            patch.dict(os.environ, {"OPENROUTER_BASE_URL": "https://relais.example/api/v1"}),
            patch("sys.stdout", io.StringIO()) as sortie,
        ):
            _, fake_openai = self._init()
        kwargs = fake_openai.call_args.kwargs
        self.assertEqual(kwargs["api_key"], _MARQUEUR)
        self.assertEqual(kwargs["base_url"], "https://relais.example/api/v1")
        self.assertEqual(kwargs["timeout"], openrouter.OPENROUTER_TIMEOUT)
        # Un endpoint détourné — un `.env` de projet suffit à en poser un —
        # doit se voir : c'est la vraie clé qui partira dans l'en-tête.
        self.assertIn("endpoint https://relais.example/api/v1", sortie.getvalue())

    def test_l_endpoint_canonique_ne_pollue_pas_la_ligne_de_preflight(self):
        with patch("sys.stdout", io.StringIO()) as sortie:
            self._init()
        self.assertNotIn("endpoint", sortie.getvalue())

    def test_plafond_inferieur_et_efforts_lus_au_catalogue(self):
        catalogue = {
            "data": [
                {
                    "id": "z-ai/glm-5.2",
                    "context_length": 65536,
                    "reasoning": {"mandatory": True, "supported_efforts": ["low", "max"]},
                }
            ]
        }
        endpoints = {
            "data": {
                "endpoints": [_endpoint("deepinfra/fp4", 16000), _endpoint("novita/fp8", 40000)]
            }
        }
        client, _ = self._init(catalogue, endpoints)
        self.assertEqual(client.max_tokens, 16000)
        self.assertEqual(client.providers, ("deepinfra/fp4", "novita/fp8"))
        self.assertTrue(client.reasoning_mandatory)
        self.assertEqual(client.supported_efforts, ("low", "max"))
        self.assertEqual(segmentation.MODEL_TOKEN_LIMITS["z-ai/glm-5.2"], 65536)

    def test_effort_none_ignore_sur_modele_imposant_est_annonce(self):
        catalogue = {
            "data": [
                {
                    "id": "z-ai/glm-5.2",
                    "context_length": 65536,
                    "reasoning": {"mandatory": True, "supported_efforts": ["low"]},
                }
            ]
        }
        with patch("sys.stderr", io.StringIO()) as err:
            client, _ = self._init(catalogue, args=_args(reasoning_effort="none"))
        self.assertTrue(client.reasoning_mandatory)
        self.assertIn("--reasoning_effort=none ignoré", err.getvalue())

    def test_le_contexte_est_reserve_a_l_entree(self):
        """`context_length` couvre l'entrée ET la complétion : demander tout le
        plafond de sortie ne laissait plus de place au prompt ni au segment.
        Mesuré sur le catalogue : six modèles sont dans ce cas."""
        catalogue = {
            "data": [
                {"id": "z-ai/glm-5.2", "context_length": 32768, "reasoning": {"mandatory": False}}
            ]
        }
        endpoints = {"data": {"endpoints": [_endpoint("deepinfra/fp4", 29491)]}}
        client, _ = self._init(catalogue, endpoints)
        self.assertEqual(client.max_tokens, 32768 - openrouter.OPENROUTER_INPUT_RESERVE)

    def test_contexte_trop_court_refuse_avant_facturation(self):
        """Un contexte de 16 384 tokens ne laisse pas 8 000 tokens de sortie une
        fois l'entrée réservée : refuser ici évite de payer un refus amont."""
        catalogue = {
            "data": [
                {"id": "z-ai/glm-5.2", "context_length": 16384, "reasoning": {"mandatory": False}}
            ]
        }
        endpoints = {"data": {"endpoints": [_endpoint("deepinfra/fp4", 14745)]}}
        with self.assertRaises(ValueError) as ctx:
            self._init(catalogue, endpoints)
        message = str(ctx.exception)
        self.assertIn("Contexte trop court", message)
        self.assertIn("16384", message)

    def test_budget_de_sortie(self):
        budget = openrouter._openrouter_output_budget
        # Grande fenêtre : l'enveloppe demandée reste le plafond du projet.
        self.assertEqual(budget(1048576, 131072, "m"), openrouter.OPENROUTER_MAX_TOKENS)
        # Le plafond de l'hébergeur reste prioritaire s'il est plus bas.
        self.assertEqual(budget(65536, 16000, "m"), 16000)
        # Sinon c'est le contexte, moins la réserve d'entrée, qui tranche.
        self.assertEqual(budget(32768, 29491, "m"), 32768 - openrouter.OPENROUTER_INPUT_RESERVE)
        with self.assertRaises(ValueError):
            budget(16384, 14745, "m")

    def test_slug_invalide_refuse_avant_tout_reseau(self):
        args = _args(model="z-ai/glm/..")
        with (
            patch.dict(os.environ, {"OPENROUTER_API_KEY": _MARQUEUR}),
            patch("urllib.request.urlopen", side_effect=AssertionError("réseau interdit")),
            self.assertRaises(ValueError) as ctx,
        ):
            openrouter._init_openrouter_client(args)
        self.assertIn("invalide", str(ctx.exception))

    def test_cle_absente_refusee_avant_tout_reseau(self):
        args = _args()
        with (
            patch.dict(os.environ, {"OPENROUTER_API_KEY": ""}),
            patch("urllib.request.urlopen", side_effect=AssertionError("réseau interdit")),
            self.assertRaises(ValueError) as ctx,
        ):
            openrouter._init_openrouter_client(args)
        self.assertIn("OPENROUTER_API_KEY", str(ctx.exception))

    def test_catalogue_injoignable_refuse_sans_construire_de_client(self):
        args = _args()
        with (
            patch.dict(os.environ, {"OPENROUTER_API_KEY": _MARQUEUR}),
            patch("urllib.request.urlopen", side_effect=OSError("DNS")),
            patch("aipmt.providers.openrouter.OpenAI") as fake_openai,
            self.assertRaises(ValueError) as ctx,
        ):
            openrouter._init_openrouter_client(args)
        self.assertIn("injoignable", str(ctx.exception))
        fake_openai.assert_not_called()
        self.assertEqual(segmentation.MODEL_TOKEN_LIMITS, self._limits)

    def test_catalogue_en_erreur_nomme_l_erreur_pas_le_slug(self):
        catalogue = {"error": {"message": "upstream 503", "code": 503}}
        with self.assertRaises(ValueError) as ctx:
            self._init(catalogue)
        self.assertIn("upstream 503", str(ctx.exception))
        self.assertNotIn("inconnu", str(ctx.exception))

    def test_fiche_sans_context_length_refusee(self):
        catalogue = {"data": [{"id": "z-ai/glm-5.2", "reasoning": {"mandatory": False}}]}
        with self.assertRaises(ValueError) as ctx:
            self._init(catalogue)
        self.assertIn("context_length", str(ctx.exception))
        self.assertEqual(segmentation.MODEL_TOKEN_LIMITS, self._limits)

    def test_context_length_illisible_refuse(self):
        catalogue = {"data": [{"id": "z-ai/glm-5.2", "context_length": "1M"}]}
        with self.assertRaises(ValueError) as ctx:
            self._init(catalogue)
        self.assertIn("illisible", str(ctx.exception))
        self.assertIn("1M", str(ctx.exception))

    def test_helper_context_length(self):
        lire = openrouter._openrouter_context_length
        self.assertEqual(lire({"context_length": 4095}, "m"), 4095)
        self.assertEqual(lire({"context_length": "32768"}, "m"), 32768)
        for entry in (
            {},
            {"context_length": None},
            {"context_length": 0},
            {"context_length": "1M"},
        ):
            with self.subTest(entry=entry), self.assertRaises(ValueError):
                lire(entry, "m")


if __name__ == "__main__":
    unittest.main()
