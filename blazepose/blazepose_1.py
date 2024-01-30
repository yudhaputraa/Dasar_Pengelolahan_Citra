import cv2
import mediapipe as mp

# Inisialisasi BlazePose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Baca frame dari webcam
cap = cv2.VideoCapture(0)  # Ganti dengan 1 jika menggunakan webcam eksternal

while cap.isOpened():
    ret, frame = cap.read()

    # Konversi frame ke format RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Deteksi pose
    results = pose.process(rgb_frame)

    # Gambar landmark pose jika terdeteksi
    if results.pose_landmarks:
        for landmark in results.pose_landmarks.landmark:
            x = int(landmark.x * frame.shape[1])
            y = int(landmark.y * frame.shape[0])
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

    # Tampilkan frame yang telah dimodifikasi
    cv2.imshow('Human Pose Estimation', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup webcam dan jendela
cap.release()
cv2.destroyAllWindows()
