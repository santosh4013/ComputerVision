import numpy as np
import cv2
cap = cv2.VideoCapture('venv/pedestrian.mp4')

while True:
    ret, frame = cap.read()
    result = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", result)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()