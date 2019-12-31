import numpy as np
import time
import random
from elevator import *
from beam import *
from wheel import *

cv2.namedWindow("Elevator")
cv2.namedWindow("KeyWin")

wh = Wheel([150, 100], 6, 40)
el = Elevator([300, 300], 9, 25, 40, wh)

slice = int((el.totalFloor+1)/2)
req = 1

img = np.zeros((600, 400, 3), np.uint8)
img2 = np.zeros((600, 300, 3), np.uint8)

sh0 = img2.shape[0]
sh1 = img2.shape[1]
for i in range(1, slice):
    cv2.line(img2, (0, round(sh0/slice)*i), (sh1, round(sh0/slice)*i), (255, 255, 255))
cv2.line(img2, (round(sh1/2), 0), (round(sh1/2), sh0), (266, 255, 255))

for i in range(1, el.totalFloor+1):
    cv2.putText(img2, str(el.totalFloor-i+1),(((i+1)%2)*round(sh1/2)+30, ((i+1)//2)*round(sh0/slice)-20),
                cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 1, cv2.LINE_AA)

def ClickPos(event, x, y, flags, param):
    global req, status
    if event == cv2.EVENT_LBUTTONDOWN:
        if status == "On move":
            return
        req = el.totalFloor - int((y/sh0)*slice)*2 - int((x/sh1)*2)
cv2.setMouseCallback("KeyWin", ClickPos)

el.drawFloors(img)
frame = -1
status = None
while 1:
    frame += 1
    printedImg = img.copy()
    wh.turn()

    floor = el.checkFloor()
    if floor<1 or floor>el.totalFloor:
        break

    status = el.goReq(req)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    if key == ord("d"):
        wh.acceleration = -1
    if key == ord("a"):
        wh.acceleration = 1

    wh.draw(printedImg)
    el.draw(printedImg)
    cv2.imshow("Elevator", printedImg)
    cv2.imshow("KeyWin", img2)
