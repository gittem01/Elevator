import cv2

class Elevator:
    def __init__(self, pos, totalFloor, xSize, ySize, connection=None):
        self.pos = pos
        self.totalFloor = totalFloor
        self.xSize = xSize
        self.ySize = ySize
        self.connection = connection
        if connection != None:
            self.pos = (connection.pos[0]+xSize/2, connection.pos[1]+connection.rope.endLen)

    def draw(self, img):

        self.pos = [self.connection.pos[0]+self.xSize/2, self.connection.pos[1]+self.connection.rope.endLen]
        if self.connection.rope.endLen<self.connection.radius:
            self.pos[1] = self.connection.pos[1]+self.connection.radius
        cv2.rectangle(img, (round(self.pos[0]), round(self.pos[1])),
        (round(self.pos[0]+self.xSize), round((self.pos[1]+self.ySize))),
        (255, 255, 255))
