import cv2
import numpy as np

img = np.zeros((900, 900, 3), np.uint8)

img = cv2.line(img, (10, 10), (720, 640), (140, 160, 180), 5)
img = cv2.rectangle(img, (10, 10), (720, 640), (140, 160, 180), -1)
img = cv2.circle(img, (500, 450), 100, (255, 0, 0), 10)
img = cv2.circle(img, (500, 450), 100, (255, 255, 0), 5)

cv2.putText(img, "Text Robotics", (10, 450), 0, 10, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(img, "Text Robotics", (10, 450), 2, 0.75, (255, 255, 255), 1, cv2.LINE_AA)

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()