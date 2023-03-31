import cv2
import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import mean_squared_error as mse

# Load the original image and the enhanced image
img_orig = cv2.imread('original_image.jpg')
img_enhanced = cv2.imread('enhanced_image.jpg')

# Compute the PSNR and MSE of the enhanced image
psnr_val = psnr(img_orig, img_enhanced)
mse_val = mse(img_orig, img_enhanced)

# Print the results
print('PSNR:', psnr_val)
print('MSE:', mse_val)
