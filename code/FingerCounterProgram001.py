import cv2
import time
import os
import HandTrackingModule as hmt

wCam, hCam = 1280, 720
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0
cTime = 0

folderPath = "FingerImages"
fList = os.listdir(folderPath)
#print(fList)

overlayList = []

for imPath in fList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    print(f'{folderPath}/{imPath}')
    overlayList.append(image)

#print(len(overlayList))

detector = hmt.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]


while True:
    success, img = cap.read()

    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    #print(lmList)

    if len(lmList) != 0:
        # 50    100
        fingers = []

        #Thumb
        if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                #print("Index finger open")
                fingers.append(1)
            else:
                fingers.append(0)
        totalFingers = fingers.count(1)
        print(totalFingers)
        #print(fingers)

        #h, w, c = overlayList[0].shape
        #img[0:h, 0:w] = overlayList[0]
        h, w, c = overlayList[totalFingers].shape
        img[0:h, 0:w] = overlayList[totalFingers]

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (250, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Finger Counter", img)
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:
        break



