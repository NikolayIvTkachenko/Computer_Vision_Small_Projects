import cv2
import numpy as np

def nothing(x):
    pass


img = np.zeros((300, 300, 3), np.uint8)
cv2.namedWindow('Image')

cv2.createTrackbar('R', 'Image', 0, 255, nothing)
cv2.createTrackbar('G', 'Image', 0, 255, nothing)
cv2.createTrackbar('B', 'Image', 0, 255, nothing)

while True:
    cv2.imshow('Image', img)

    r = cv2.getTrackbarPos('R', 'Image')
    g = cv2.getTrackbarPos('G', 'Image')
    b = cv2.getTrackbarPos('B', 'Image')

    img[:] = [b, g, r]

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break



