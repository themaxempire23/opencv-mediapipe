# Affine Transformation->Is rotating an image and leaving a blank space

import cv2
import numpy as np


# Load image
img = cv2.imread(r"C:\Users\maxnd\Documents\Machine Learning\opencv-mediapipe\week2\image.jpeg")
if img is None:
    exit()


rows, cols, ch = img.shape
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

matrix=cv2.getAffineTransform(pts1,pts2)

affine=cv2.warpAffine(img,matrix,(cols,rows))


cv2.imshow("Original", img)
cv2.imshow("Affine Transform", affine)
cv2.waitKey(0)
cv2.destroyAllWindows()   