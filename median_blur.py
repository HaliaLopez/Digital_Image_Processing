import cv2
def run():
    img = cv2.imread("images/phoenix.jpg")
    # Median blur method
    blur_img = cv2.medianBlur(img, 15)
    cv2.imshow('Original image', img)
    cv2.imshow('Blur image', blur_img)
    cv2.waitKey(0)
if __name__ == '__main__':
    run()