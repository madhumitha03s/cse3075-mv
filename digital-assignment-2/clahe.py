import cv2
import numpy as np

# Load the image
img = cv2.imread('images/picture1.jpg')

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Contrast-Limited Adaptive Histogram Equalization (CLAHE)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
clahe_img = clahe.apply(gray_img)

# Display the results
cv2.imshow('Input Image', img)
cv2.imshow('Enhanced Image', clahe_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
