import cv2
def run():
 
    img = cv2.imread("images/phoenix.jpg")
    # Split image metod
    B, G, R = cv2.split(img)
    cv2.imshow('image B', B)
    cv2.imshow('image G', G)
    cv2.imshow('image R', R)
    cv2.waitKey(0)
if __name__ == '__main__':
    run()