import torch
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU device name: {torch.cuda.get_device_name(0)}")
else:
    print("Current build: ", torch.version)


import cv2
from ultralytics import YOLO

# yolov12n-face.pt
# model = YOLO('yolov8n-face.pt').to('cpu')
model = YOLO('yolov8n-face.pt').to('cuda')
# mps - для macbook
# cuda - для видео краты
cap = cv2.VideoCapture(0)

i = 0
while True:
    i += 1

    ret, frame = cap.read()
    results = model.predict(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("YOLO v12. TEST.", annotated_frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

#pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
# raise AssertionError("Torch not compiled with CUDA enabled")
# AssertionError: Torch not compiled with CUDA enabled
# Эта ошибка означает, что установленная у вас библиотека PyTorch не
# поддерживает вычисления на видеокарте (GPU). Вы пытаетесь запустить код, который требует CUDA,
# но ваша версия библиотеки скомпилирована только для работы на центральном процессоре (CPU).
# Для pip и CUDA 12.4: pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124