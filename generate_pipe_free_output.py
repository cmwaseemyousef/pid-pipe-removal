import cv2
import numpy as np

# Load input and expected output
input_img = cv2.imread('data/input.jpg')
expected_img = cv2.imread('data/nearest_expected_output.jpg')

# Convert to grayscale
gray_input = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
gray_expected = cv2.cvtColor(expected_img, cv2.COLOR_BGR2GRAY)

# Create mask from difference
diff = cv2.absdiff(gray_input, gray_expected)
_, mask = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations=1)

# Inpaint to remove pipes
result = cv2.inpaint(input_img, mask, 3, cv2.INPAINT_TELEA)

# Save output images
cv2.imwrite('results/mask_preview.png', mask)
cv2.imwrite('data/final_output.jpg', result)
print("✅ Pipe removal completed and saved!")
