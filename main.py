import numpy as np
import cv2
cap = cv2.VideoCapture('venv/pedestrian.mp4')

while cap.isOpened():
    ret, frame = cap.read()

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()

