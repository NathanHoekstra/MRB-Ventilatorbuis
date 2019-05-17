import cv2

class ObjectTracker:
    def __init__(self):
        self.BoundingBox = False
        self.tracker = cv2.TrackerKCF_create()

    def trackObject(self, frame):
        if self.BoundingBox is not None:
            # grab the new bounding box coordinates of the object
            (success, box) = self.tracker.update(frame)

            # check to see if the tracking was a success
            if success:
                (x, y, w, h) = [int(v) for v in box]
                cv2.rectangle(frame, (x, y), (x + w, y + h),
                              (0, 255, 0), 2)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        # if the 's' key is selected, we are going to "select" a bounding
        # box to track
        if key == ord("s"):
            # select the bounding box of the object we want to track (make
            # sure you press ENTER or SPACE after selecting the ROI)
            self.BoundingBox = cv2.selectROI("Frame", frame, fromCenter=False,
                                   showCrosshair=True)

            # start OpenCV object tracker using the supplied bounding box
            # coordinates, then start the FPS throughput estimator as well
            self.tracker.init(frame, self.BoundingBox)
