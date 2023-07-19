import cv2
import numpy as np


cam = cv2.VideoCapture(0)

while True:
    _,frame= cam.read()
    
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
    lower_orng = np.array([6, 147, 120])
    upper_orng = np.array([10, 255, 255])
    mask = cv2.inRange(color, lower_orng, upper_orng)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>1000:
         cv2.drawContours(frame, [cnt], 0, (0,0,0), 3)
        
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    
    k=cv2.waitKey(1)
    if k == ord('q'):
        break
    
cv2.destroyAllWindows()
