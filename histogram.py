import cv2
import numpy as np
# Import numpy library for array handling
from matplotlib import pyplot as plt
# Importing matplot library for second form of histogram
def run():
   
    img = cv2.imread("images/phoenix.jpg", cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Original Image', img) 
    # CalcHist command to create the histogram and save it to a variable
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    # Creating a figure to display images on screen
    fig, ax = plt.subplots(2, 2)
    ax[0, 0].imshow(img, cmap='gray')
    ax[0, 0].set_title('Imagen') # Title of image
    ax[0, 0].axis('off') # Don't show numbers

    ax[0, 1].plot(hist, color='gray')
    ax[1, 0].imshow(img, cmap='gray') 
    ax[1, 0].set_title('Imagen') 
    ax[1, 0].axis('off')

    ax[1, 1].hist(img.ravel(), 256, [0, 256])
    plt.show() # Show figure
    cv2.waitKey(0) 
if __name__ == '__main__':
    run()