import cv2

class Elevator:
    def __init__(self, pos, totalFloor, xSize, ySize, connection=None):
        self.pos = pos
        self.totalFloor = totalFloor
        self.xSize = xSize
        self.ySize = ySize
        self.connection = connection
        if connection != None:
            self.pos = (connection.pos[0]+self.connection.radius-self.xSize/2, connection.pos[1]+connection.rope.endLen)

    def checkFloor(self): # Only checking for the y value, x is always same
        bottom = self.connection.pos[1]+self.connection.radius+self.totalFloor*self.ySize
        top = self.connection.pos[1]+self.connection.radius
        relativePos = self.pos[1]-top
        floor = round(self.totalFloor-relativePos/self.ySize, 2)
        return floor

    def draw(self, img):
        self.pos = [self.connection.pos[0]+self.connection.radius-self.xSize/2,
                    self.connection.pos[1]+self.connection.rope.endLen]
        cv2.rectangle(img, (round(self.pos[0]), round(self.pos[1])),
        (round(self.pos[0]+self.xSize), round((self.pos[1]+self.ySize))),
        (255, 0, 0))

    def drawFloors(self, img):
        cv2.line(img, (round(self.pos[0]), self.connection.pos[1]+self.connection.radius),
                      (round(self.pos[0]), self.connection.pos[1]+self.connection.radius+self.totalFloor*self.ySize), (255, 255, 255))
        cv2.line(img, (round(self.pos[0]+self.xSize), self.connection.pos[1]+self.connection.radius),
                      (round(self.pos[0]+self.xSize), self.connection.pos[1]+self.connection.radius+self.totalFloor*self.ySize), (255, 255, 255))
        for i in range(self.totalFloor+1):
            cv2.line(img, (round(self.pos[0]), self.connection.pos[1]+self.connection.radius+i*self.ySize),
                          (round(self.pos[0]+self.xSize), self.connection.pos[1]+self.connection.radius+i*self.ySize),
                          (255, 255, 255))
