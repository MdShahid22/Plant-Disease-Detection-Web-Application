
import tensorflow as tf

# Load the trained model
model = tf.keras.models.load_model("plant_disease_model.keras")

# Load validation dataset
validation_dataset = tf.keras.utils.image_dataset_from_directory(
    "dataset/PlantVillage",
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(128, 128),
    batch_size=32
)

# Evaluate the model
loss, accuracy = model.evaluate(validation_dataset)

print("\nModel Evaluation Results")
print("------------------------")
print("Validation Loss:", loss)
print("Validation Accuracy:", accuracy * 100, "%")
