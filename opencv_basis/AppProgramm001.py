#https://www.youtube.com/watch?v=oc64kCbPi6o&list=PLVFGVo0DNh5duhps6KsiCQIoObyzcM2Cs

import cv2
import numpy as np

img = cv2.imread("images/logo_ocp_001.jpg", 1)
cv2.namedWindow("Image", cv2.WINDOW_AUTOSIZE)
#WINDOW_NORMAL растягивать изображение возможно
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()


