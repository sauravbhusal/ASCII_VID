import cv2
import numpy as np

capture = cv2.VideoCapture(0)
chs  = [".", ";", "|", "+", "%", "&", "#", "@"]
n_chs = len(chs)


def rescale_frame(frame, percentage):
    width = int(int(capture.get(3)) * percentage / 100)
    height = int(int(capture.get(4)) * percentage / 100)
    dimention = (width, height)
    return cv2.resize(frame, dimention, interpolation = cv2.INTER_AREA)


while True:
    ret, frame = capture.read()

    cv_resized_image = rescale_frame(frame, 50)
    cv2.imshow('frame',frame)
    cv2.imshow('resized',cv_resized_image)
    
    if cv2.waitKey(1) == ord('q'):
        break
        
capture.release()
cv2.destroyAllWindows()
