import cv2
import numpy as np

img = cv2.resize(cv2.imread(r"C:\Users\Max\Documents\Projects\opencv-mediapipe\week2\image.jpeg"), (640, 480)) #Loading image
cv2.imshow("Original", img)

cv2.imshow("Blur",cv2.GaussianBlur(img,(15,15),0))
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32) #Sharpern Kernel

cv2.imshow("sharp",cv2.filter2D(img,-1,kernel))

cv2.imshow("edge",cv2.Canny(img,50,150))

cv2.waitKey(0), cv2.destroyAllWindows()

# Imagine filtering and edge detection