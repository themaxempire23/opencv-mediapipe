import cv2
import numpy as np


# Load image
img = cv2.imread(r"C:\Users\maxnd\Documents\Machine Learning\opencv-mediapipe\week2\image.jpeg")
if img is None:
    print("Error: Image not loaded. Check the file path or file intergrity.")
    exit()

_, binary =cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) # Conerterting to grayscale

#kernel = np.ones((5,5), np.unt8)
#kernel = np.ones((5,5), np.unt8)

kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(binary, kernel, iterations=1)
dilation = cv2.dilate(binary, kernel, iterations=1)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)


# Show the results
cv2.imshow("Original", binary)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()