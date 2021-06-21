# This module is used to capture your background

import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, back = cap.read()
    if ret:
        cv2.imshow("image", back)
        if cv2.waitKey(5) == ord('q'):
#             print(ord('q'))
#saving the background image
            cv2.imwrite('image.jpg', back)
            break

cap.release()
cv2.destroyAllWindows
