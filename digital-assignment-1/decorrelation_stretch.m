% decorrelation stretch
clc
clear 
close all

% reading the input image
I = imread('images\picture1.jpg');
S = imadjust(I,stretchlim(I));
subplot(2,2,1); 
imshow(I); 
title('Original Image');

% image after contrast stretching
subplot(2,2,2);
imshow(S); 
title('Contrast Stretched Image');

% histogram of original image
subplot(2,2,3);
imhist(I);
title('Histogram of Original Image');

% histogram after decorrelation stretching
subplot(2,2,4);
imhist(S);
title('Histogram of Decorrelation Stretched Image');

% metric to compare the results
nI =niqe(I);
nS = niqe(S);
fprintf("Image score for orginal image: %0.2f.\n", nI)
fprintf("Image score for decorrelation-stretched image: %0.2f.\n", nS)