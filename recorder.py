import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, image = cap.read()
    image = cv2.flip(image, 1)
    cv2.imshow("Who's There", image)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break 
    
cap.release()
cv2.destroyAllWindows()