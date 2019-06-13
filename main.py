import cv2

from WindowManager import WindowManager
from BallDetector import  BallDetector
from ObjectTracker import ObjectTracker
from PIDController import *
from ArduinoHandler import ArduinoHandler

mouseClickPosition = (100, 300)

def onMouseClickEvent(event, x, y, flags, params):
    global mouseClickPosition
    if event == cv2.EVENT_LBUTTONDBLCLK:
        mouseClickPosition = (x, y)

def main():
    ballLower = (8, 130, 160)
    ballUpper = (255, 255, 255)

    windowManager = WindowManager()
    ballDetector = BallDetector(ballLower, ballUpper)
    objectTracker = ObjectTracker()
    nano = ArduinoHandler()
    pidController = PIDController(1, 1, 2, 20, nano)
    nano.setAnalogPort('d:3:p')

    print("Program started, press q to quit the application")
    print("When using the ObjectTracker, press s to freeze a frame and use the mouse to select an object")
    cap = cv2.VideoCapture(0)


    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
    cap.set(cv2.CAP_PROP_FPS, 60)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = windowManager.resizeWindow(frame, width=800)
        fps = cap.get(cv2.CAP_PROP_FPS)
        height, width = frame.shape[:2]

        windowTitle = "Object detection W: " + str(width) + " H: " + str(height) + " FPS: " + str(fps)
        #cv2.setMouseCallback(windowTitle, onMouseClickEvent)

        frame = ballDetector.locateBall(frame)
        objectTracker.trackObject(frame, windowTitle)

        if objectTracker.isSelected():
            pidController.controlPIDFan(ballDetector.getBallPosition(), objectTracker.getObjectPosition(), fps)

        elif ballDetector.isBallFound() and not objectTracker.isSelected():
            pidController.controlPIDFan(ballDetector.getBallPosition(), mouseClickPosition, fps)

        else:
            nano.analogWrite(0.8)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()