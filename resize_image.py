import cv2 
def run():
    
    img = cv2.imread("images/phoenix.jpg", cv2.IMREAD_GRAYSCALE)
    # Using the resize method with the number of rows and columns
    newImg = cv2.resize(img, (500, 500), 1, 1)
    cv2.imshow('New Image', newImg)
    cv2.imshow('Original Image', img)
    cv2.waitKey(0)
if __name__ == '__main__':
    run()
