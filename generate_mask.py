import cv2
import numpy as np

# Load input and expected output
input_img = cv2.imread('input.jpg')
expected_img = cv2.imread('nearest_expected_output.jpg')

# Convert to grayscale
gray_input = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
gray_expected = cv2.cvtColor(expected_img, cv2.COLOR_BGR2GRAY)

# Create binary mask of pipe differences
mask = cv2.absdiff(gray_input, gray_expected)
_, mask = cv2.threshold(mask, 30, 255, cv2.THRESH_BINARY)
mask = cv2.dilate(mask, np.ones((3,3), np.uint8), iterations=1)

# Save mask
cv2.imwrite('pipe_mask.png', mask)
