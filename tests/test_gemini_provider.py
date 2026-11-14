"""Provider Gemini : réessais sur panne passagère, délai par tentative.

Le SDK `google-genai` ne réessaie rien et n'impose aucun délai par défaut. Le
2026-11-14, sur le niveau gratuit, Gemini Flash répondait « 503 high demand »
ou ne répondait pas du tout : aipmt perdait le fichier au premier 503, et un
appel muet le bloquait sans limite.

Comme pour Mistral, les réessais sont éprouvés sur le VRAI SDK, branché sur un
transport HTTP simulé : vérifier seulement que des options sont passées au
constructeur ne prouverait pas que le SDK en fait quelque chose. Les corps
d'erreur reproduisent ceux que l'API a réellement renvoyés ce soir-là.
"""

from __future__ import annotations

import os
import sys
import unittest
from types import SimpleNamespace
from unittest.mock import patch

import httpx2

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from google.genai import errors as genai_errors

from aipmt.providers import gemini

_FAKE_ENV = {"GOOGLE_API_KEY": "fixture-gemini-key"}  # pragma: allowlist secret

_HIGH_DEMAND = {
    "error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. "
        "Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE",
    }
}

_PREPAY_DEPLETED = {
    "error": {
        "code": 402,
        "message": "Your prepayment credits are depleted.",
        "status": "RESOURCE_EXHAUSTED",
    }
}

_SUCCESS = {
    "candidates": [
        {"content": {"role": "model", "parts": [{"text": "Hello"}]}, "finishReason": "STOP"}
    ],
    "modelVersion": "gemini-3.8-flash",
}

# Ce que le transport simulé rejoue : une réponse, ou une exception à lever.
_Step = httpx2.Response | Exception


def _args() -> SimpleNamespace:
    return SimpleNamespace(model="gemini-3.8-flash", eco=False)


class TestGeminiRetry(unittest.TestCase):
    """Le client construit par le provider réessaie les pannes passagères,
    jamais un refus, et ne reste pas suspendu à un serveur muet."""

    def setUp(self) -> None:
        # Le niveau de raisonnement mémorisé par modèle ne doit pas fuir d'un
        # test à l'autre : chaque test part de la cascade complète.
        gemini._GEMINI_ACCEPTED_THINKING_LEVEL.clear()

    def tearDown(self) -> None:
        gemini._GEMINI_ACCEPTED_THINKING_LEVEL.clear()

    def _client_on(self, steps: list[_Step]):
        """Client du provider, branché sur un transport qui rejoue `steps` ;
        la dernière étape se répète une fois la liste épuisée."""
        requests: list[httpx2.Request] = []

        def handler(request: httpx2.Request) -> httpx2.Response:
            requests.append(request)
            step = steps[min(len(requests), len(steps)) - 1]
            if isinstance(step, Exception):
                raise step
            return step

        http_client = httpx2.Client(transport=httpx2.MockTransport(handler))
        real_client = gemini.genai.Client

        def build(**kwargs):
            options = kwargs.pop("http_options").model_copy(update={"httpx_client": http_client})
            return real_client(http_options=options, **kwargs)

        with (
            patch.dict(os.environ, _FAKE_ENV, clear=True),
            patch("aipmt.providers.gemini.genai.Client", side_effect=build),
        ):
            client = gemini._init_gemini_client(_args())
        return client, requests

    def test_un_503_est_reessaye_apres_une_attente(self) -> None:
        client, requests = self._client_on(
            [httpx2.Response(503, json=_HIGH_DEMAND), httpx2.Response(200, json=_SUCCESS)]
        )
        with patch("tenacity.nap.time.sleep") as sleep:
            text = gemini._call_gemini(client, _args(), "prompt", "segment")
        self.assertEqual(text, "Hello")
        self.assertEqual(len(requests), 2)
        sleep.assert_called_once()
        # 10 s de base, plus une gigue d'au plus une seconde.
        self.assertGreaterEqual(sleep.call_args.args[0], 10.0)
        self.assertLessEqual(sleep.call_args.args[0], 11.0)

    def test_un_delai_depasse_est_reessaye(self) -> None:
        """Le cas du serveur muet : le délai tombe, la tentative suivante passe."""
        client, requests = self._client_on(
            [httpx2.ReadTimeout("timed out"), httpx2.Response(200, json=_SUCCESS)]
        )
        with patch("tenacity.nap.time.sleep"):
            text = gemini._call_gemini(client, _args(), "prompt", "segment")
        self.assertEqual(text, "Hello")
        self.assertEqual(len(requests), 2)

    def test_chaque_requete_porte_le_delai(self) -> None:
        """Sans délai, httpx attend indéfiniment : c'est le défaut du SDK."""
        client, requests = self._client_on([httpx2.Response(200, json=_SUCCESS)])
        gemini._call_gemini(client, _args(), "prompt", "segment")
        timeout = requests[0].extensions["timeout"]
        self.assertEqual(timeout["read"], 300.0)
        self.assertEqual(timeout["connect"], 300.0)
        # Le serveur reçoit le même plafond et abandonne de son côté.
        self.assertEqual(requests[0].headers["X-Server-Timeout"], "300")

    def test_un_402_n_est_pas_reessaye(self) -> None:
        """Un crédit prépayé épuisé ne se règle pas en réessayant."""
        client, requests = self._client_on([httpx2.Response(402, json=_PREPAY_DEPLETED)])
        args = _args()
        with patch("tenacity.nap.time.sleep") as sleep:
            self.assertRaisesRegex(
                genai_errors.ClientError,
                "prepayment",
                gemini._call_gemini,
                client,
                args,
                "prompt",
                "segment",
            )
        self.assertEqual(len(requests), 1)
        sleep.assert_not_called()

    def test_un_503_persistant_finit_par_remonter(self) -> None:
        """Une panne durable échoue en clair au lieu de boucler, après avoir
        attendu assez longtemps pour qu'une fenêtre d'une minute se libère."""
        client, requests = self._client_on([httpx2.Response(503, json=_HIGH_DEMAND)])
        args = _args()
        with patch("tenacity.nap.time.sleep") as sleep:
            self.assertRaisesRegex(
                genai_errors.ServerError,
                "503",
                gemini._call_gemini,
                client,
                args,
                "prompt",
                "segment",
            )
        self.assertEqual(len(requests), 4)
        self.assertEqual(sleep.call_count, 3)
        total = sum(call.args[0] for call in sleep.call_args_list)
        self.assertGreaterEqual(total, 60.0)
        self.assertLessEqual(total, 73.0)


if __name__ == "__main__":
    unittest.main()
