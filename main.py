import cv2
import time
from arduinoHandler import arduinoHandler

PWM_3 = 'd:3:p'
LED_BUILTIN = 13

def main():
    img = cv2.imread('img/lena.png',1)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def blink():
    due = arduinoHandler()
    while True:
        due.digitalWrite(LED_BUILTIN, True)
        time.sleep(1)
        due.digitalWrite(LED_BUILTIN, False)
        time.sleep(0.5)

if __name__ == "__main__":
    blink()