import cv2
import numpy as np


cap = cv2.VideoCapture(0)
back = cv2.imread('./image.jpg')

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # cv2.imshow("hsv", hsv)

        colr = np.uint8([[[0, 0, 255]]])  # bgr->red color
        # get hsv value of red from bgr
        hsv_colr = cv2.cvtColor(colr, cv2.COLOR_BGR2HSV)
        print(hsv_colr)
        # range for substitution -> l(hue-10,100,100), h(hue+10,255,255)
        l_red = np.array([0, 100, 100])
        u_red = np.array([10, 255, 255])

        mask = cv2.inRange(hsv, l_red, u_red)
        # cv2.imshow("mask", mask)

        # only red part visible (i.e. background where red color is in frame)
        part1 = cv2.bitwise_and(back, back, mask=mask)
        # cv2.imshow("part1", part1)

        mask = cv2.bitwise_not(mask)

        # other than red part visible (i.e. all frame except red)
        part2 = cv2.bitwise_and(frame, frame, mask=mask)
        # cv2.imshow("part2", part2)

        cv2.imshow("cloak", part1+part2)

        if cv2.waitKey(5) == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()
