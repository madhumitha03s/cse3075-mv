import cv2
import numpy as np

# Load the image
img = cv2.imread('images/picture1.jpg', 0)

# Define the intensity levels
low_intensity = 100
high_intensity = 200

# Apply image level slicing
img_sliced = np.zeros_like(img)
img_sliced[(img >= low_intensity) & (img <= high_intensity)] = 255

# Display the results
cv2.imshow('Input Image', img)
cv2.imshow('Sliced Image', img_sliced)
cv2.waitKey(0)
cv2.destroyAllWindows()
