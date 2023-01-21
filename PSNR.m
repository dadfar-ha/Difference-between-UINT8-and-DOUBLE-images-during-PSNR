clc
clear all
rgb=imread('C:\Users\Dadfar\Desktop\New folder (2)\results\result2\Poster\original.jpg');
rgb1=imread('C:\Users\Dadfar\Desktop\New folder (2)\results\result2\Poster\Guassian\Noise\gua01_our3.png');
%psnr(rgb,rgb1,255)
figure(1);subplot(2,1,1);imshow(rgb);title('original');
figure(1);subplot(2,1,2);imshow(rgb1);title('Downsample');
s=mse(rgb1,rgb);
s1=immse(rgb1,rgb);
psnr=20 * log10(255 / sqrt(s1));
e = mean( (rgb(:) - rgb1(:)) .^ 2 );

e = immse2 (rgb1, rgb);
psnr=20 * log10(255 / sqrt(e));

%% COMPUTATION

% compute the MSE
%open immse.m