import cv2
def run():
  
    img = cv2.imread("images/phoenix.jpg", cv2.IMREAD_GRAYSCALE)
    width, height = img.shape[0:2]
    # Getting the starting and ending index of the row and column
    startRow = int(width * .15)
    startCol = int(height * .15)
    endRow = int(width * .85)
    endCol = int(height * .85)
    # Mapping the values ​​for the new image
    newimg = img[startRow:endRow, startCol:endCol]
    cv2.imshow('Original image', img)
    cv2.imshow('Crop image', newimg)
    cv2.waitKey(0)
if __name__ == '__main__':
    run()