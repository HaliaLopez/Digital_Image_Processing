import cv2 
import numpy as np
from matplotlib import pyplot as plt

def run ():
    img = cv2.imread("images/phoenix.jpg", cv2.IMREAD_GRAYSCALE)
    # Fourier Transform
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20 * np.log(np.abs(fshift))

    # Hight filter
    rows, cols = img.shape
    crow, ccol = rows // 2, cols // 2

    # Zero center mask
    mask = np.ones((rows, cols), np.uint8)
    r = 30  
    mask[crow-r:crow+r, ccol-r:ccol+r] = 0
    fshift_filtered = fshift * mask

    # Invert Fourier transform
    f_ishift = np.fft.ifftshift(fshift_filtered)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    
    plt.figure(figsize=(12, 4))

    plt.subplot(131), plt.imshow(img, cmap='gray')
    plt.title('INPUT IMAGE'), plt.xticks([]), plt.yticks([])

    plt.subplot(132), plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('MAGNITUDE SPECTRUM'), plt.xticks([]), plt.yticks([])

    plt.subplot(133), plt.imshow(img_back, cmap='gray')
    plt.title('FILTERED IMAGE (HPF)'), plt.xticks([]), plt.yticks([])

    plt.show()
if __name__ == '__main__':
    run()

