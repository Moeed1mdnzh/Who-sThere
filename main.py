import os
import cv2
import json
import numpy as np
from feature_extractor import Extractor
from face_detector import FaceDetector, Drawing

cap = cv2.VideoCapture(0)
face_det = FaceDetector()
drawing = Drawing((30, 255, 30), 1)
extractor = Extractor("database.json")
extractor.load()

while True:
    _, image = cap.read()
    image = cv2.flip(image, 1)
    clone = image.copy()
    res, prob = face_det.search(image)
    if res is not None:
        if prob[0] > 0.90:
            pts = res[0]
            drawing.begin(image, pts)
            crop = clone[int(pts[1]):int(pts[3]), int(pts[0]):int(pts[2])]
            if len(crop) != 0:
                emb = face_det.extract(crop)
                try:
                    index = extractor.process(emb)
                    cv2.putText(image, index, (int(pts[0]-10), int(pts[3]+20)), cv2.FONT_HERSHEY_SIMPLEX,
                                0.7, (247, 206, 0), 2)
                except TypeError:
                    pass

    cv2.imshow("Who's There", image)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
