import cv2

img=cv2.imread("resource/people.png")
resize=cv2.resize(img,(300,200))
crop=img[0:200,100:400]

print(img.shape)
cv2.imshow("output",img)
cv2.imshow("resixe",resize)
cv2.imshow("crop",crop)
cv2.waitKey(0)