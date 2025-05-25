import cv2
import numpy as np
def run():
  
    img = cv2.imread("images/phoenix.jpg")
    # Contrast function
    contrast_img = cv2.addWeighted(img, 4, np.zeros(img.shape,img.dtype), 0, 0)
    cv2.imshow('Original image', img)
    cv2.imshow('Contrast image', contrast_img)
    cv2.waitKey(0)
if __name__ == '__main__':
    run()
