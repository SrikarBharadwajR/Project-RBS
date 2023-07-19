from queue import Empty
import cv2 
import numpy as np

cap = cv2.VideoCapture(0)

cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H", "Trackbars", 0, 180, Empty)
cv2.createTrackbar("L-S", "Trackbars", 0, 255,Empty)
cv2.createTrackbar("L-V", "Trackbars", 0, 255,Empty)
cv2.createTrackbar("U-H", "Trackbars", 180, 255,Empty)
cv2.createTrackbar("U-S", "Trackbars", 255, 255,Empty)
cv2.createTrackbar("U-V", "Trackbars", 255, 255,Empty)

while True:
    ret,frame = cap.read()
    
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("L-H", "Trackbars")
    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    l_v = cv2.getTrackbarPos("L-V", "Trackbars")
    u_h = cv2.getTrackbarPos("U-H", "Trackbars")
    u_s = cv2.getTrackbarPos("U-S", "Trackbars")
    u_v = cv2.getTrackbarPos("U-V", "Trackbars")
    
    lower_red = np.array([l_h, l_s, l_v])
    upper_red = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(color, lower_red, upper_red)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow('frame' , result)
    
    k=cv2.waitKey(1) 
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()