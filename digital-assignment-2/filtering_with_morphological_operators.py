import cv2
import numpy as np

# Load the image
img = cv2.imread('images/picture1.jpg', 0)

# Define the structuring element for morphological operations
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# Apply morphological closing to remove noise
img_closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Apply morphological gradient to enhance edges
img_gradient = cv2.morphologyEx(img_closed, cv2.MORPH_GRADIENT, kernel)

# Apply adaptive thresholding to obtain a binary image
img_binary = cv2.adaptiveThreshold(img_gradient, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# Display the results
cv2.imshow('Input Image', img)
cv2.imshow('Enhanced Image', img_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
