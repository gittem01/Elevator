import numpy as np
from elevator import *
from beam import *
from wheel import *

cv2.namedWindow("Elevator")
cv2.namedWindow("KeyWin")

wh = Wheel([150, 100], 6, 40)
el = Elevator([300, 300], 6, 25, 40, wh)

img = np.zeros((600, 400, 3), np.uint8)
img2 = np.zeros((300, 300, 3), np.uint8)

el.drawFloors(img)
frame = 0
while 1:
    frame += 1
    printedImg = img.copy()
    wh.turn()
    wh.draw(printedImg)
    el.draw(printedImg)

    key = cv2.waitKey(1)
    if key>0 and key<300:
        img2 = np.zeros((300, 300, 3), np.uint8)
        cv2.putText(img2, chr(key), (90,180), cv2.FONT_HERSHEY_SIMPLEX, 5, 255, 3)
    if key == ord("q"):
        break
    if key == ord("d"):
        wh.speed -= 0.001
    if key == ord("a"):
        wh.speed += 0.001
    cv2.imshow("Elevator", printedImg)
    cv2.imshow("KeyWin", img2)
