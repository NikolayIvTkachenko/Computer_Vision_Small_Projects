import cv2
import numpy as np

# HSV Hue Saturation Value

# изменение цветового простраства

# cv2.cvtColor(frame, flag)


def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("frame")

cv2.createTrackbar("HL", "frame", 0, 180, nothing)
cv2.createTrackbar("SL", "frame", 0, 255, nothing)
cv2.createTrackbar("VL", "frame", 0, 255, nothing)

cv2.createTrackbar("H", "frame", 0, 180, nothing)
cv2.createTrackbar("S", "frame", 0, 255, nothing)
cv2.createTrackbar("V", "frame", 0, 255, nothing)



while True:
    success, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hl = cv2.getTrackbarPos("HL", "frame")
    sl = cv2.getTrackbarPos("SL", "frame")
    vl = cv2.getTrackbarPos("VL", "frame")

    h = cv2.getTrackbarPos("H", "frame")
    s = cv2.getTrackbarPos("S", "frame")
    v = cv2.getTrackbarPos("V", "frame")

    lower = np.array([hl, sl, vl])
    upper = np.array([h, s, v])

    mask = cv2.inRange(hsv, lower, upper)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.rotate(res, cv2.ROTATE_90_CLOCKWISE)

    height, width = res.shape[:2]
    res = cv2.resize(res, (height * 2, width * 2), interpolation=cv2.INTER_CUBIC)

    cv2.imshow("Video", frame)
    # cv2.imshow("hsv", hsv)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()