import cv2
import numpy as np
from matplotlib import pyplot as plt

def run():
  
    img = cv2.imread("images/phoenix.jpg", cv2.IMREAD_GRAYSCALE)

    # Morphology operations
    # Element (Diamond 3x3)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    # Apply opening (Erosion then dilation)
    opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    # Apply closure (Dilation followed by erosion)
    closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)

    # Normalize image
    closed = cv2.normalize(closed, None, 0, 255, cv2.NORM_MINMAX)

    # Convert image to uint8 type

    closed_uint8 = np.uint8(closed)

    # Canny method
    edges =cv2.Canny(closed_uint8, 50, 150) 


    white_edges = np.zeros_like(edges)
    white_edges[edges > 0] = 255

    closed_edges = cv2.morphologyEx(white_edges, cv2.MORPH_CLOSE, kernel)

    plt.figure(figsize=(12, 2))

    plt.subplot(121), plt.imshow(white_edges, cmap='gray')
    plt.title('CLOSE EDGES'), plt.xticks([]), plt.yticks([])

    plt.subplot(122), plt.imshow(closed_edges, cmap='gray')
    plt.title('WHITE CLOSE EDGES'), plt.xticks([]), plt.yticks([])

    plt.show()
    
if __name__ == '__main__':
    run() 

    