import cv2image
image=cv2.imread(r"C:\Users\Max\Documents\Projects\opencv-mediapipe\week1\image.jpeg")
gray_image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

cv2.destroyAllWindows()

HSV_image=cv2.cvtColor(image,cv2.COLOR_RGB2HSV)

LAB_image=cv2.cvtColor(image,cv2.COLOR_RGB2Lab)

#Showing the image to the user within 4 tabs

# 1st showing the grayscale image
cv2.imshow('Grayscale image',gray_image)
cv2.waitKey(0)


# 2nd showing the HSV image
cv2.imshow('HSV image',HSV_image)
cv2.waitKey(0)


# 3rd showing the Lab image
cv2.imshow('LAB image',LAB_image)
cv2.waitKey(0)



