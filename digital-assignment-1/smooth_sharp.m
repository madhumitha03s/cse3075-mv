% program for image smoothing and sharpening
clc
clear
close all

% reading the input image
I = imread('images/picture1.jpg');
subplot(2, 2, 1);
imshow(I);
title('Original Image');

% applying smoothing technique
Iblur1 = imgaussfilt(I,2);
Iblur2 = imgaussfilt(I,8);

% diplay plot of smoothened images
subplot(2, 2, 2);
imshow(Iblur1);
title('Smoothened Image 1');

subplot(2, 2, 3);
imshow(Iblur2);
title('Smoothened Image ');

% sharpening the best image obtained
S = imsharpen(Iblur1, 'amount', 20);

% display the final result
subplot(2, 2, 4);
imshow(S);
title('Sharpened Image');

% metric to compare the results
nI =niqe(I);
nIblur1 = niqe(Iblur1);
nS = niqe(S);
fprintf("Image score for orginal image: %0.2f.\n", nI)
fprintf("Image score for smoothened image: %0.2f.\n", nIblur1)
fprintf("Image score for sharpened image: %0.2f.\n", nS)