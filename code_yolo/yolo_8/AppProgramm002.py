import torch
from ultralytics.nn.tasks import DetectionModel

# Для PyTorch 2.6+ обязательно регистрируем класс безопасности
torch.serialization.add_safe_globals([DetectionModel])

from ultralytics import YOLO
import cv2

#model = YOLO('yolov8s.pt').to('cuda')
model = YOLO('yolov8x.pt').to('cuda')
#model = YOLO('yolov8x.pt').to('cpu')

cap = cv2.VideoCapture("../video/auto_fro_camera_short.mp4")

while True:
    success, img = cap. read()

    if not success:
        break

    #cv2.imshow("Video", img)
    results = model(img, show=False)
    annotated_frame = results[0].plot()

    cv2.imshow("Picture", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break