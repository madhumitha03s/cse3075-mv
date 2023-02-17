% image enhancement by histogram equalization
clc
clear
close all
I = imread('images\picture1.jpg');
H = histeq(I);

% reading the input image
subplot(2,2,1);
imshow(I); 
title('Original Image');

% image after histogram equalization
subplot(2,2,2); 
imshow(H);
title('Histogram Equalized Image');

% histogram of the original image
subplot(2,2,3);
imhist(I);
title('Histogram of Original Image');

% histogram of the equalized image
subplot(2,2,4);
imhist(H);
title('Histogram of Equalized Image');

% metric to compare the results
nI =niqe(I);
nH = niqe(H);
fprintf("Image score for orginal image: %0.2f.\n", nI)
fprintf("Image score for histogram-equalised image: %0.2f.\n", nH)