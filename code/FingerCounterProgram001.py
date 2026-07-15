import math
import cv2
import mediapipe as mp
import time
import numpy as np
import os

wCam, hCam = 1280, 720
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0
cTime = 0

folderPath = "FingerImages"
fList = os.listdir(folderPath)
print(fList)

overlayList = []

for imPath in fList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    print(f'{folderPath}/{imPath}')
    overlayList.append(image)

print(len(overlayList))





while True:
    success, img = cap.read()

    h, w, c = overlayList[0].shape
    img[0:h, 0:w] = overlayList[0]



    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Finger Counter", img)
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:
        break



