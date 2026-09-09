#!/usr/bin/env python3
"""Compare les invariants de STRUCTURE de deux Markdown : source et traduction.

Le README décrit ce protocole comme la bonne façon de juger un modèle — « nombre
de sections, de liens, d'URL distinctes, de blocs de code, de codes en ligne, de
lignes de tableau » — sans livrer l'outil. Le voici : c'est celui qui a produit
les tableaux de modèles conseillés, et celui que les contrôles de paquet
appellent après une traduction réelle.

Ce qu'il ne fait PAS : juger la qualité de la langue. Une traduction fidèle et
une paraphrase creuse comptent pareil. Il attrape ce qu'un modèle perd en
silence — une URL, un bloc de code, une ligne de tableau — pas ce qu'il dit mal.

Deux artefacts mesurés sur les écritures non latines sont neutralisés, faute de
quoi l'outil signalait des écarts qui n'existaient pas :

- une URL suivie d'une parenthèse PLEINE CHASSE `）` n'est pas coupée par une
  regex qui s'arrête à `)` : la chaîne extraite diffère alors que l'URL est
  identique. Toute ponctuation finale est donc rognée, quelle que soit sa
  largeur ;
- une citation de cinq lignes en français tient en trois lignes en chinois : on
  compte les BLOCS de citation, pas les lignes.

Sans ces deux corrections, Gemini et Codex auraient été publiés à onze langues
sur quatorze au lieu de treize et douze.

usage: compare_structure.py SOURCE.md TRADUCTION.md
       exit 0 si la structure est identique, 1 sinon.
"""

import re
import sys

# Ponctuation qui peut suivre une URL sans espace, demi-chasse et pleine chasse.
_PONCTUATION_FINALE = "`)》）】」』,.;:!?、。，；：！？…"
# Une URL s'arrête au premier délimiteur, y compris pleine chasse : en chinois
# elle est suivie de « `）、 » SANS espace, et une regex qui n'exclut que les
# blancs avalerait la phrase entière.
_URL_REGEX = re.compile(r"https?://[^\s<>\"'`()\[\]（）【】「」『』，。、；：！？]+")

# La note de traduction ajoutée en fin de document n'existe pas dans la source :
# la retirer avant de compter, sinon chaque comparaison signale un faux écart.
_NOTE_SEPARATEUR = "\n\n**"


def urls(texte):
    """URL distinctes du document, ponctuation finale rognée."""
    return {u.rstrip(_PONCTUATION_FINALE) for u in _URL_REGEX.findall(texte)}


def compte(texte):
    """Les invariants comptés. Chacun est un élément qu'une traduction peut
    perdre sans que rien d'autre ne le signale."""
    return {
        "sections": len(re.findall(r"^## ", texte, re.M)),
        "titres": len(re.findall(r"^### ", texte, re.M)),
        "liens": len(re.findall(r"\]\(https?://", texte)),
        "urls": len(urls(texte)),
        # `>` SEUL sépare les deux moitiés d'une citation du mode news : exiger
        # « > » suivi d'un espace coupait chaque citation en deux blocs, et la
        # cible anglaise — où la ligne de drapeau disparaît — semblait alors en
        # perdre la moitié.
        "citations": len(re.findall(r"(?:^|\n)(?:>[^\n]*\n?)+", texte)),
        "fences": len(re.findall(r"^```", texte, re.M)),
        "code": len(re.findall(r"`[^`\n]+`", texte)),
        "gras": texte.count("**") // 2,
        "tableau": len(re.findall(r"^\|", texte, re.M)),
    }


def corps_sans_note(texte):
    """Le document sans sa note de traduction finale, s'il en porte une."""
    if texte.rstrip().endswith("**"):
        return texte.rsplit(_NOTE_SEPARATEUR, 1)[0]
    return texte


def ecarts(source, traduction, attendus=None):
    """Écarts de structure, du plus parlant au moins. `attendus` surcharge une
    valeur de référence — en mode news vers l'anglais, les lignes de drapeau
    disparaissent par contrat, et leur absence n'est pas une perte."""
    reference, mesure = compte(source), compte(traduction)
    if attendus:
        reference = {**reference, **attendus}
    trouves = [
        f"{cle} {mesure[cle]}≠{reference[cle]}"
        for cle in reference
        if mesure[cle] != reference[cle]
    ]
    perdues = urls(source) - urls(traduction)
    if perdues:
        trouves.append(f"{len(perdues)} URL perdue(s) : {', '.join(sorted(perdues)[:3])}")
    return trouves


def main(argv):
    if len(argv) != 3:
        print(__doc__.strip().splitlines()[-2].strip(), file=sys.stderr)
        return 2
    with open(argv[1], encoding="utf-8") as f:
        source = f.read()
    with open(argv[2], encoding="utf-8") as f:
        traduction = f.read()
    trouves = ecarts(source, corps_sans_note(traduction))
    print("; ".join(trouves) if trouves else "structure identique")
    return 1 if trouves else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
