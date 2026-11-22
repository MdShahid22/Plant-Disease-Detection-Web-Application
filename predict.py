
import tensorflow as tf
import numpy as np

# Load trained model
model = tf.keras.models.load_model("plant_disease_model.keras")

# Get class names from training dataset
train_dataset = tf.keras.utils.image_dataset_from_directory(
    "dataset/PlantVillage",
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(128, 128),
    batch_size=32
)

class_names = train_dataset.class_names

# Load test image
image_path = "test_images/leaf.jpg"

img = tf.keras.utils.load_img(
    image_path,
    target_size=(128, 128)
)

# Convert image into array
img_array = tf.keras.utils.img_to_array(img)

# Add batch dimension
img_array = tf.expand_dims(img_array, 0)

# Make prediction
predictions = model.predict(img_array)

# Get predicted class
predicted_index = np.argmax(predictions[0])

predicted_class = class_names[predicted_index]

confidence = predictions[0][predicted_index] * 100

# Display result
print("\nPlant Disease Prediction")
print("------------------------")

print("Predicted Disease:", predicted_class)

print("Confidence:", round(float(confidence), 2), "%")
