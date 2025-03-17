import cv2
import numpy as np
import matplotlib.pyplot as plt
from preprocess import preprocess_image

def remove_pipes(image_path):
    binary = preprocess_image(image_path)

    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 1))
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 50))

    detect_horizontal = cv2.morphologyEx(binary, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
    detect_vertical = cv2.morphologyEx(binary, cv2.MORPH_OPEN, vertical_kernel, iterations=2)

    pipe_mask = cv2.bitwise_or(detect_horizontal, detect_vertical)

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    cleaned_image = cv2.inpaint(image, pipe_mask, inpaintRadius=7, flags=cv2.INPAINT_TELEA)

    plt.figure(figsize=(10, 5))
    plt.imshow(cleaned_image, cmap='gray')
    plt.title("Pipes Removed, Symbols Intact")
    plt.axis("off")
    plt.show()

    return cleaned_image

if __name__ == "__main__":
    image_path = "C:/Users/user/Desktop/ImageProcessingProject/dataset/images/diagram_0.png"
    cleaned = remove_pipes(image_path)
    cv2.imwrite("C:/Users/user/Desktop/ImageProcessingProject/dataset/cleaned_output.png", cleaned)
    print("✅ Pipes Removed Successfully")
