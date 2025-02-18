import cv2
import numpy as np


# Load image
img = cv2.imread(r"C:\Users\maxnd\Documents\Machine Learning\opencv-mediapipe\week2\image.jpeg")
if img is None:
    print("Error: Image not loaded. Check the file path or file intergrity.")
    exit()

gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Conerterting to grayscale

gray
# Show the results
cv2.imshow("Harris Corners", img)
cv2.waitKey(0)
cv2.destroyAllWindows()