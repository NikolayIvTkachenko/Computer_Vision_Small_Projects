import cv2
import mediapipe as mp
import time


class Facedetector():
    def __init__(self, minDetectionCon=0.5):
        self.minDetectionCon = minDetectionCon
        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(0.75)

    def findFace(self, img, draw=True):
        imgRgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRgb)
        print(self.results)

        bboxs = []

        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                print(detection.location_data.relative_bounding_box)
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                    int(bboxC.width * iw), int(bboxC.height * ih)

                bboxs.append([id, bbox, detection.score])

                cv2.rectangle(img, bbox, (255, 0, 255), 2)
                print(detection.score)
                print(id, detection)
                cv2.putText(img, f'{int(detection.score[0] * 100)}%',
                            (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN,
                            3, (255, 0, 0), 3)

        return img, bboxs


def main():
    print("Main Program")
    #cap = cv2.VideoCapture("girl_face.mp4")
    #people_on_street.mp4
    #cap = cv2.VideoCapture("people_on_street.mp4")
    #people_on_street_2.mp4
    cap = cv2.VideoCapture("people_on_street_2.mp4")

    pTime = 0
    cTime = 0

    detector = Facedetector()

    while True:
        success, img = cap.read()

        img, bboxs = detector.findFace(img)

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
