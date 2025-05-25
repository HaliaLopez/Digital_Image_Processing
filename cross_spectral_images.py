import cv2 
import numpy as np
from matplotlib import pyplot as plt

def run ():
    img = cv2.imread("images/phoenix.jpg")

    image = cv2.resize(img, (500, 500), 1, 1)
    B, G, R = cv2.split(image)
    # NIR image (R(%60) y G(%40))
    nir = 0.6*R + 0.4*G
    nir = np.uint8(nir) 

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # FUSION 
    fused = cv2.addWeighted(gray, 0.5, nir, 0.5, 0)
    # Max pixel fusion
    fused_max = np.maximum(gray, nir)

    plt.figure(figsize=(12, 4))

    plt.subplot(141), plt.imshow(image)
    plt.title('ORIGINAL IMAGE'), plt.xticks([]), plt.yticks([])

    plt.subplot(142), plt.imshow(gray, cmap='gray')
    plt.title('GRAYSCALE IMAGE'), plt.xticks([]), plt.yticks([])

    plt.subplot(143), plt.imshow(nir, cmap='gray')
    plt.title('NIR IMAGE'), plt.xticks([]), plt.yticks([])

    plt.subplot(144), plt.imshow(fused_max, cmap='gray')
    plt.title('FUSED IMAGE'), plt.xticks([]), plt.yticks([])

    plt.show()

if __name__ == '__main__':
    run()