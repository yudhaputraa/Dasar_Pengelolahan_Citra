import os
from ultralytics import YOLO

# Set GPU device
os.environ['CUDA_VISIBLE_DEVICES'] = '0'  # Ganti '0' dengan indeks GPU yang ingin Anda gunakan

try:
    # Load a Pretrained YOLOv8n Model
    model = YOLO('yolov8m-pose.pt')

    # Run inference on the source
    results = model(source="citra2.mp4", show=True, conf=0.3, save=True)
except Exception as e:
    print(f"Error: {e}")
