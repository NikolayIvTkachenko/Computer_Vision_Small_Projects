import time
import cv2
import mediapipe as mp


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands() #self.mode,
                                        #self.maxHands,
                                        #self.detectionCon,
                                        #self.trackCon)

    def findHands(self, image, draw=True):
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_drawing.draw_landmarks(
                        image,
                        hand_landmarks,
                        self.mphands.HAND_CONNECTIONS
                    )
        return image

    def findPosition(self, image):
        for id, lm in enumerate(self.results.hand_landmarks.landmark):
            print(id, lm)
            h, w, c = image.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            print(cx, cy)

            if id == 0:
                cv2.circle(image, (cx, cy), 25, (255, 0, 255), cv2.FILLED)


def main():

    pTime = 0
    cTime = 0

    detector = handDetector()
    cap = cv2.VideoCapture(0)

    while True:
        data, image = cap.read()
        img = detector.findHands(image)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("HAND", img)
        key = cv2.waitKey(1)
        if key == ord('q') or key == 27:
            break


if __name__ == "__main__":
    main()

