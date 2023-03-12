import cv2
import numpy as np

img=cv2.imread("resource/people.png")

width,height=(700,400)

pt1= np.float32([[150,360],[0,490],[190,650],[320,450]])
pt2= np.float32([[0,0],[0,height],[width,0],[width,height]])
mat=cv2.getPerspectiveTransform(pt1,pt2)

newimg=cv2.warpPerspective(img,mat,(width,height))

cv2.imshow("image",newimg)
cv2.waitKey(0)
cv2.destroyAllWindows