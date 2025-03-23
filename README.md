# 2Methylbutan2ol Serpentes

Une application pour inculquer Python aux minots

## Pour les élèves 🐍

Cette application est ton compagnon pour apprendre Python ! Elle te permet de :

- Écrire du code avec des couleurs qui t'aident à comprendre
- Voir directement si ton code fonctionne
- Avoir des explications simples sur comment coder
- Faire des exercices de plus en plus difficiles
- Trouver des surprises cachées !

Tu trouveras :

- Un menu avec différents niveaux
- Un endroit pour écrire ton code
- Une fenêtre qui montre les résultats
- Des boutons d'aide si tu es bloqué
- Des options pour personnaliser l'application

## Pour les enseignants 👩‍🏫👨‍🏫

### Structure technique

L'application est développée en Python avec une architecture modulaire :

#### Fichiers sources

- [main.py](./main.py): Application principale (GUI, logique, gestion des événements)
- [debogger.py](./debogger.py) : Exécution sécurisée et analyse du code élève

#### Bibliothèques

- Pygame : Interface graphique et événements
- OpenCV : Gestion des animations/GIF
- SQLite3 : Persistance des données
- Numpy : Manipulation des matrices
- ITMGR : Gestion des dépendances
- Pleins d'autres...

### Fonctionnalités pédagogiques

1. Progression structurée
   - Niveaux progressifs
   - Validation des compétences
   - Feedback immédiat

2. Outils d'apprentissage
   - Éditeur avec coloration syntaxique personnalisable
   - Débogueur pédagogique
   - Visualisation des variables
   - Documentation interactive

3. Sécurité
   - Sandbox pour l'exécution du code
   - Gestion des erreurs adaptée
   - Messages d'erreur explicatifs

4. Suivi
   - Base de données SQLite
   - Interface adaptative
   - Statistiques de progression
