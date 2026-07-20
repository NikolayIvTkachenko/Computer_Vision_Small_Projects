from ultralytics import YOLO
model = YOLO('yolov8s.pt')
#model = YOLO('yolov8x-seg.pt')
#model = YOLO('yolov8n.pt')
#model1 = YOLO('yolov8n-seg.yaml')
#model2 = YOLO('yolov8n-seg.pt')
#model3 = YOLO('yolov8n-seg.yaml').load('yolov8n.pt')
#results = model.train(data='mydataset_yolo/data.yaml', epochs=100, imgsz=640)


#docs.ultralytics.com