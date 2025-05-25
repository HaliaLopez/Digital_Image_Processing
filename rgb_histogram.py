import cv2
from matplotlib import pyplot as plt
def run():
    
    img = cv2.imread("images/phoenix.jpg")
    cv2.imshow('Original image', img)
    # Split chanels
    chanels = cv2.split(img)
    colors = ("b", "g", "r")
    plt.figure()
    # Figure title
    plt.title('RGB histogram')
    plt.xlabel('Bits')
    plt.ylabel('Pixels')
 
    for (chanel, color) in zip (chanels, colors):
        # Histogram for chanel
        histogram = cv2.calcHist([chanel], [0], None, [256], [0, 256])
        plt.plot(histogram, color=color)
        plt.xlim([0, 256])

    plt.show()
    cv2.waitKey(0)
if __name__ == '__main__':
    run()