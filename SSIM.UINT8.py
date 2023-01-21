from skimage.metrics import structural_similarity as ssim
import numpy as np
import cv2
import argparse


def mse(imageA, imageB):
 # the 'Mean Squared Error' between the two images is the sum of the squared difference between the two images
 mse_error = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
 mse_error /= float(imageA.shape[0] * imageA.shape[1])
	
 # return the MSE. The lower the error, the more "similar" the two images are.
 return mse_error

def compare(imageA, imageB):
 # Calculate the MSE and SSIM
 m = mse(imageA, imageB)
 multichannel=True
 s = ssim(imageA, imageB)

 # Return the SSIM. The higher the value, the more "similar" the two images are.
 return s


def main():
     imageA = cv2.imread("/content/drive/MyDrive/testing/original.png")
     imageB = cv2.imread("/content/drive/MyDrive/testing/pt_JPEG_40_our5.png")
     imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
     imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
     imageA=cv2.resize(imageA, dsize=(256,256))
     imageB=cv2.resize(imageB, dsize=(256,256))
     ssim_value  = compare(imageA, imageB)
     mse_value = mse(imageA, imageB)

     print(f"SSIM value is {ssim_value} dB")
     print(f"MSE value is {mse_value} dB")

       
if __name__ == "__main__":
    main()
