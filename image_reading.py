import cv2 #import library OpenCv
def run ():
    # Image reading
    img = cv2.imread("images/phoenix.jpg", cv2.IMREAD_GRAYSCALE)
if __name__ == '__main__':
    run()
