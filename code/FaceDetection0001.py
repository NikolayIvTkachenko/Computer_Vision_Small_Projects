import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture("girl_face.mp4")

pTime = 0
cTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.75)

while True:
    success, img = cap.read()

    imgRgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(img)
    print(results)

    if results.detections:
        for id, detection in enumerate(results.detections):
            print(detection.location_data.relative_bounding_box)
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin*ih), \
                   int(bboxC.width*iw), int(bboxC.height*ih)

            cv2.rectangle(img, bbox, (255, 0, 255), 2)
            print(detection.score)
            print(id, detection)
            cv2.putText(img, f'{int(detection.score[0]*100)}%',
                        (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_PLAIN,
                        3, (255, 0, 0), 3)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Face detection", img)
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:
        break