"""Le comparateur de structure doit MORDRE, et ne pas crier à tort.

Il a produit les tableaux de modèles conseillés du README : un faux positif y
disqualifiait un modèle correct, un faux négatif y publiait un modèle qui perd
de l'information. Les deux corrections d'écritures non latines qu'il porte
viennent d'un tel faux positif, mesuré — sans elles, deux modèles auraient été
publiés à onze langues sur quatorze au lieu de treize et douze.
"""

from __future__ import annotations

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from compare_structure import corps_sans_note, ecarts, urls

SOURCE = """## Une section

Un paragraphe avec un [lien](https://example.com/a) et du `code en ligne`.

```python
print("bloc")
```

> Une citation
> — attribution

| a | b |
| - | - |
| 1 | 2 |

Du **gras** ici.
"""


class LeComparateurNeCriePasATort(unittest.TestCase):
    def test_une_traduction_fidele_ne_signale_rien(self):
        traduit = SOURCE.replace("Une section", "A section").replace("Un paragraphe", "A paragraph")
        self.assertEqual(ecarts(SOURCE, traduit), [])

    def test_une_url_suivie_de_ponctuation_pleine_chasse_reste_la_meme(self):
        """Le faux positif qui a motivé l'outil : en chinois, l'URL est suivie
        de « ）、 » SANS espace, et une regex qui n'exclut que les blancs
        avalait la phrase entière."""
        latin = "Voir https://example.com/a (ici)."
        chinois = "参见 https://example.com/a （这里）、然后"
        self.assertEqual(urls(latin), urls(chinois))

    def test_une_citation_plus_courte_nest_pas_une_citation_perdue(self):
        """Cinq lignes en français tiennent en trois en chinois : on compte les
        BLOCS, pas les lignes."""
        court = SOURCE.replace("> Une citation\n> — attribution", "> 引用\n> — 归属")
        self.assertEqual(ecarts(SOURCE, court), [])

    def test_la_note_de_traduction_finale_est_retiree_avant_de_compter(self):
        avec_note = SOURCE + "\n\n**Traduit par un modèle.**\n"
        self.assertEqual(ecarts(SOURCE, corps_sans_note(avec_note)), [])


class LeComparateurMord(unittest.TestCase):
    def test_une_url_perdue_est_signalee(self):
        sans_url = SOURCE.replace("https://example.com/a", "")
        trouves = ecarts(SOURCE, sans_url)
        self.assertTrue(any("URL perdue" in e for e in trouves), trouves)

    def test_un_bloc_de_code_perdu_est_signale(self):
        sans_bloc = SOURCE.replace('```python\nprint("bloc")\n```\n', "")
        self.assertTrue(any(e.startswith("fences") for e in ecarts(SOURCE, sans_bloc)))

    def test_une_section_perdue_est_signalee(self):
        self.assertTrue(
            any(e.startswith("sections") for e in ecarts(SOURCE, SOURCE.replace("## ", "")))
        )

    def test_un_code_en_ligne_perdu_est_signale(self):
        sans_code = SOURCE.replace("`code en ligne`", "code en ligne")
        self.assertTrue(any(e.startswith("code") for e in ecarts(SOURCE, sans_code)))

    def test_une_ligne_de_tableau_perdue_est_signalee(self):
        sans_ligne = SOURCE.replace("| 1 | 2 |\n", "")
        self.assertTrue(any(e.startswith("tableau") for e in ecarts(SOURCE, sans_ligne)))

    def test_une_citation_entierement_perdue_est_signalee(self):
        sans_citation = SOURCE.replace("> Une citation\n> — attribution\n", "")
        self.assertTrue(any(e.startswith("citations") for e in ecarts(SOURCE, sans_citation)))

    def test_un_attendu_surcharge_la_reference(self):
        """Mode news vers l'anglais : la ligne de drapeau disparaît par contrat,
        son absence n'est pas une perte."""
        sans_citation = SOURCE.replace("> Une citation\n> — attribution\n", "")
        self.assertEqual(ecarts(SOURCE, sans_citation, attendus={"citations": 0}), [])


if __name__ == "__main__":
    unittest.main()
