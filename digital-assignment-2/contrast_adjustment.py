import cv2

# Load the image
img = cv2.imread('images/picture1.jpg', 0)

# Define the parameters for contrast adjustment
alpha = 1.5 # Contrast control (1.0-3.0)
beta = 0 # Brightness control (0-100)

# Apply contrast adjustment
img_contrast = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

# Display the results
cv2.imshow('Input Image', img)
cv2.imshow('Contrast Adjusted Image', img_contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()
