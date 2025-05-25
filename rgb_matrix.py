import cv2
def run():

    img = cv2.imread("images/phoenix.jpg")
    B, G, R = cv2.split(img)
    newImg = cv2.resize(B, (15, 15), 1, 1)
    print("The blue matrix: ")
    print(newImg[::])
    newImg2 = cv2.resize(G, (15, 15), 1, 1)
    print("The green matrix: ")
    print(newImg2[::])
    newImg3 = cv2.resize(R, (15, 15), 1, 1)
    print("The red matrix: ")
    print(newImg3[::])
if __name__ == '__main__':
    run()