import cv2

# Load the image
img = cv2.imread('images/picture1.jpg', 0)

# Apply histogram equalization
img_eq = cv2.equalizeHist(img)

# Display the results
cv2.imshow('Input Image', img)
cv2.imshow('Enhanced Image', img_eq)
cv2.waitKey(0)
cv2.destroyAllWindows()
