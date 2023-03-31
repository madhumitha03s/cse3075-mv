import cv2
import numpy as np

# Load the image
img = cv2.imread('images/picture1.jpg')

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the image
blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

# Compute the unsharp mask
unsharp_mask = cv2.addWeighted(gray_img, 2, blurred_img, -1, 0)

# Scale the unsharp mask to the 0-255 range
scaled_mask = cv2.normalize(unsharp_mask, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)

# Apply the unsharp mask to the original image
enhanced_img = cv2.addWeighted(img, 1.5, cv2.cvtColor(scaled_mask, cv2.COLOR_GRAY2BGR), -0.5, 0)

# Display the results
cv2.imshow('Input Image', img)
cv2.imshow('Enhanced Image', enhanced_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
