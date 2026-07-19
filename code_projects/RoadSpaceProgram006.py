import cv2
import numpy as np
import LibFunctionProgram006

video = cv2.VideoCapture("video/road_field.mp4")

if not video.isOpened():
    print('error while opening the video')

while True:
    success, frame = video.read()

    base = np.copy(frame)

    frame = LibFunctionProgram006.region_of_interest(frame)
    frame = LibFunctionProgram006.canny(frame)

    lines = cv2.HoughLinesP(frame, 2, np.pi/180, 100, np.array([()]), minLineLength=20, maxLineGap=5)
    average_lines = LibFunctionProgram006.average_slope_intercept(frame, lines=lines)

    #line_image = LibFunctionProgram006.display_lines(base, average_lines)
    line_image = LibFunctionProgram006.display_lines_fill(base, average_lines)
    combo = cv2.addWeighted(base, 0.8, line_image, 0.5, 1)

    cv2.imshow("Video", combo)
    #cv2.imshow("Video Countr", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

