import cv2
import numpy as np

mat=np.ones((5,5),np.uint8)

img = cv2.imread("resource/people.png")
#gray color image
gray= cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#blured image
blur= cv2.GaussianBlur(img,(7,7),sigmaX=0)

#edges of image is genrated
canny=cv2.Canny(img,100,200)


#edges are incresed OR dialeated
dialate=cv2.dilate(canny,mat,iterations=1)

#edges are eroded

erode=cv2.erode(dialate,mat,iterations=1)

cv2.imshow("erode",erode)
cv2.imshow("dialtion",dialate)
cv2.imshow("image",img)
cv2.imshow("canny",canny)
cv2.imshow("gray",gray)
cv2.waitKey(0)