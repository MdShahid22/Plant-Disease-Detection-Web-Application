import tensorflow as tf
from tensorflow.keras import layers, models

# Create CNN model
model = models.Sequential([

    # First convolution block
    layers.Input(shape=(128, 128, 3)),
    layers.Rescaling(1./255),

    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Second convolution block
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Third convolution block
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Classification layers
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),

    # Output layer: 15 disease categories
    layers.Dense(15, activation='softmax')
])

# Display model architecture
model.summary()

# Compile the CNN model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Load training dataset
train_dataset = tf.keras.utils.image_dataset_from_directory(
    "dataset/PlantVillage",
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(128, 128),
    batch_size=32
)

# Load validation dataset
validation_dataset = tf.keras.utils.image_dataset_from_directory(
    "dataset/PlantVillage",
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(128, 128),
    batch_size=32
)

print("\nClass Names:", train_dataset.class_names)
print("Number of Classes:", len(train_dataset.class_names))

print("\nModel compiled successfully!")

# Train the CNN model
history = model.fit(
    train_dataset,
    validation_data=validation_dataset,
    epochs=10
)

# Save the trained model
model.save("plant_disease_model.keras")

print("Model saved successfully!")

# Evaluate the model
loss, accuracy = model.evaluate(validation_dataset)

print("\nModel Evaluation:")
print("Validation Loss:", loss)
print("Validation Accuracy:", accuracy * 100, "%")