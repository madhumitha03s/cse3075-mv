% unsharp mask filtering
clc
clear
close all

% reading the input image
I = imread('images\picture1.jpg');
subplot(1, 2, 1);
imshow(I);
title('Original Image');

% image after sharpening
S = imsharpen(I, 'amount', 3);
subplot(1, 2, 2);
imshow(S);
title('Sharpened Image');

% metric to compare the results
nI =niqe(I);
nS = niqe(S);
fprintf("Image score for orginal image: %0.2f.\n", nI)
fprintf("Image score for sharpened image: %0.2f.\n", nS)