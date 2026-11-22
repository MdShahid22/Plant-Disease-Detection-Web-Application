
import tensorflow as tf

dataset_path = "dataset/PlantVillage"

# Image settings
image_size = (128, 128)
batch_size = 32

# Load training dataset
train_dataset = tf.keras.utils.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=image_size,
    batch_size=batch_size
)

# Load validation dataset
validation_dataset = tf.keras.utils.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=image_size,
    batch_size=batch_size
)

# Display dataset information
print("\nDisease Categories:")
print(train_dataset.class_names)

print("\nNumber of Training Batches:")
print(len(train_dataset))

print("\nNumber of Validation Batches:")
print(len(validation_dataset))

# Check image and label shapes
for images, labels in train_dataset.take(1):
    print("\nImage Batch Shape:", images.shape)
    print("Label Batch Shape:", labels.shape)
