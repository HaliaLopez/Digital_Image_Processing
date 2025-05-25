import cv2
def run():
   
    img = cv2.imread("images/phoenix.jpg", cv2.IMREAD_GRAYSCALE)
    
    width, height = img.shape[0:2]
    print("Width: ", width, " Height: ", height)
   # Obtaining rotation matrix
    rotationMatrix = cv2.getRotationMatrix2D((width/2, height/2),90,1)
    # Rotation method
    rotatedImage = cv2.warpAffine(img, rotationMatrix, (width,height))
    cv2.imshow('Rotated Image', rotatedImage)
    cv2.imshow('Original Image', img)
    cv2.waitKey(0)
if __name__ == '__main__':
    run()