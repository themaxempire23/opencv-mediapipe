import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

video_path = r"C:\Users\maxnd\Documents\Machine Learning\mediapipe\opencv-mediapipe\week3\Soccer_Match_topview.mp4"
cap = cv2.VideoCapture(video_path)

desired_width = 640

with mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.7) as pose:
    while cap.isOpened():
        ret,frame = cap.read()
        if not ret:
            break

        height, width, _ = frame.shape
        scale = desired_width / width
        resized_frame = cv2.resize(frame, (desired_width, int(height * scale)))

        resized_frame = cv2.flip(resized_frame, 1)

        cv2.imshow("Pose Estimation", resized_frame)