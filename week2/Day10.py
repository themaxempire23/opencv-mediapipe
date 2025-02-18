# Corner Harris

import cv2
import numpy as np


# Load image
img = cv2.imread(r"C:\Users\maxnd\Documents\Machine Learning\opencv-mediapipe\week2\image.jpeg")
if img is None:
    print("Error: Image not loaded. Check the file path or file intergrity.")
    exit()

gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Conerterting to grayscale

gray=np.float32(gray)

dst=cv2.cornerHarris(gray,2,3,0..04)

dst=cv2.dilate(dst,None)
img[dst>0.01*dst.max()]=[0,255,0]

# Show the results
cv2.imshow("Harris Corners", img)
cv2.waitKey(0)
cv2.destroyAllWindows()