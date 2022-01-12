import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    we = int(cap.get(3))
    he = int(cap.get(4))
    image = np.zeros(frame.shape, np.uint8)
    smfr = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lb = np.array([90, 50, 50])
    ub = np.array([130, 255, 255])

    mask = cv2.inRange(smfr, lb, ub)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', result)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()