# Контуры

import cv2
import numpy as np


cap = cv2.VideoCapture(0)
cv2.namedWindow("frame")


while True:
    success, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(gray, 100, 200)
    # Алгоритм фильтрайции контуров - cv2.RETR_LIST
    # cv2.CHAIN_APPROX_NONE - без урезания контуров
    contours, h = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    # Сортировка контуров по площади, первый самые большие
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    # -1 - нарисовать все контуры
    # 1 - нарисовать водин контур
    cv2.drawContours(frame, [contours[0]], -1, (0, 0, 255), 5)

    cv2.imshow("Video", frame)
    cv2.imshow("edge", edge)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()