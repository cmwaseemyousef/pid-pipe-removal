import cv2
import numpy as np
import matplotlib.pyplot as plt
from remove_pipes import remove_pipes

def detect_symbols(image_path):
    cleaned_image = remove_pipes(image_path)
    
    _, binary = cv2.threshold(cleaned_image, 150, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    symbol_mask = np.zeros_like(cleaned_image)
    for contour in contours:
        if 100 < cv2.contourArea(contour) < 1000:
            cv2.drawContours(symbol_mask, [contour], -1, 255, thickness=cv2.FILLED)

    plt.figure(figsize=(10, 5))
    plt.imshow(symbol_mask, cmap='gray')
    plt.title("Detected Symbols")
    plt.axis("off")
    plt.show()

    return symbol_mask

if __name__ == "__main__":
    image_path = "C:/Users/user/Desktop/ImageProcessingProject/dataset/images/diagram_0.png"
    symbols = detect_symbols(image_path)
    print("✅ Symbols Extracted Successfully")
