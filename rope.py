import cv2

class Rope:
    def __init__(self, connection, endLen=100):
        self.connection = connection
        self.endLen = endLen
    def draw(self, img):
        if self.endLen<0:
            return
        p = self.connection.pos
        cv2.line(img, (round(p[0]+self.connection.radius), round(p[1])),
         (round(p[0]+self.connection.radius), round(p[1]+self.endLen)), (255, 0, 0))
