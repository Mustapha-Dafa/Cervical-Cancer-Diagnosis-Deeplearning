# Project: Cell Classification (CNN Ensemble)

Description
-----------
This repository contains a notebook for training CNN models (DenseNet, Inception, Xception), saved pre-trained models, and a Flask web interface for making predictions via a REST API.

Project Structure
----------------
- [notebook.ipynb](notebook.ipynb) — Main notebook (data preparation, model definitions for `DenseNet`, `Inception`, `Xception`, ensemble functions).
  - Main functions: [`createFrame`](notebook.ipynb), [`DenseNet`](notebook.ipynb), [`Inception`](notebook.ipynb), [`Xception`](notebook.ipynb), [`doFusion`](notebook.ipynb), [`generateRank1`](notebook.ipynb), [`generateRank2`](notebook.ipynb).
- [data](data) — Class folders containing images (subfolders `CROPPED/`).
- [saved_models/densenet_model.h5](saved_models/densenet_model.h5) — Saved DenseNet model.
- [saved_models/inception_model.h5](saved_models/inception_model.h5) — Saved Inception model.
- [saved_models/xception_model.h5](saved_models/xception_model.h5) — Saved Xception model.
- [web interface/app.py](web interface/app.py) — Flask application exposing the `/predict` endpoint.
  - Utility functions: [`read_image`](web interface/app.py), [`predict`](web interface/app.py).
- [web interface/templates/index.html](web interface/templates/index.html) — Upload web page.

Prerequisites
------------
- Python 3.8+
- Packages (examples):
  - tensorflow
  - flask
  - pillow
  - numpy
  - scikit-learn
  - pandas

Installation (example)
---------------------
1. Create and activate virtualenv:
   - python -m venv venv
   - on Windows: venv\Scripts\activate
2. Install dependencies:
   - pip install tensorflow flask pillow numpy scikit-learn pandas

Usage
-----
1. Launch web interface (paths contain spaces, use quotes if needed):
   - python "web interface/app.py"
   - The application loads models from:
     - [saved_models/densenet_model.h5](saved_models/densenet_model.h5)
     - [saved_models/inception_model.h5](saved_models/inception_model.h5)
     - [saved_models/xception_model.h5](saved_models/xception_model.h5)

2. Prediction endpoint:
   - POST /predict
   - Form-data field: `file` (image file)
   - Image is processed by [`read_image`](web interface/app.py) function and predicted by all 3 models then merged via ensemble function (implemented in notebook).
   - Curl example:
     - curl -X POST -F "file=@/path/to/image.jpg" http://127.0.0.1:5000/predict

Retraining and Experiments
-------------------------
- Open [notebook.ipynb](notebook.ipynb) to:
  - Prepare data with [`createFrame`](notebook.ipynb).
  - Train or retrain: [`DenseNet`](notebook.ipynb), [`Inception`](notebook.ipynb), [`Xception`](notebook.ipynb).
  - Generate ensemble and evaluate: [`doFusion`](notebook.ipynb), [`generateRank1`](notebook.ipynb), [`generateRank2`](notebook.ipynb).
- Save trained models in `saved_models/` for Flask API to load them.

Notes
-----
- Classes are determined from folders under [data](data). The `IMG_DIM` variable (128x128) is used for input size.
- The `/predict` endpoint expects pre-processed images according to [`read_image`](web interface/app.py).

Important Files (links)
----------------------
- [notebook.ipynb](notebook.ipynb)
- [data](data)
- [saved_models/densenet_model.h5](saved_models/densenet_model.h5)
- [saved_models/inception_model.h5](saved_models/inception_model.h5)
- [saved_models/xception_model.h5](saved_models/xception_model.h5)
- [web interface/app.py](web interface/app.py)
- [web interface/templates/index.html](web interface/templates/index.html)
