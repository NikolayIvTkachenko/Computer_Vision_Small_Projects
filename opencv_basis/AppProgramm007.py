import cv2
import numpy as np


cap = cv2.VideoCapture(0)
cv2.namedWindow("frame")


while True:
    success, frame = cap.read()

    cv2.imshow("Video", frame)

    # Averaging
    # для робота ядро лучше использовать 3х3 или 5х5
    blur = cv2.blur(frame, (10, 10))
    cv2.imshow("blur", blur)

    #Размытие Гаусса
    gauss = cv2.GaussianBlur(frame, (5, 5), 0)
    cv2.imshow("gauss", gauss)

    # Билатеральное размытие на основе Гауса но сохраняет края/границы
    # 9 - Радиус ядра - d
    # 75 sigmaColor
    # 75 sigmaSpaec
    bblur = cv2.bilateralFilter(frame, 9, 75, 75)
    cv2.imshow("bblur", bblur)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()