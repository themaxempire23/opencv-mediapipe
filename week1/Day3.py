# Basic Image Operations

import cv2
image=cv2.imread(r"C:\Users\Max\Documents\Projects\opencv-mediapipe\week1\image.jpeg")
image1=cv2.imread(r"C:\Users\Max\Documents\Projects\opencv-mediapipe\week1\image1.jpeg")

# Resising Image
image=cv2.resize(image,(500,500))
image1=cv2.resize(image1,(500,500))

#alpha weight of 1st image
#beta weight of 2nd image

alpha=0.7
beta=0.3


Blend=cv2.addWeighted(image,alpha,image1,beta,0)

# function to show the image
cv2.imshow("Blended image",Blend)

cv2.waitKey(0)
