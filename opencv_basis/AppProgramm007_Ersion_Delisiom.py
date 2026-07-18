import cv2
import numpy as np


def nothing(x):
    pass


kernel = np.ones((5, 5), np.uint8)

cap = cv2.VideoCapture(0)

cv2.namedWindow("frame")

cv2.createTrackbar("H", "frame", 0, 180, nothing)
cv2.createTrackbar("S", "frame", 0, 255, nothing)
cv2.createTrackbar("V", "frame", 0, 255, nothing)

cv2.createTrackbar("HL", "frame", 0, 180, nothing)
cv2.createTrackbar("SL", "frame", 0, 255, nothing)
cv2.createTrackbar("VL", "frame", 0, 255, nothing)

while True:
    success, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h = cv2.getTrackbarPos("H", "frame")
    s = cv2.getTrackbarPos("S", "frame")
    v = cv2.getTrackbarPos("V", "frame")

    hl = cv2.getTrackbarPos("HL", "frame")
    sl = cv2.getTrackbarPos("SL", "frame")
    vl = cv2.getTrackbarPos("VL", "frame")

    lower = np.array([hl, sl, vl])
    upper = np.array([h, s, v])

    frame = cv2.bilateralFilter(frame, 9, 75, 75)

    mask = cv2.inRange(hsv, lower, upper)

    res = cv2.bitwise_and(frame, frame, mask=mask)
    edge = cv2.Canny(mask, 100, 200)

    countours, h = cv2.findContours(edge, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    countours = sorted(countours, key=cv2.contourArea, reverse=True)

    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)
    # морфологическон открытие или закрытие
    opennig = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opennig, cv2.MORPH_CLOSE, kernel)

    try:
        cv2.drawContours(frame, [countours[0]], -1, (255, 0, 0), 5)
    except Exception:
        print()

    cv2.imshow("mask", mask)
    cv2.imshow("er", erosion)
    cv2.imshow("dil", dilation)
    cv2.imshow("open", opennig)
    cv2.imshow("close", closing)
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
