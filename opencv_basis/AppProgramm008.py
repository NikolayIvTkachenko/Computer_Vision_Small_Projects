import cv2
import numpy as np


cap = cv2.VideoCapture(0)
cv2.namedWindow("frame")


while True:
    success, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    success, t1 = cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY)
    success, t2 = cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY_INV)
    success, t3 = cv2.threshold(frame, 127, 255, cv2.THRESH_TRUNC)
    success, t4 = cv2.threshold(frame, 127, 255, cv2.THRESH_TOZERO)
    success, t5 = cv2.threshold(frame, 127, 255, cv2.THRESH_TOZERO_INV)


    cv2.imshow("t1", t1)
    cv2.imshow("t2", t2)
    cv2.imshow("t3", t3)
    cv2.imshow("t4", t4)
    cv2.imshow("t5", t5)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()