import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture("two_people_talks.mp4")

pTime = 0
cTime = 0



while True:
    success, img = cap.read()


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Face detection", img)
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:
        break