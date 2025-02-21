# Histograms and color Normalization
# Applying filters to images 

import cv2
import numpy as np


# Load image
img = cv2.imread(r"C:\Users\maxnd\Documents\Machine Learning\opencv-mediapipe\week2\image.jpeg", cv2.IMREAD_GRAYSCALE)
if img is None:
    exit()

equalized=cv2.equalizeHist(img)
normalized=cv2.normalize(img,None,0,255,cv2.NORM_MINMAX)

# Display the results
cv2.imshow("Original", img)
cv2.imshow("Equalized Image", equalized)
cv2.imshow("Normalized Image", normalized)
cv2.waitKey(0)
cv2.destroyAllWindows() 