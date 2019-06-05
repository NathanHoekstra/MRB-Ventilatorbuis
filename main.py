import cv2
import keyboard
import time

from WindowManager import WindowManager
from BallDetector import  BallDetector
from ObjectTracker import ObjectTracker
from PIDController import *

from ArduinoHandler import ArduinoHandler

def main():
    ballLower = (8, 130, 160)
    ballUpper = (255, 255, 255)

    windowManager = WindowManager()
    ballDetector = BallDetector(ballLower, ballUpper)
    objectTracker = ObjectTracker()
    pidController = PIDController(1, 1, 1, 20)

    print("Program started, press q to quit the application")
    print("When using the ObjectTracker, press s to freeze a frame and use the mouse to select an object")
    cap = cv2.VideoCapture(0)


    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
    cap.set(cv2.CAP_PROP_FPS, 60)
    #cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = windowManager.resizeWindow(frame, width=1200)
        fps = cap.get(cv2.CAP_PROP_FPS)
        height, width = frame.shape[:2]
        windowTitle = "Object detection W: " + str(width) + " H: " + str(height) + " FPS: " + str(fps)

        frame = ballDetector.locateBall(frame)
        objectTracker.trackObject(frame, windowTitle)

        if objectTracker.isSelected():
            pidController.setBallPosition(ballDetector.getBallPosition())
            pidController.setSetpoint(objectTracker.getObjectPosition())
            pidController.setFrameRate(fps)
            print(pidController.pwmOutput())

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def firmataTest():
    PWM_3 = 'd:3:p'
    LED_BUILTIN = 13
    nano = ArduinoHandler()
    nano.setAnalogPort(PWM_3)
    pwm = 0
    while True:
        if keyboard.is_pressed('u'):
            pwm = 0.630
        elif keyboard.is_pressed('d'):
            pwm = 1
        print(pwm)
        nano.analogWrite(pwm)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
    #firmataTest()