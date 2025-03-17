import cv2
import numpy as np
import matplotlib.pyplot as plt

def preprocess_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, binary = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)  # Convert to binary
    edges = cv2.Canny(binary, 50, 150)  # Detect edges

    plt.figure(figsize=(10, 5))
    plt.imshow(edges, cmap='gray')
    plt.title("Edge Detection for Technical Diagram")
    plt.axis("off")
    plt.show()
    
    return binary

if __name__ == "__main__":
    image_path = "C:/Users/user/Desktop/ImageProcessingProject/dataset/images/diagram_0.png"
    binary = preprocess_image(image_path)
    print("✅ Image Preprocessing Complete")
