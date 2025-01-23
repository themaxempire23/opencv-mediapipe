import cv2
import numpy as np

def draw_shapes_and_text():
    # Creating blank image
    #img = np.zeros((500, 800, 3), dtype=np.uint8) # declaring img variable followed an entry of zeros

    # If I want to change the image
    img=cv2.imread(r"C:\Users\Max\Documents\Projects\opencv-mediapipe\week1\image.jpeg")

    cv2.line(img, (50, 50),( 500, 100),(0, 255, 0), 5)
    cv2.rectangle(img, (50, 50),( 500, 100),(0, 255, 0), 5)
    cv2.circle(img,(50,50),50,(255, 0,255),5)

    font=cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img,"Opencv Professional certificate",(100,200),font,1,(255,255,255),2)

    cv2.imshow("Drawn_image", img)
    cv2.waitKey(0)


    cv2.imshow("Edit",img)
    cv2.waitKey(0)

draw_shapes_and_text()