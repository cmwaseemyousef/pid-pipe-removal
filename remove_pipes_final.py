import cv2

# Load original image and mask
img = cv2.imread('input.jpg')
mask = cv2.imread('pipe_mask.png', 0)

# Inpaint pipes using the mask
result = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

# Save output
cv2.imwrite('final_output.png', result)
