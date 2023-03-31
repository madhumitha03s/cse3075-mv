import cv2
import numpy as np

# Load the original image and the enhanced image
img_orig = cv2.imread('original_image.jpg')
img_enhanced = cv2.imread('enhanced_image.jpg')

# Compute the SSIM of the enhanced image
ssim_val = cv2.SSIM(img_orig, img_enhanced)

# Print the result
print('SSIM:', ssim_val)
