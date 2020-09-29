import numpy as np
import cv2
import time

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)

time.sleep(2)
background = 0

for i in range(30):
    ret, background = cam.read()
    
while(cam.isOpened()):
    
    ret, img = cam.read()
    
    if ret == False:
        break
        
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    loweryellow = np.array([0,120,70])
    upperyellow = np.array([10,255,255])
    mask1 = cv2.inRange(hsv , loweryellow , upperyellow)
    
    loweryellow = np.array([170,120,70])
    upperyellow = np.array([180,255,255])
    mask2 = cv2.inRange(hsv , loweryellow , upperyellow)
    
    mask1 = mask1 + mask2 

    mask2 = cv2.bitwise_not(mask1)
    
    res1 = cv2.bitwise_and(background, background, mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)
    
    final_output = cv2.addWeighted(res1 , 1, res2 , 1, 0)
    
    cv2.imshow('Invisible' , final_output)
    k=cv2.waitKey(10)
    if k==27:
        break
        
cam.release()
cv2.destroyAllWindows()