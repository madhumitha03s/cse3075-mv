% constrast-limited adaptive histogram equalization
clc
clear
close all

% reading the input image
I = imread('images\picture1.jpg');
M = rgb2lab(I);
H = histeq(I);
L = M(:,:,1)/100;
L = adapthisteq(L,'NumTiles',[8 8],'ClipLimit',0.005);
M(:,:,1) = L*100;
R = lab2rgb(M);

% image after histogram equalization
subplot(2,2,1); 
imshow(H); 
title('Histogram Equalized Image');

% histogram of equalized image
subplot(2,2,2); 
imhist(H); 
title('Histogram Equalization');

% image after clahe is applied
subplot(2,2,3);
imshow(R); 
title('CLAHE Image');

% histogram of clahe image
subplot(2,2,4);
imhist(R);
title('CLAHE Histogram');

% metric to compare the results
nI =niqe(I);
nR = niqe(R);
fprintf("Image score for orginal image: %0.2f.\n", nI)
fprintf("Image score for clahe image: %0.2f.\n", nR)