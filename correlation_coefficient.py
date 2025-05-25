import cv2
import numpy as np
def run():

    img = cv2.imread("images/phoenix.jpg", cv2.IMREAD_GRAYSCALE)
    new_img = cv2.resize(img, (10, 10), 1, 1)
    img2 = cv2.imread("images/phoenix.jpg", cv2.IMREAD_GRAYSCALE)
    new_img_2 = cv2.resize(img2, (10, 10), 1, 1)
    # Function for correlation coefficient
    c = np.corrcoef(new_img, new_img_2)
    print(c[::])
if __name__ == '__main__':
    run()