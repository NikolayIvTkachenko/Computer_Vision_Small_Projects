import cv2
import numpy as np
import LibFunctionProgram006

video = cv2.VideoCapture("video/road_field.mp4")

if not video.isOpened():
    print('error while opening the video')

while True:
    success, frame = video.read()

    frame = LibFunctionProgram006.canny(frame)



    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
