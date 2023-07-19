import cv2 
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([93  ,40 ,200])
    upper_blue = np.array([113 , 60, 280])
    mask = cv2.inRange(color, lower_blue, upper_blue)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow('result' , result)
    cv2.imshow('frame' , color)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()