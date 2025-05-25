import cv2
import numpy as np
def run():
    img = cv2.imread("images/phoenix.jpg")
    # Glow image function
    glow_img = cv2.addWeighted(img, 1, np.zeros(img.shape,img.dtype), 0, 127)
    cv2.imshow('Original image', img)
    cv2.imshow('Brightness image', glow_img)
    cv2.waitKey(0)
if __name__ == '__main__':
    run()