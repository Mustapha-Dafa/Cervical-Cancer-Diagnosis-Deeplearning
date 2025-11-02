# Projet : Classification de cellules (ensemble CNN)

Description
-----------
Ce dépôt contient un notebook d'entraînement de modèles CNN (DenseNet, Inception, Xception), des modèles pré-entraînés sauvegardés et une interface web Flask pour faire des prédictions via une API REST.

Structure du projet
-------------------
- [notebook.ipynb](notebook.ipynb) — Notebook principal (préparation des données, définition des modèles `DenseNet`, `Inception`, `Xception`, fonctions d'ensemble).
  - Fonctions principales : [`createFrame`](notebook.ipynb), [`DenseNet`](notebook.ipynb), [`Inception`](notebook.ipynb), [`Xception`](notebook.ipynb), [`doFusion`](notebook.ipynb), [`generateRank1`](notebook.ipynb), [`generateRank2`](notebook.ipynb).
- [data](data) — Dossiers de classes contenant les images (sous-dossiers `CROPPED/`).
- [saved_models/densenet_model.h5](saved_models/densenet_model.h5) — Modèle DenseNet sauvegardé.
- [saved_models/inception_model.h5](saved_models/inception_model.h5) — Modèle Inception sauvegardé.
- [saved_models/xception_model.h5](saved_models/xception_model.h5) — Modèle Xception sauvegardé.
- [web interface/app.py](web interface/app.py) — Application Flask exposant l'endpoint `/predict`.
  - Fonctions utiles : [`lire_image`](web interface/app.py), [`predict`](web interface/app.py).
- [web interface/templates/index.html](web interface/templates/index.html) — Page web d'upload.

Prérequis
---------
- Python 3.8+
- Packages (exemples) :
  - tensorflow
  - flask
  - pillow
  - numpy
  - scikit-learn
  - pandas

Installation (exemple)
----------------------
1. Créer un virtualenv et l'activer :
   - python -m venv venv
   - sous Windows : venv\Scripts\activate
2. Installer les dépendances :
   - pip install tensorflow flask pillow numpy scikit-learn pandas

Utilisation
----------
1. Lancer l'interface web (les chemins contiennent un espace, utiliser des guillemets si nécessaire) :
   - python "web interface/app.py"
   - L'application charge les modèles depuis :
     - [saved_models/densenet_model.h5](saved_models/densenet_model.h5)
     - [saved_models/inception_model.h5](saved_models/inception_model.h5)
     - [saved_models/xception_model.h5](saved_models/xception_model.h5)

2. Endpoint de prédiction :
   - POST /predict
   - Champ form-data : `file` (fichier image)
   - L'image est traitée par la fonction [`lire_image`](web interface/app.py) et prédite par les 3 modèles puis fusionnée via la fonction d'ensemble (implémentée dans le notebook).
   - Exemple curl :
     - curl -X POST -F "file=@/chemin/vers/image.jpg" http://127.0.0.1:5000/predict

Retraining et expériences
-------------------------
- Ouvrir [notebook.ipynb](notebook.ipynb) pour :
  - Préparer les données avec [`createFrame`](notebook.ipynb).
  - Entraîner ou réentraîner : [`DenseNet`](notebook.ipynb), [`Inception`](notebook.ipynb), [`Xception`](notebook.ipynb).
  - Générer l'ensemble et évaluer : [`doFusion`](notebook.ipynb), [`generateRank1`](notebook.ipynb), [`generateRank2`](notebook.ipynb).
- Sauvegarder les modèles entraînés dans `saved_models/` pour que l'API Flask les charge.

Notes
-----
- Les classes sont déterminées à partir des dossiers sous [data](data). La variable `IMG_DIM` (128x128) est utilisée pour la taille d'entrée.
- L'endpoint `/predict` s'attend à une image pré-traitée conformément à [`lire_image`](web interface/app.py).

Fichiers importants (liens)
---------------------------
- [notebook.ipynb](notebook.ipynb)
- [data](data)
- [saved_models/densenet_model.h5](saved_models/densenet_model.h5)
- [saved_models/inception_model.h5](saved_models/inception_model.h5)
- [saved_models/xception_model.h5](saved_models/xception_model.h5)
- [web interface/app.py](web interface/app.py)
- [web interface/templates/index.html](web interface/templates/index.html)

Licence
-------
(Ajouter ici la licence souhaitée)

Contact
-------
(Omettre ou ajouter informations de contact)