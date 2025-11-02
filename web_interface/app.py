from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import tensorflow as tf
from PIL import Image
import io
import numpy as np
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))                  
project_root = os.path.abspath(os.path.join(current_dir, '..'))    
sys.path.append(project_root) 

from src.ensemble import *


app = Flask(__name__)
CORS(app)

# Charger le modèle entraîné
model_dens = tf.keras.models.load_model('saved_models/densenet_model.h5')
model_inception = tf.keras.models.load_model('saved_models/inception_model.h5')
model_xception = tf.keras.models.load_model('saved_models/xception_model.h5')

def lire_image(fichier) -> np.ndarray:
    image = Image.open(io.BytesIO(fichier))
    image = image.resize((128, 128))  # Ajustez la taille en fonction de l'entrée de votre modèle
    image = np.array(image).astype('float32') / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    fichier = request.files['file']
    image = lire_image(fichier.read())
    #prediction = modele.predict(image)
    res1 = model_dens.predict(image)
    res2 = model_inception.predict(image) 
    res3 = model_xception.predict(image)
    predictedClass = doFusion_single(res1,res2,res3,class_no=5)
    resultat = "Cancéreux" if (predictedClass == 1 or predictedClass == 0) else "Non cancéreux"
    #resultat = "Cancéreux" if (np.argmax(prediction) == 1 or np.argmax(prediction) == 0) else "Non cancéreux"
    return jsonify({"prediction": resultat})

if __name__ == '__main__':
    app.run(debug=True)
