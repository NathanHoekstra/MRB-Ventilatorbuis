import cv2
from BallDetector import  BallDetector
from ObjectTracker import ObjectTracker
from PIDController import *


def main():
    ballLower = (8, 130, 200)
    ballUpper = (255, 255, 255)

    ballDetector = BallDetector(ballLower, ballUpper)
    objectTracker = ObjectTracker()
    pidController = PIDController(1, 1, 1, 20)

    print("Program started, press q to quit the application")
    print("When using the ObjectTracker, press s to freeze a frame and use the mouse to select an object")

    cap = cv2.VideoCapture(0)
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        fps = cap.get(cv2.CAP_PROP_FPS)
        height, width = frame.shape[:2]
        windowTitle = "Object detection W: " + str(width) + " H: " + str(height)

        frame = ballDetector.locateBall(frame)
        objectTracker.trackObject(frame, windowTitle)

        pidController.setBallPosition(ballDetector.getBallPosition())
        pidController.setSetpoint(objectTracker.getObjectPosition())

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()