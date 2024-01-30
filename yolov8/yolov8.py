from ultralytics import YOLO

model = YOLO('yolov8m-pose.pt')

results = model.track(source='citra2.mp4', show=True, tracker='bytetrack.yaml')