import cv2
import numpy as np

def binary_image(image_path=r"C:\Users\Max\Documents\Projects\opencv-mediapipe\week1\image.jpeg"):

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    _, simple_thresh = cv2.threshold(image, 127, cv2.THRESH_BINARY)

    adapative_mean = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    adapative_gaussian = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    _, otsu_thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    cv2.imshow("simple_thresh", simple_thresh)
    cv2.imshow("Adap_mean", adaptive_mean)
    cv2.imshow("Adap_gauss", simple_gaussian)
    cv2.imshow("otsu_thresh", otsu_thresh_thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    binary_image()