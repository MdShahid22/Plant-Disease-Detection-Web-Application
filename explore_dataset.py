
import os

dataset_path = "dataset/PlantVillage"

categories = []

for category in os.listdir(dataset_path):

    category_path = os.path.join(dataset_path, category)

    if os.path.isdir(category_path):

        images = [
            img for img in os.listdir(category_path)
            if img.lower().endswith((".jpg", ".jpeg", ".png"))
        ]

        if len(images) > 0:
            categories.append((category, len(images)))

print("Total Categories:", len(categories))
print("\nDisease Categories and Image Counts:\n")

total_images = 0

for category, count in categories:
    print(category, ":", count, "images")
    total_images += count

print("\nTotal Images:", total_images)
