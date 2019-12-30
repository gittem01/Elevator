import cv2
import math

class Beam:
    def __init__(self, pos, angle, length):
        self.pos = pos
        self.angle = angle
        self.length = length
    def draw(self, img):
        startPos = (round(self.pos[0]),round(self.pos[1]))
        endPos = (round(self.pos[0]+self.length*math.cos(self.angle)),
                  round(self.pos[1]-self.length*math.sin(self.angle)))
        cv2.line(img, startPos, endPos, (255, 0, 0))
        cv2.circle(img, endPos, 2, (0, 0, 255), -1)
