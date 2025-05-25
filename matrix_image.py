import cv2 
def run():
    img = cv2.imread("images/phoenix.jpg", cv2.IMREAD_GRAYSCALE)
    # Matrix size
    newImg = cv2.resize(img, (15, 15), 1, 1)
    # Shape for width and height
    width, height = newImg.shape[0:2]
    # Print information
    print("La matriz de la imagen es:")
    print(newImg[::])
    print("Alto y ancho")
    print(width, height) 
if __name__ == '__main__':
    run()