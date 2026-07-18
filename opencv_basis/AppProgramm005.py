import cv2
import numpy as np


cap = cv2.VideoCapture(0)
cv2.namedWindow("frame")


while True:
    success, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Sobel() вычисление градиентов
    # cv2.CV_64F -
    #framex = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    #framey = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    framex = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    framey = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
    edge=cv2.Canny(gray, 120, 180) # 80, 150 # 150, 220


    cv2.imshow("Video", frame)
    cv2.imshow("x", framex)
    cv2.imshow("y", framey)
    cv2.imshow("edge", edge)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()