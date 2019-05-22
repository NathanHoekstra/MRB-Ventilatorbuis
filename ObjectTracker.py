import cv2

class ObjectTracker:
    def __init__(self):
        self.__boundingBox = False
        self.__tracker = cv2.TrackerKCF_create()
        self.__objectPosition = None

    def trackObject(self, frame, windowTitle):
        if self.__boundingBox is not None:
            # grab the new bounding box coordinates of the object
            (success, box) = self.__tracker.update(frame)

            # check to see if the tracking was a success
            if success:
                (x, y, w, h) = [int(v) for v in box]
                cv2.rectangle(frame, (x, y), (x + w, y + h),
                              (0, 255, 0), 2)
                self.__objectPosition = (int(x + (w/2)), int(y + (h/2)))
                cv2.circle(frame, self.__objectPosition, 5, (0, 0, 255), -1)

        cv2.imshow(windowTitle, frame)
        key = cv2.waitKey(1) & 0xFF
        # if the 's' key is selected, we are going to "select" a bounding
        # box to track
        if key == ord("s"):
            # select the bounding box of the object we want to track (make
            # sure you press ENTER or SPACE after selecting the ROI)
            self.__boundingBox = cv2.selectROI(windowTitle, frame, fromCenter=False,
                                               showCrosshair=True)

            # start OpenCV object tracker using the supplied bounding box
            # coordinates, then start the FPS throughput estimator as well
            self.__tracker.init(frame, self.__boundingBox)

    def getObjectPosition(self):
        return self.__objectPosition
