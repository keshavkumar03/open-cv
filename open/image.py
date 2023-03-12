import cv2
import numpy as np

# Load image file
img = cv2.imread('resource/people.png')
arr=np.array(img)

# Check if img is a numpy array
print(arr)

 #Display image using cv2.imshow
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

