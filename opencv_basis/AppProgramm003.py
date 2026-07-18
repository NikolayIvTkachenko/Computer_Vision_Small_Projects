import cv2

img1 = cv2.imread("images/logo_ocp_003.jpg")
img2 = cv2.imread("images/robocop.jpg")

# Объедение картинок должны совпадать по размерам, высоте и ширене картинок должны быть одинаково
h1, w1 = img1.shape[:2]
img2_resized = cv2.resize(img2, (w1, h1), interpolation=cv2.INTER_LINEAR)

# s = cv2.add(img1, img2_resized)

# s = cv2.subtract(img1, img2_resized)

# Смешивание изображений
s = cv2.addWeighted(img1, 1, img2_resized, 0.05, 0)

cv2.imshow('add', s)


cv2.imshow('add', s)
cv2.waitKey(0)
cv2.destroyAllWindows()