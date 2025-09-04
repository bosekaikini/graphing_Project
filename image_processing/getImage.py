from PIL import Image
import cv2
#Goal: Take an image and convert it to a usable matrix

image_path="line_test.jpg"
try:
    img = Image.open(image_path)
    print(f"Image loaded successfully: {img.format}, {img.mode}, {img.size}")
except Exception as e:
    print(f"An error occurred: {e}")

image_matrix=cv2.imread(image_path)