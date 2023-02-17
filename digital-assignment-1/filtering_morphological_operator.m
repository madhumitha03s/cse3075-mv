% filtering with morphological operators
clc
clear 
close all

% reading the input image
I = imread('images\picture1.jpg');
subplot(2, 2, 1);
imshow(I);
title('Original Image');

% filtering the noise
se = ones(3,3);
J = imnoise(I,'salt & pepper', 0.2);
subplot(2, 2, 2);
imshow(J);
title('Image with Salt & Pepper Noise');

% morphologically filtered image
subplot(2, 2, 3);
imshow(imclose(imopen(I,se),se));
title('Morphologically Filtered Image');

% metric to compare the results
nI =niqe(I);
nJ = niqe(J);
nIse = niqe(imclose(imopen(I,se),se));
fprintf("Image score for orginal image: %0.2f.\n", nI)
fprintf("Image score for salt and pepper image: %0.2f.\n", nJ)
fprintf("Image score for salt and pepper image: %0.2f.\n", nIse)