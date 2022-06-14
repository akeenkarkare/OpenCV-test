import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    #mask for blue: [90, 50, 50], [130, 255, 255]
    #mask for red: [0,50,20], [5,255,255]

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_colour = np.array([36, 25, 25]) #for green
    upper_colour = np.array([70, 255, 255]) #for green

    mask = cv2.inRange(hsv, lower_colour, upper_colour)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', result)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
