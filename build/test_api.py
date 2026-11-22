
import requests
import os

# Image path
image_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "test_images",
    "leaf.jpg"
)

# Flask API URL
url = "http://127.0.0.1:5000/predict"

# Send image to Flask
with open(image_path, "rb") as image:
    files = {
        "image": image
    }

    response = requests.post(url, files=files)

# Display result
print("API Status Code:", response.status_code)
print("Prediction Result:")
print(response.json())
