# YoloRoadSafety

## Description
YoloRoadSafety est un projet utilisant YOLO (You Only Look Once) pour la détection d'objets visant à améliorer la sécurité routière. Ce projet permet de détecter des éléments comme les véhicules, les panneaux de signalisation, et les obstacles, contribuant ainsi à la prévention des accidents.

## Fonctionnalités
- Détection d'objets en temps réel sur des routes.
- Extraction de données pertinentes sur les objets détectés.
- Support pour les images et vidéos.

## Prérequis
- Python 3.x
- OpenCV
- TensorFlow
- NumPy

## Installation
1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/RestumpY/YoloRoadSafety.git
   ```
   
2. Installez les dépendances requises : 
  ```bash
  pip install -r requirements.txt
  ```
## Utilisation
- Exécutez extract.py pour extraire des informations d'images ou de vidéos.
- Utilisez le modèle YOLO pour détecter les objets dans vos fichiers multimédias.

## Structure du Projet
- backend/ : Contient le code backend pour le traitement des données.
- extract.py : Script permettant d'extraire des informations sur les objets détectés.
- Yolo/ : Contient le modèle YOLO et les fichiers associés.


## Contribution
Les contributions sont les bienvenues. Pour cela, veuillez :
- Forker le projet.
- Créer une branche (feature/ma-nouvelle-fonctionnalité).
- Faire une pull request.

## Licence
Ce projet est sous licence MIT. Veuillez consulter le fichier LICENSE pour plus de détails.

## Auteur
Créé par RestumpY.
