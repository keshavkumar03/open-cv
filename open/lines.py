import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)

img[:]=(200,250,200)

cv2.line(img,(0,0),(400,400),(100,250,200),20)
cv2.rectangle(img,(0,0),(200,300),(400,250,100),cv2.FILLED)
cv2.circle(img,(100,100),50,(200,300,400),50)
cv2.putText(img,"opencv2",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(34,40,60),3)
cv2.imshow("IMAGE",img)
cv2.waitKey(0)

