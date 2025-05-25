import cv2 
def run():
    
    img = cv2.imread("images/phoenix.jpg", cv2.IMREAD_GRAYSCALE)
    # Imshow method
    cv2.imshow('Original Image', img)
    # Time function
    cv2.waitKey(0)
    
if __name__ == '__main__':
    run()