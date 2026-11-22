import tensorflow as tf

dataset_path = "dataset/PlantVillage"

# Load training images
train_dataset = tf.keras.utils.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(128, 128),
    batch_size=32
)

# Load validation images
validation_dataset = tf.keras.utils.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(128, 128),
    batch_size=32
)

print("Class Names:", train_dataset.class_names)
print("Training Dataset:", train_dataset)
print("Validation Dataset:", validation_dataset)

print("\nNumber of Training Batches:", len(train_dataset))
print("Number of Validation Batches:", len(validation_dataset))

# Display one batch of images
for images, labels in train_dataset.take(1):
    print("\nImage Batch Shape:", images.shape)
    print("Label Batch Shape:", labels.shape)