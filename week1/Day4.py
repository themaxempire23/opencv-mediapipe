import cv2
import numpy as np

def draw_shapes_and_text():
    # Creating blank image
    img = np.zeros((500, 800, 3), dtype=np.uint8) # declaring img variable followed an entry of zeros

    cv2.line(img, (50, 50),( 500, 100),(0, 255, 0), 5)
    cv2.rectangle(img, (50, 50),( 500, 100),(0, 255, 0), 5)

    cv2.imshow("Edit",img)
    cv2.waitKey(0)

draw_shapes_and_text()