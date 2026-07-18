import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("track")
cv2.createTrackbar("T1", "track", 0, 255, nothing)
cv2.createTrackbar("T2", "track", 0, 255, nothing)

kernel=np.ones((5, 5))

while True:
    ret, frame = cap.read()

    cv2.imshow("Frame", frame)

    frame = cv2.bilateralFilter(frame, 9, 75, 75)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    thresh1=cv2.getTrackbarPos("T1", "track")
    thresh2=cv2.getTrackbarPos("T2", "track")

    canny=cv2.Canny(gray, threshold1=thresh1, threshold2=thresh2)
    dil=cv2.dilate(canny, kernel, iterations=1)

    contours, h = cv2.findContours(dil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 10000: # Более менее оптимальное число
            cv2.drawContours(frame, contour, -1, (200, 200, 0), 3)
            p = cv2.arcLength(contour, True)
            num = cv2.approxPolyDP(contour, 0.01 * p, True)
            #print(num)
            x, y, w, h = cv2.boundingRect(num)
            # Длинна num говорит о том, скколько точек есть в объекте
            print(len(num))
            cv2.rectangle(frame, (x, y, x+w, y+h), (0, 0, 256), 4)


    cv2.imshow("frame", frame)
    # cv2.imshow("Gray", gray)
    cv2.imshow("dil",dil)
    cv2.imshow("Canny", canny)

    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()


# Traceback (most recent call last):
#  File "D:\DRONES\CODE_COMPUTER_VISION\ComputerVision\pythonProject\code_projects\RecogniseObjectsProgram003.py", line 16, in <module>
#    cv2.imshow("Frame", frame)
# cv2.error: OpenCV(5.0.0) D:\a\opencv-python\opencv-python\opencv\modules\highgui\src\window.cpp:951: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow'