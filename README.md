# Jeu du Pendu - Nicolas Allard

Projet réalisé dans le cadre du cours MGA802
19 mai 2026
Nicolas Allard

## Description

Ce programme est un jeu du pendu développé en Python.

Le programme :
- lit une liste de mots à partir d’un fichier texte
- choisit un mot aléatoirement
- demande au joueur de proposer des lettres
- affiche la progression du mot à deviner
- gère les erreurs et les lettres déjà utilisées
- fourni un indice lors de la dernière tentative

N.B. : Les accents ne sont pas considérés dans le jeu. Ainsi, il y a seulement les 26 lettres de l'alphabet qui sont disponibles.

---

## Prérequis

Le projet nécessite :
- la bibliothèque unidecode

Installation de la bibliothèque :

```bash
pip install unidecode
```

---

## Utilisation

1. Ouvrir le projet dans PyCharm ou un terminal
2. Vérifier que le fichier `mots_pendu.txt` est présent
3. Le fichiers `mots_pendu.txt` peut être remplacé par un fichier de même nom comportant des mots différents à la guise de l'utilisateur. Il s'uffit de mettre un mot par ligne dans ce fichier pour assurer la comptabilité.
3. Exécuter le fichier.
4. Suivre les consignes à l'écran

---