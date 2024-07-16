import os
import cv2
import numpy as np
from database_config import Database
from face_detector import FaceDetector, Drawing

cap = cv2.VideoCapture(0)
face_det = FaceDetector()
drawing = Drawing((30, 255, 30), 1)
db = Database("database.json")

while True:
    _, image = cap.read()
    image = cv2.flip(image, 1)
    clone = image.copy()
    res, prob = face_det.search(image)
    if res is not None:
        if prob[0] > 0.90:
            pts = res[0]
            drawing.begin(image, pts)
            key = cv2.waitKey(1)
            if key == ord("c"):
                crop = clone[int(pts[1]):int(pts[3]), int(pts[0]):int(pts[2])]
                break
                               
            # cv2.rectangle(image, (pts[0], pts[1]), (pts[2], pts[3]), (100, 255, 100), 2)
            # cv2.putText(image, str(prob[i])[:8], (pts[0], pts[3]+20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (50, 50, 255), 2)

    cv2.imshow("Who's There", image)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break 
    
cap.release()
cv2.destroyAllWindows()

name = input("Enter your name --> ")
key = db.add(name)
cv2.imwrite(os.sep.join(["images", key])+".jpg", crop)
