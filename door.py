import cv2

class Door:
    def __init__(self, connection):
        self.connection = connection
        self.posx = connection.pos[0]
        self.ySize = connection.ySize
        self.xSize = connection.xSize/2
        self.posy0 = connection.pos[1]
        self.posy1 = connection.pos[1]+self.ySize
        self.lastFloor = None
    def draw(self, img):
        self.posx = self.connection.pos[0]
        self.posy0 = self.connection.pos[1]
        self.posy1 = self.connection.pos[1]+self.ySize
        img[round(self.posy0+1):round(self.posy0+self.ySize), round(self.posx)+1: round(self.posx+self.xSize)] = (0, 255, 255)
        img[round(self.posy0+1):round(self.posy0+self.ySize), round(self.posx+self.xSize): round(self.posx+self.xSize*2)] = (0, 255, 255)

    def animate(self, image, winName):
        if self.connection.checkFloor() == self.lastFloor:
            return
        self.lastFloor = self.connection.checkFloor()
        self.posx = self.connection.pos[0]
        self.posy0 = self.connection.pos[1]
        self.posy1 = self.connection.pos[1]+self.ySize
        totalFrame = 500
        for i in range(1, totalFrame+1):
            key = cv2.waitKey(1)
            img2 = image.copy()
            img2[round(self.posy0+1):round(self.posy0+self.ySize), round(self.posx+1): round(self.posx+self.xSize)] = (0, 0, 0)
            img2[round(self.posy0+1):round(self.posy0+self.ySize), round(self.posx+self.xSize): round(self.posx+self.xSize*2+1)] = (0, 0, 0)
            img2[round(self.posy0):round(self.posy0+self.ySize), round(self.posx-(i/totalFrame)*self.xSize): round(self.posx+self.xSize-(i/totalFrame)*self.xSize)] = (0, 255, 255)
            img2[round(self.posy0):round(self.posy0+self.ySize), round(self.posx+self.xSize+(i/totalFrame)*self.xSize): round(self.posx+self.xSize*2+(i/totalFrame)*self.xSize)] = (0, 255, 255)
            cv2.imshow(winName, img2)
        for i in range(totalFrame, 0, -1):
            key = cv2.waitKey(1)
            img2 = image.copy()
            img2[round(self.posy0+1):round(self.posy0+self.ySize), round(self.posx+1): round(self.posx+self.xSize)] = (0, 0, 0)
            img2[round(self.posy0+1):round(self.posy0+self.ySize), round(self.posx+self.xSize): round(self.posx+self.xSize*2+1)] = (0, 0, 0)
            img2[round(self.posy0):round(self.posy0+self.ySize), round(self.posx-(i/totalFrame)*self.xSize): round(self.posx+self.xSize-(i/totalFrame)*self.xSize)] = (0, 255, 255)
            img2[round(self.posy0):round(self.posy0+self.ySize), round(self.posx+self.xSize+(i/totalFrame)*self.xSize): round(self.posx+self.xSize*2+(i/totalFrame)*self.xSize)] = (0, 255, 255)
            cv2.imshow(winName, img2)
