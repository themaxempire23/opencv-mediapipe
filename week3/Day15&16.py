import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Starting the camera
cap=cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame= cap.read()
        if not ret:
           break

        frame=cv2.flip(frame,1)
        fram_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(fram_rgb)

        if results.multi_hand_landmarks:
           for hand_landmarks in results.multi_hand_landmarks:
              mp_drawing.draw_landmarks(frame,hand_landmarks,mp_hands.HAND_CONNECTIONS)

              cv2.imshow("Hand tracking",frame)

              if cv2.waitKey(1) & 0xFF==27:
                 break
cap.release()
cv2.destroyAllWindows()   
  

              