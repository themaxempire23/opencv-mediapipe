import cv2
image=cv2.imread(r"C:\Users\Max\Documents\Projects\opencv-mediapipe\week1\image.jpeg")



gray_image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

HSV_image=cv2.cvtColor(image,cv2.COLOR_RGB2HSV)

LAB_image=cv2.cvtColor(image,cv2.COLOR_RGB2Lab)


#Showing the image to the user within 4 tabs

cv2.imshow('OG image',image) 
cv2.imshow('Grayscale image',gray_image)      # 1st showing the grayscale image
cv2.imshow('HSV image',HSV_image)             # 2nd showing the HSV image
cv2.imshow('LAB image',LAB_image)             # 3rd showing the Lab image

cv2.waitKey(0)

cv2.destroyAllWindows()

