def PSNR(original, noisy):
    mse = np.mean((original - noisy) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr
  
def main():
     original = cv2.imread("/content/drive/MyDrive/testing/original.png")
     noisy = cv2.imread("/content/drive/MyDrive/testing/pt_JPEG_40_our5.png")
     original=cv2.resize(original,(256,256))
     noisy=cv2.resize(noisy, (256,256))
     value = PSNR(original, noisy)
     mse2 = np.mean((original - noisy) ** 2)

     print(f"PSNR value is {value} dB")
     print(f"mse value is {mse2} dB")

       
if __name__ == "__main__":
    main()