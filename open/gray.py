import cv2

img = cv2.imread('resource/people.png')

gray_img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("output",gray_img)
cv2.waitKey(0)