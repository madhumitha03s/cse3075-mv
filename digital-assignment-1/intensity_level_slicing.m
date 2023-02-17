% program for intensity level slicing
clc
clear 
close all

% reading the input image
A = imread('images\picture1.jpg');
B = double(A);
[m, n] = size(B);

% intensity level slicing
max_int = double(255);
P = double(round(max_int/1.25));
Q = double(round(2*max_int));

for i = 1:m
    for j = 1:m
        if(B(i, j) >= P && B(i, j) <= Q)
            C(i, j) = max_int;
        else
            C(i, j) = B(i, j);
        end
    end
end

% display the original image
subplot(1, 2, 1);
imshow(A);
title('Original Image');

% display the image after intensity level slicing
subplot(1, 2, 2);
imshow(unit8(C));
title('Intensity level sliced Image');