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

import contextlib
import io
import logging
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
_BOTH_KEYS_ENV = {**_FAKE_ENV, "GEMINI_API_KEY": "fixture-other-key"}  # pragma: allowlist secret

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


class _GeminiClientCase(unittest.TestCase):
    """Client du vrai SDK sur transport simulé, état global remis à neuf."""

    def setUp(self) -> None:
        # Le niveau de raisonnement mémorisé par modèle ne doit pas fuir d'un
        # test à l'autre : chaque test part de la cascade complète.
        gemini._GEMINI_ACCEPTED_THINKING_LEVEL.clear()
        # Le relais des relances vit sur un journal global du SDK, qu'un autre
        # module de tests a pu équiper : chaque test part d'un journal nu.
        self._sdk_logger = logging.getLogger(gemini._GEMINI_SDK_LOGGER)
        self._saved_logger = (self._sdk_logger.level, list(self._sdk_logger.filters))
        self._sdk_logger.filters[:] = [
            f for f in self._sdk_logger.filters if not isinstance(f, gemini._GeminiRetryNotice)
        ]
        self._sdk_logger.setLevel(logging.NOTSET)

    def tearDown(self) -> None:
        gemini._GEMINI_ACCEPTED_THINKING_LEVEL.clear()
        level, filters = self._saved_logger
        self._sdk_logger.setLevel(level)
        self._sdk_logger.filters[:] = filters

    def _client_on(self, steps: list[_Step], env: dict[str, str] | None = None):
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
            patch.dict(os.environ, env or _FAKE_ENV, clear=True),
            patch("aipmt.providers.gemini.genai.Client", side_effect=build),
        ):
            client = gemini._init_gemini_client(_args())
        return client, requests


class TestGeminiRetry(_GeminiClientCase):
    """Le client construit par le provider réessaie les pannes passagères,
    jamais un refus, et ne reste pas suspendu à un serveur muet."""

    def test_un_503_est_reessaye_apres_une_attente(self) -> None:
        client, requests = self._client_on(
            [httpx2.Response(503, json=_HIGH_DEMAND), httpx2.Response(200, json=_SUCCESS)]
        )
        stderr = io.StringIO()
        with patch("tenacity.nap.time.sleep") as sleep, contextlib.redirect_stderr(stderr):
            text = gemini._call_gemini(client, _args(), "prompt", "segment")
        self.assertEqual(text, "Hello")
        self.assertEqual(len(requests), 2)
        sleep.assert_called_once()
        # 10 s de base, plus une gigue d'au plus une seconde.
        self.assertGreaterEqual(sleep.call_args.args[0], 10.0)
        self.assertLessEqual(sleep.call_args.args[0], 11.0)
        # La relance se voit : statut d'erreur et attente, sans le corps JSON.
        self.assertRegex(
            stderr.getvalue(),
            r"^⚠ Gemini : ServerError: 503 UNAVAILABLE — nouvelle tentative dans 1[01] s\n$",
        )

    def test_un_delai_depasse_est_reessaye(self) -> None:
        """Le cas du serveur muet : le délai tombe, la tentative suivante passe."""
        client, requests = self._client_on(
            [httpx2.ReadTimeout("timed out"), httpx2.Response(200, json=_SUCCESS)]
        )
        with patch("tenacity.nap.time.sleep"), contextlib.redirect_stderr(io.StringIO()):
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
        stderr = io.StringIO()
        with patch("tenacity.nap.time.sleep") as sleep, contextlib.redirect_stderr(stderr):
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
        # Une ligne par attente ; la dernière tentative échoue sans en annoncer.
        self.assertEqual(stderr.getvalue().count("nouvelle tentative"), 3)

    def test_un_delai_depasse_est_annonce(self) -> None:
        client, _ = self._client_on(
            [httpx2.ReadTimeout("timed out"), httpx2.Response(200, json=_SUCCESS)]
        )
        stderr = io.StringIO()
        with patch("tenacity.nap.time.sleep"), contextlib.redirect_stderr(stderr):
            gemini._call_gemini(client, _args(), "prompt", "segment")
        self.assertIn("⚠ Gemini : ReadTimeout: timed out — nouvelle tentative", stderr.getvalue())

    def test_un_second_client_ne_double_pas_l_avis(self) -> None:
        self._client_on([httpx2.Response(200, json=_SUCCESS)])
        client, _ = self._client_on(
            [httpx2.Response(503, json=_HIGH_DEMAND), httpx2.Response(200, json=_SUCCESS)]
        )
        notices = [f for f in self._sdk_logger.filters if isinstance(f, gemini._GeminiRetryNotice)]
        self.assertEqual(len(notices), 1)
        stderr = io.StringIO()
        with patch("tenacity.nap.time.sleep"), contextlib.redirect_stderr(stderr):
            gemini._call_gemini(client, _args(), "prompt", "segment")
        self.assertEqual(stderr.getvalue().count("nouvelle tentative"), 1)


class TestGeminiRetryNoticeLeavesSdkLogAlone(_GeminiClientCase):
    """Le relais n'ajoute que l'avis de relance : ce que le journal du SDK
    affichait avant s'affiche toujours, ce qu'il taisait reste tu."""

    def test_l_avertissement_des_deux_cles_reste_visible(self) -> None:
        """Avertissement réel du SDK, émis à la construction du client. Un
        handler posé sur ce journal l'aurait fait disparaître."""
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            self._client_on(
                [httpx2.Response(200, json=_SUCCESS)],
                env=_BOTH_KEYS_ENV,
            )
        self.assertIn("Both GOOGLE_API_KEY and GEMINI_API_KEY are set", stderr.getvalue())

    def test_le_reste_du_niveau_info_reste_muet(self) -> None:
        self._client_on([httpx2.Response(200, json=_SUCCESS)])
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            self._sdk_logger.info("The user provided Vertex AI API key will take precedence.")
        self.assertEqual(stderr.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
