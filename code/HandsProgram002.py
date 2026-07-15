import time

import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mphands = mp.solutions.hands

cap=cv2.VideoCapture(0)
hands=mphands.Hands()

pTime = 0
cTime = 0

while True:
    data, image=cap.read()
    image=cv2.cvtColor(cv2.flip(image,1), cv2.COLOR_BGR2RGB)
    results=hands.process(image)
    image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                print(id, lm)
                h, w, c = image.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(cx, cy)

                if id == 0:
                    cv2.circle(image, (cx, cy), 25, (255, 0, 255), cv2.FILLED)

            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mphands.HAND_CONNECTIONS
            )

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(image, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("HAND", image)
    key = cv2.waitKey(5)
    if key == ord('q') or key == 27:
        break

cap.release()
cv2.destroyAllWindows()