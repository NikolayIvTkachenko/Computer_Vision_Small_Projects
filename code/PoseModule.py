import time
import cv2
import mediapipe as mp


class poseDetector():

    def __init__(self, mode=False, upBody=False, smooth=True, detectionCom=0.5, trackCon=0.5):
        self.mode=mode
        self.upBody=upBody
        self.smooth=smooth
        self.detectionCon=detectionCom
        self.trackCon=trackCon
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode,
                                     1,
                                     self.upBody,
                                     self.smooth,
                                     True,
                                     self.detectionCon,
                                     self.trackCon)

        # static_image_mode=False,
        # model_complexity=1,
        # smooth_landmarks=True,
        # enable_segmentation=False,
        # smooth_segmentation=True,
        # min_detection_confidence=0.5,
        # min_tracking_confidence=0.5):

        # self.smooth,

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        print(self.results.pose_landmarks)
        if draw:
            if self.results.pose_landmarks:
                self.mpDraw.draw_landmarks(
                    img,
                    self.results.pose_landmarks,
                    self.mpPose.POSE_CONNECTIONS
                )
        return img

    def findPosition(self, img, draw=True):
        lmList = []

        for id, lm in enumerate(self.results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)
            cx, cy = int(lm.x*w), int(lm.y*h)
            lmList.append([id, cx, cy])
            if draw:
                cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)

        return lmList

def main():
    pTime = 0
    cTime = 0
    # cap = cv2.VideoCapture(0)
    # human_walking
    # cap = cv2.VideoCapture("human_walking.mp4")
    cap = cv2.VideoCapture("girl_dancing.mp4")

    detector = poseDetector()

    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img)
        print(lmList)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('q') or key == 27:
            break

if __name__ == "__main__":
    main()



