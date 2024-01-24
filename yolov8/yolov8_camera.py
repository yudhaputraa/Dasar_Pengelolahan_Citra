from ultralytics import YOLO

# Load a Pretrained YOLOv8n Model
model = YOLO('yolov8m-pose.pt')

# Run inference on the camera (using camera index 0)
results = model(source=0, show=True, conf=0.3)

# Tambahkan loop untuk menangani frame dari kamera secara real-time
while True:
    # Dapatkan frame dari kamera
    frame = capture_frame_from_camera()  # Implementasikan fungsi ini sesuai dengan pustaka atau API kamera yang Anda gunakan

    # Run inference pada setiap frame
    results = model(source=frame, show=True, conf=0.3)

    # TODO: Lakukan sesuatu dengan hasil deteksi seperti menampilkan atau menyimpannya

    # Hentikan loop jika diperlukan (misalnya, tekan tombol tertentu)
    if user_presses_exit():
        break
