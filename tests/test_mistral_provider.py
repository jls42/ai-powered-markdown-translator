"""Provider Mistral : réessais sur dépassement de débit, blocs de raisonnement.

Les réessais sont éprouvés sur le VRAI SDK `mistralai`, branché sur un
transport HTTP simulé : vérifier seulement qu'un `retry_config` est passé au
constructeur ne prouverait pas que le SDK en fait quelque chose. Le 429 simulé
reproduit celui que l'API renvoie réellement — sans `Retry-After` (mesuré le
2026-09-17).
"""

from __future__ import annotations

import os
import sys
import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import httpx

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from mistralai.client.errors import SDKError
from mistralai.client.models import TextChunk, ThinkChunk

from aipmt.providers import mistral

_FAKE_ENV = {"MISTRAL_API_KEY": "fixture-mistral-key"}  # pragma: allowlist secret

_RATE_LIMITED = {
    "object": "error",
    "message": "Rate limit exceeded",
    "type": "rate_limited",
    "param": None,
    "code": "1300",
}


def _completion(content: str = "Hello") -> dict:
    return {
        "id": "cmpl-test",
        "object": "chat.completion",
        "model": "mistral-small-2603",
        "created": 0,
        "usage": {"prompt_tokens": 3, "completion_tokens": 1, "total_tokens": 4},
        "choices": [
            {
                "index": 0,
                "finish_reason": "stop",
                "message": {"role": "assistant", "content": content},
            }
        ],
    }


def _args(model: str = "mistral-small-2603") -> SimpleNamespace:
    return SimpleNamespace(model=model, eco=False)


class TestMistralText(unittest.TestCase):
    def test_une_chaine_passe_telle_quelle(self) -> None:
        self.assertEqual(mistral._mistral_text("  Bonjour  ", "m"), "  Bonjour  ")

    def test_un_contenu_absent_est_une_erreur_explicite(self) -> None:
        with self.assertRaisesRegex(RuntimeError, r"Mistral returned no content \(model=m\)"):
            mistral._mistral_text(None, "m")

    def test_les_blocs_de_raisonnement_sont_ecartes(self) -> None:
        content = [
            ThinkChunk(thinking=[TextChunk(text="Je réfléchis…")]),
            TextChunk(text="The cat sleeps."),
        ]
        self.assertEqual(mistral._mistral_text(content, "m"), "The cat sleeps.")

    def test_un_bloc_de_raisonnement_porteur_de_texte_est_ecarte_aussi(self) -> None:
        # L'exclusion se fait sur le TYPE : un bloc `thinking` qui exposerait un
        # jour un `text` (résumé de raisonnement) ne doit pas entrer dans la
        # traduction.
        content = [
            SimpleNamespace(type="thinking", text="Résumé du raisonnement"),
            TextChunk(text="The cat sleeps."),
        ]
        self.assertEqual(mistral._mistral_text(content, "m"), "The cat sleeps.")

    def test_plusieurs_blocs_de_texte_sont_colles_sans_separateur(self) -> None:
        content = [TextChunk(text="## Titre\n\nDébut "), TextChunk(text="et fin.")]
        self.assertEqual(mistral._mistral_text(content, "m"), "## Titre\n\nDébut et fin.")

    def test_un_bloc_inconnu_porteur_de_texte_est_garde(self) -> None:
        # Liste NÉGATIVE, comme pour Claude : un type nouveau mais textuel reste
        # exploitable au lieu de faire échouer la traduction.
        content = [SimpleNamespace(type="nouveau", text="Texte")]
        self.assertEqual(mistral._mistral_text(content, "m"), "Texte")

    def test_rien_que_du_raisonnement_est_une_erreur_qui_nomme_les_blocs(self) -> None:
        content = [ThinkChunk(thinking=[TextChunk(text="…")])]
        with self.assertRaisesRegex(RuntimeError, r"aucun bloc de texte.*thinking"):
            mistral._mistral_text(content, "m")

    def test_call_mistral_rend_le_texte_d_une_reponse_en_blocs(self) -> None:
        client = MagicMock()
        client.chat.complete.return_value = MagicMock(
            choices=[
                MagicMock(
                    finish_reason="stop",
                    message=MagicMock(
                        content=[
                            ThinkChunk(thinking=[TextChunk(text="…")]),
                            TextChunk(text="  Traduit  "),
                        ]
                    ),
                )
            ]
        )
        self.assertEqual(mistral._call_mistral(client, _args(), "prompt", "segment"), "Traduit")


class TestMistralRetry(unittest.TestCase):
    """Le client construit par le provider réessaie sur 429, pas sur 400."""

    def _client_on(self, responses: list[httpx.Response]):
        """Client du provider, branché sur un transport qui rejoue `responses`."""
        requests: list[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return responses[min(len(requests), len(responses)) - 1]

        http_client = httpx.Client(transport=httpx.MockTransport(handler))
        real_mistral = mistral.Mistral
        with (
            patch.dict(os.environ, _FAKE_ENV, clear=True),
            patch(
                "aipmt.providers.mistral.Mistral",
                side_effect=lambda **kwargs: real_mistral(client=http_client, **kwargs),
            ),
        ):
            client = mistral._init_mistral_client(_args())
        return client, requests

    def test_un_429_sans_retry_after_est_reessaye_apres_une_attente(self) -> None:
        client, requests = self._client_on(
            [httpx.Response(429, json=_RATE_LIMITED), httpx.Response(200, json=_completion())]
        )
        with patch("mistralai.client.utils.retries.time.sleep") as sleep:
            text = mistral._call_mistral(client, _args(), "prompt", "segment")
        self.assertEqual(text, "Hello")
        self.assertEqual(len(requests), 2)
        sleep.assert_called_once()
        # 2 s de base, plus une gigue d'au plus une seconde.
        self.assertGreaterEqual(sleep.call_args.args[0], 2.0)
        self.assertLessEqual(sleep.call_args.args[0], 3.0)

    def test_un_400_n_est_pas_reessaye(self) -> None:
        client, requests = self._client_on(
            [httpx.Response(400, json={"object": "error", "message": "bad request"})]
        )
        args = _args()
        with patch("mistralai.client.utils.retries.time.sleep") as sleep:
            self.assertRaises(SDKError, mistral._call_mistral, client, args, "prompt", "segment")
        self.assertEqual(len(requests), 1)
        sleep.assert_not_called()

    def test_un_429_persistant_finit_par_remonter(self) -> None:
        """Un compte durablement bridé échoue en clair au lieu de boucler."""
        client, requests = self._client_on([httpx.Response(429, json=_RATE_LIMITED)])
        clock = iter(range(0, 10_000, 100))  # chaque lecture de l'horloge avance de 100 s
        args = _args()
        with (
            patch("mistralai.client.utils.retries.time.sleep"),
            patch("mistralai.client.utils.retries.time.time", side_effect=lambda: next(clock)),
        ):
            self.assertRaisesRegex(
                SDKError, "429", mistral._call_mistral, client, args, "prompt", "segment"
            )
        self.assertLessEqual(len(requests), 5)

    def test_le_backoff_couvre_une_fenetre_d_une_minute(self) -> None:
        """Les plafonds Mistral sont PAR MINUTE : des attentes cumulées plus
        courtes abandonneraient avant que la fenêtre ne se libère."""
        backoff = mistral.MISTRAL_RETRY_CONFIG.backoff
        self.assertEqual(mistral.MISTRAL_RETRY_CONFIG.strategy, "backoff")
        self.assertTrue(mistral.MISTRAL_RETRY_CONFIG.retry_connection_errors)
        # Attentes cumulées des réessais qui partent avant l'abandon, gigue exclue.
        total, retries = 0.0, 0
        while True:
            wait = min(
                backoff.initial_interval / 1000 * backoff.exponent**retries,
                backoff.max_interval / 1000,
            )
            if total + wait > backoff.max_elapsed_time / 1000:
                break
            total += wait
            retries += 1
        self.assertGreaterEqual(total, 60)
        self.assertGreaterEqual(backoff.max_interval, 60_000)


if __name__ == "__main__":
    unittest.main()
