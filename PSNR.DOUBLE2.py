#PSNR SSIM SKIMAGE
from skimage.metrics import peak_signal_noise_ratio
original = cv2.imread("/content/drive/MyDrive/testing/original.png")
noisy = cv2.imread("/content/drive/MyDrive/testing/pt_JPEG_40_our3.png")  
d=peak_signal_noise_ratio(noisy,original,data_range=255)
from skimage.metrics import structural_similarity as ssim
print(d)
ss=ssim(original,noisy,multichannel=True)
print(ss)