import cv2
import mediapipe as mp
import time
import numpy as np
import HandTrackingModule as htm

wCam, hCam = 1280, 720
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0
cTime = 0

detector = htm.handDetector(detectionCon=0.7)


while True:
    success, img = cap.read()

    img = detector.findHands(img)
    lmList = detector.fi


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Gesture detection:", img)
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:
        break