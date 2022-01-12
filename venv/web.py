import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    we = int(cap.get(3))
    he = int(cap.get(4))
    image = np.zeros(frame.shape, np.uint8)
    smfr = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:he // 2, :we // 2] = cv2.rotate(smfr, cv2.cv2.ROTATE_180)
    image[he // 2:, :we // 2] = cv2.rotate(smfr, cv2.cv2.ROTATE_180)
    image[:he // 2, we // 2:] = smfr
    image[he // 2:, we // 2:] = smfr

    cv2.imshow('frame', image)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()