import cv2
import numpy as np

# Load the image
img = cv2.imread('images/picture1.jpg')

# Apply Gaussian blur to the image
blurred_img = cv2.GaussianBlur(img, (5, 5), 0)

# Apply unsharp mask to the blurred image
unsharp_mask = cv2.addWeighted(img, 1.5, blurred_img, -0.5, 0)

# Display the results
cv2.imshow('Input Image', img)
cv2.imshow('Enhanced Image', unsharp_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
