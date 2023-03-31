import cv2
import numpy as np

# Load the image
img = cv2.imread('images/picture1.jpg')

# Convert the image to float32
img_float = np.float32(img)

# Compute the covariance matrix of the image channels
cov_matrix = np.cov(img_float.reshape(-1, 3).T)

# Compute the eigenvectors and eigenvalues of the covariance matrix
eigen_values, eigen_vectors = np.linalg.eig(cov_matrix)

# Compute the decorrelated image
decorrelated_img = np.dot(eigen_vectors.T, img_float.reshape(-1, 3).T).T

# Normalize the decorrelated image
normalized_img = (decorrelated_img - np.min(decorrelated_img)) / (np.max(decorrelated_img) - np.min(decorrelated_img))

# Scale the normalized image to the 0-255 range
scaled_img = (normalized_img * 255).astype(np.uint8)

# Display the results
cv2.imshow('Input Image', img)
cv2.imshow('Enhanced Image', scaled_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
