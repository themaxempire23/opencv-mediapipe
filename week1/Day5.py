import cv2

vid=cv2.VideoCapture(0)

while True:
    net,frame=vid.read()
    cv2.imshow("frame",frame)

    if cv2.waitKey(1)==ord('h'):
        break

vid.release()
cv2.destroyAllWindows()