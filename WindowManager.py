import cv2

class WindowManager:
    def resizeWindow(self, image, width=None, height=None, interArea=cv2.INTER_AREA):

        (currentHeight, currentWidth) = image.shape[:2]

        # If specified width and height is set to none, return current image
        if width is None and height is None:
            return image

        if width is None:
            ratio = height / float(currentHeight)
            dimension = (int(currentWidth * ratio), height)
        else:
            ratio = width / float(currentWidth)
            dimension = (width, int(currentHeight * ratio))

        resizedImage = cv2.resize(image, dimension, interpolation=interArea)
        return resizedImage
