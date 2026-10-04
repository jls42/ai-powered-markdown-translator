"""Code inline dans une citation news : protection puis restauration.

Le code est extrait AVANT les citations EN. Un code placé dans le corps d'une
citation partait donc avec elle dans `<NEWSQUOTE id="N"/>` : le modèle ne voyait
jamais son placeholder, et la validation le déclarait « manquant » pour TOUTES
les langues (run news du 2 octobre 2026, disjoncteur déclenché sur
`#INLINECODE19#`). En cible EN, celui de la ligne `> 🇫🇷 _trad_` disparaissait
aussi, puisque la consigne demande au modèle de supprimer cette ligne.

Ces tests rejouent le pipeline sans appel réseau : `_protect_pipeline_inputs`,
une traduction simulée qui obéit aux consignes, puis `_restore_pipeline_outputs`.
"""

from __future__ import annotations

import os
import re
import sys
import unittest
from argparse import Namespace

# Vise `src/`, comme les autres tests : `unittest discover` n'y ajoute rien.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from aipmt import pipeline

SOURCE = """---
title: Test
locale: 'fr'
---

## Claude Code

Un plugin se liste avec `/plugin list`.

> We're adding a new plugin. Enable it with: `/plugin enable you-should-know@builtin`
>
> 🇫🇷 _Nous ajoutons un plugin. Activez-le avec : `/plugin enable you-should-know@builtin`_
> — [@ClaudeDevs sur X](https://x.com/ClaudeDevs/status/1)
"""

QUOTE_LINE = "> We're adding a new plugin. Enable it with: `/plugin enable you-should-know@builtin`"
_ANY_PLACEHOLDER = re.compile(r"#(?:CODEBLOCK|INLINECODE|URL|ANCHOR|REFLABEL)\d+#")


def _args(target_lang):
    return Namespace(news=True, source_lang="fr", target_lang=target_lang)


class TestNewsQuoteCode(unittest.TestCase):
    def _protect(self, target_lang):
        content, state = pipeline._protect_pipeline_inputs(SOURCE, _args(target_lang))
        # Tout placeholder de code à valider doit être visible par le modèle.
        for placeholder in state.inline_placeholders + state.block_placeholders:
            self.assertIn(placeholder, content)
        return content, state

    def test_code_in_quote_body_restored_for_other_target(self):
        content, state = self._protect("de")
        self.assertNotIn("We're adding a new plugin", content)  # citation mise de côté
        translated = content.replace("🇫🇷", "🇩🇪")  # traduction simulée
        out = pipeline._restore_pipeline_outputs(translated, state, _args("de"))
        self.assertIn(QUOTE_LINE, out)
        self.assertIn(
            "> 🇩🇪 _Nous ajoutons un plugin. Activez-le avec : "
            "`/plugin enable you-should-know@builtin`_",
            out,
        )
        self.assertIn("`/plugin list`", out)
        self.assertIsNone(_ANY_PLACEHOLDER.search(out))
        self.assertNotIn("<NEWSQUOTE", out)

    def test_code_in_quote_body_and_flag_line_for_en_target(self):
        content, state = self._protect("en")
        # La ligne de traduction source ne part plus au modèle en cible EN.
        self.assertNotIn("🇫🇷", content)
        out = pipeline._restore_pipeline_outputs(content, state, _args("en"))
        self.assertIn(QUOTE_LINE, out)
        self.assertNotIn("🇫🇷", out)
        self.assertIn("`/plugin list`", out)
        self.assertIsNone(_ANY_PLACEHOLDER.search(out))

    def test_backslashes_in_quoted_code_restored_verbatim(self):
        """La citation est restaurée telle quelle, antislashs compris."""
        source = SOURCE.replace(
            "`/plugin enable you-should-know@builtin`\n>",
            '`printf "a\\nb\\d"`\n>',
            1,
        )
        args = _args("de")
        content, state = pipeline._protect_pipeline_inputs(source, args)
        out = pipeline._restore_pipeline_outputs(content.replace("🇫🇷", "🇩🇪"), state, args)
        self.assertIn('Enable it with: `printf "a\\nb\\d"`', out)

    def test_code_dropped_from_prose_still_fails(self):
        """Témoin : la validation détecte toujours un code supprimé hors citation."""
        content, state = self._protect("de")
        prose_placeholder = state.inline_placeholders[0]
        self.assertEqual(state.inline_codes[0], "`/plugin list`")
        translated = content.replace("🇫🇷", "🇩🇪").replace(prose_placeholder, "")
        with self.assertRaisesRegex(RuntimeError, re.escape(prose_placeholder)):
            pipeline._restore_pipeline_outputs(translated, state, _args("de"))


if __name__ == "__main__":
    unittest.main()
