
import os
import numpy as np
from PIL import Image

# Dataset path
dataset_path = "dataset/PlantVillage"

# Select category
category = "Tomato_Early_blight"

category_path = os.path.join(dataset_path, category)

# Get image files
images = [
    img for img in os.listdir(category_path)
    if img.lower().endswith((".jpg", ".jpeg", ".png"))
]

# Select one image
image_path = os.path.join(category_path, images[0])

# Open image
image = Image.open(image_path)

print("Original Image Size:", image.size)

# Resize image
image = image.resize((128, 128))

print("Resized Image Size:", image.size)

# Convert image into NumPy array
image_array = np.array(image)

print("Array Shape:", image_array.shape)

# Normalize pixel values
image_array = image_array / 255.0

print("Minimum Pixel Value:", image_array.min())
print("Maximum Pixel Value:", image_array.max())
