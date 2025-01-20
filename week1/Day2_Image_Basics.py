import cv2image
image=cv2.imread(r"C:\Users\Max\Documents\Projects\opencv-mediapipe\week1\image.jpeg")
gray_image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cv2.imshow('Grayscale image',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
