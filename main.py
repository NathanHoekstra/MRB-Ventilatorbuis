import cv2
from pyfirmata import Arduino, util
import platform
import time

# if platform is macOS and board is Arduino DUE
if platform.system() == "Darwin":
    board = Arduino('/dev/cu.usbmodem14101')


def main():
    img = cv2.imread('img/lena.png',1)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    while True:
        board.digital[13].write(1)
        time.sleep(1)
        board.digital[13].write(0)
        time.sleep(0.5)