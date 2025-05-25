import cv2
def run():
 
    img = cv2.imread("images/phoenix.jpg", cv2.IMREAD_GRAYSCALE)

    cv2.imshow('Original Image', img)
    # Thresholding OTSU
    threshold, imgu = cv2.threshold(img, 127, 255, cv2.THRESH_OTSU)
    # Binary Thresholding
    threshold, imgu2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # Invert binary Thresholding
    threshold, imgu3 = cv2.threshold(img, 127, 255,cv2.THRESH_BINARY_INV)
    # Trunc Thresholding
    threshold, imgu4 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    # To zero Thresholding
    threshold, imgu5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    # Invert to zero Thresholding
    threshold, imgu6 = cv2.threshold(img, 127, 255,cv2.THRESH_TOZERO_INV)
    
    cv2.imshow('Otsu', imgu)
    cv2.imshow('Binary', imgu2)
    cv2.imshow('Binary_Inv', imgu3)
    cv2.imshow('Trunc', imgu4)
    cv2.imshow('To_zero', imgu5)
    cv2.imshow('To_zero_inv', imgu6)
    # función de tiempo para no cerrar ventanas
    cv2.waitKey(0)
if __name__ == '__main__':
    run()