import numpy as np
from elevator import *
from beam import *
from wheel import *

wh = Wheel([150, 100], 6, 50)

el = Elevator([300, 300], 10, 50, 80, wh)

img = np.zeros((600, 400, 3), np.uint8)

while 1:
    printedImg = img.copy()
    wh.turn()
    wh.draw(printedImg)
    el.draw(printedImg)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    if key == ord("d"):
        wh.speed -= 0.001
    if key == ord("a"):
        wh.speed += 0.001
    cv2.imshow("Elevator", printedImg)
