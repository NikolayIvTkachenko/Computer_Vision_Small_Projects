import cv2
import mediapipe as mp
import time


class FaceMeshDetector():
    def __init__(self, staticMode=False, maxFaces=2, minDetectionCon=0.5, minTrackCon=0.5):


        self.staticMode=staticMode
        self.maxFaces=maxFaces
        self.minDetectionCon=minDetectionCon
        self.minTrackCon=minTrackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode,
                                                 self.maxFaces,
                                                 False,
                                                 self.minDetectionCon,
                                                 self.minTrackCon)
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)



    def findMeshFace(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.faceMesh.process(imgRGB)
        if results.multi_face_landmarks:
            for faceLms in results.multi_face_landmarks:
                # mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACE_CONNECTIONS)
                self.mpDraw.draw_landmarks(img,
                                      faceLms,
                                      self.mpFaceMesh.FACEMESH_CONTOURS,
                                      self.drawSpec,
                                      self.drawSpec)
            for id, lm in enumerate(faceLms.landmark):
                print(lm)
                ih, iw, ic = img.shape
                x, y = int(lm.x * iw), int(lm.y * ih)
                print(id, x, y)


def main():
    # cap = cv2.VideoCapture("two_people_talks.mp4")
    # cap = cv2.VideoCapture("girl_face.mp4")
    cap = cv2.VideoCapture("two_people_2.mp4")

    pTime = 0
    cTime = 0
    detector = FaceMeshDetector()
    while True:
        success, img = cap.read()
        detector.findMeshFace(img)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow("Face detection", img)
        key = cv2.waitKey(1)
        if key == ord('q') or key == 27:
            break


if __name__ == "__main__":
    main()



