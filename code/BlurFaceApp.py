import cv2

def blur_face(img):
    (b, w) = img.shape[:2]
    dW = int(w / 3.0)
    dH = int(h / 3.0)
    if dW % 2 == 0:
        dW -= 1
    if dH % 2 == 0:
        dH -= 1

    return cv2.GaussianBlur(img, (dW, dH), 0)

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('../code_projects/haar_cascade/haarcascade_frontalface_default.xml')

while True:
    succes, img = cap.read()
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.5, minNeighbors=5, minSize=(20, 20))

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        img[y: y+h, x: x+w] = blur_face(img[y: y+h, x:x+w])

    cv2.imshow("Blur Camera", img)

    k = cv2.waitKey(1) & 0xFF
    if k ==27:
        break

cap.release()
cv2.destroyAllWindows()