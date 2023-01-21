#MSE
import numpy
import math

def psnr(img1, img2):
    mse = numpy.mean( (img1 - img2) ** 2 )
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

original = cv2.imread("/content/original.jpg")
noisy = cv2.imread("/content/gua01_our3.png")   
value = psnr(original, noisy)
print(f"PSNR value is {value} dB")
mse = numpy.mean( (original - noisy) ** 2 )
print("MSE1:", mse)
Y = np.square(np.subtract(original,noisy)).mean()
print("MSE2:", Y)