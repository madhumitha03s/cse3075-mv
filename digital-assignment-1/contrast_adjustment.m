% program for contrast adjustment
clc 
clear
close all

% reading the images
A = imread('images\picture1.jpg');

% contrast adjustment
B = A*1.5;

% display input and output images
subplot(1, 2, 1);
imshow(A);
title('Original Image');
subplot(1, 2, 2);
imshow(B);
title('Image after Contrast Adjustment');

% metric to compare the results
nA =niqe(A);
nB = niqe(B);
fprintf("Image score for orginal image: %0.2f.\n", nA)
fprintf("Image score for contrast-adjusted image: %0.2f.\n", nB)