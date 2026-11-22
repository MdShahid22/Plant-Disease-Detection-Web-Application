
import os
import numpy as np
import tensorflow as tf

from flask import Flask, jsonify, request
from flask_cors import CORS
from PIL import Image

# Initialize Flask
app = Flask(__name__)
CORS(app)

# Get project directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

# Load trained CNN model
MODEL_PATH = os.path.join(
    BASE_DIR,
    "plant_disease_model.keras"
)

print("Loading CNN model...")

model = tf.keras.models.load_model(MODEL_PATH)

print("CNN model loaded successfully!")

# Get class names from dataset folders
DATASET_DIR = os.path.join(
    PROJECT_DIR,
    "dataset",
    "PlantVillage"
)

class_names = sorted([
    folder for folder in os.listdir(DATASET_DIR)
    if os.path.isdir(os.path.join(DATASET_DIR, folder))
])

print("Number of classes:", len(class_names))


# Home API
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Plant Disease Detection API is running!"
    })


# Prediction API
@app.route("/predict", methods=["POST"])
def predict():

    # Check whether image was uploaded
    if "image" not in request.files:
        return jsonify({
            "error": "No image uploaded"
        }), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({
            "error": "No image selected"
        }), 400

    try:
        # Open and resize image
        img = Image.open(file.stream).convert("RGB")
        img = img.resize((128, 128))

        # Convert image to NumPy array
        img_array = np.array(img)

        # Add batch dimension
        img_array = np.expand_dims(img_array, axis=0)

        # Make prediction
        predictions = model.predict(
            img_array,
            verbose=0
        )

        # Get predicted class
        predicted_index = np.argmax(predictions[0])

        predicted_class = class_names[predicted_index]

        confidence = float(
            predictions[0][predicted_index] * 100
        )

        # Return prediction
        return jsonify({
            "predicted_disease": predicted_class,
            "confidence": round(confidence, 2)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


# Start Flask server
if __name__ == "__main__":
    app.run(debug=True)
