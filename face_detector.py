import cv2
import numpy as np
from PIL import Image
from facenet_pytorch import MTCNN, InceptionResnetV1

class FaceDetector:
    def __init__(self, im_size=160):
        self.mtcnn = MTCNN(keep_all=True)
        self.model = InceptionResnetV1(pretrained="vggface2").eval()
        
    def _utilize(self, im):
        return Image.fromarray(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
    
    def _detect(self, im):
        return self.mtcnn.detect(im)
    
    def search(self, im):
        im_modified = self._utilize(im)
        res = self._detect(im_modified)
        return res
    
class Drawing:
    def __init__(self, color, thickness):
        self.color = color 
        self.thickness = thickness 
        
    def _draw_1(self, pts, im):
        pts_1 = np.array([[pts[0]+15, pts[1]], [pts[0], pts[1]], [pts[0], pts[1]+15],], np.int32)
        pts_1 = pts_1.reshape((-1, 1, 2))
        cv2.polylines(im, [pts_1], False, (30, 255, 30), 1)
    
    def _draw_2(self, pts, im):
        pts_2 = np.array([[pts[2]-15, pts[1]], [pts[2], pts[1]], [pts[2], pts[1]+15],], np.int32)
        pts_2 = pts_2.reshape((-1, 1, 2))
        cv2.polylines(im, [pts_2], False, (30, 255, 30), 1)
    
    def _draw_3(self, pts, im):
        pts_3 = np.array([[pts[0]+15, pts[3]], [pts[0], pts[3]], [pts[0], pts[3]-15],], np.int32)
        pts_3 = pts_3.reshape((-1, 1, 2))
        cv2.polylines(im, [pts_3], False, (30, 255, 30), 1)
    
    def _draw_4(self, pts, im):
        pts_4 = np.array([[pts[2]-15, pts[3]], [pts[2], pts[3]], [pts[2], pts[3]-15],], np.int32)
        pts_4 = pts_4.reshape((-1, 1, 2))
        cv2.polylines(im, [pts_4], False, (30, 255, 30), 1)
    
    def begin(self, im, pts):
        pts = (int(pts[0]), int(pts[1]), int(pts[2]), int(pts[3]))
        self._draw_1(pts, im)
        self._draw_2(pts, im)
        self._draw_3(pts, im)
        self._draw_4(pts, im)