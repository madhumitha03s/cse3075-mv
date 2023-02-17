% image enhancement
clear;
close all;
I = imread('images\picture1.jpg');
subplot(2, 3, 1);
imshow(I);

% detaching the background to view it
se = strel('disk', 15);
Background = imopen(I, se); 
subplot(2, 3, 2);
imshow(Background);

% subtracting the blurred background from the image
enhancedI = I - Background;
subplot(2, 3, 3);
imshow(enhancedI);

% converting the rgb image to grayscale
J = imadjust(rgb2gray(I));
subplot(2, 3, 4);
imshow(J);

% applying gaussian filter to remove noise 
IJ = imnoise(J, 'gaussian', 0, 0.0001);
subplot(2, 3, 5);
imshow(IJ);

% metric to compare the results
nI =niqe(I);
nIJ = niqe(IJ);
fprintf("Image score for orginal image: %0.2f.\n", nI)
fprintf("Image score for enhanced image: %0.2f.\n", nIJ)