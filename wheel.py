import cv2
from beam import *
from rope import *

class Wheel:
    def __init__(self, pos, numOfBeams, radius):
        self.pos = pos
        self.numOfBeams = numOfBeams
        self.radius = radius
        self.beams = [Beam(pos, i*(math.pi/(numOfBeams/2)), radius) for i in range(1, numOfBeams+1)]
        self.speed = 0
        self.maxSpeed = 0.01
        self.rope = Rope(self)
        self.acceleration = 0

    def draw(self, img):
        cv2.circle(img, (round(self.pos[0]), round(self.pos[1])), self.radius, (255, 0, 0), 2)
        for beam in self.beams:
            beam.draw(img)
        self.rope.draw(img)
    def turn(self):
        self.speed += self.acceleration
        if self.speed > self.maxSpeed:
            self.speed = self.maxSpeed
        elif self.speed < -self.maxSpeed:
            self.speed = -self.maxSpeed
        for beam in self.beams:
            beam.angle += self.speed
        self.rope.endLen -= self.speed*self.radius
