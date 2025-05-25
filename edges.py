import cv2
def run():
  
    img = cv2.imread("images/phoenix.jpg")
    # Canny method
    edge_img = cv2.Canny(img, 100, 200)
    cv2.imshow('Original image', img)
    cv2.imshow('Edge image', edge_img)
    cv2.waitKey(0)
if __name__ == '__main__':
    run()