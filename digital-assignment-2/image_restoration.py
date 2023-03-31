import numpy as np
import cv2

# Load the degraded image
img = cv2.imread('images/picture1.jpg', 0)

# Define the kernel
kernel_size = 3
kernel = np.ones((kernel_size, kernel_size), np.float32) / kernel_size**2

# Compute the Fourier transform of the degraded image and the kernel
f_img = np.fft.fft2(img)
f_kernel = np.fft.fft2(kernel, s=img.shape)

# Compute the power spectrum of the kernel
power_kernel = np.abs(f_kernel)**2

# Set the value of K
K = 0.01

# Compute the Wiener filter
f_restored = np.conj(f_kernel) / (power_kernel + K)
restored = np.fft.ifft2(f_restored * f_img).real

# Display the results
cv2.imshow('Degraded Image', img)
cv2.imshow('Restored Image', restored.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
