import cv2
import time
from ArduinoHandler import ArduinoHandler
from BallDetector import  BallDetector

PWM_3 = 'd:3:p'
LED_BUILTIN = 13

ballLower = (8, 130, 200)
ballUpper = (255, 255, 255)

ballDetector = BallDetector(ballLower, ballUpper)

def main():
    print("Program started, press q to quit the application")
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        result = ballDetector.locateBall(frame)

        # Display the resulting frame
        cv2.imshow('frame', result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()