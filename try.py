"""
 * Python program to mask out everything but the wells
 * in a standardized scanned 96-well plate image, without
 * using a file with well center location.
"""
import numpy as np
import cv2
import sys
import matplotlib.pyplot as plt

image = cv2.imread(sys.argv[1])
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

h = image.shape[0]
w = image.shape[1]

kernel = np.ones((5,5), np.uint8) 
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))

_, result = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 
      
# Calcution of Sobelx 
sobelx = cv2.Sobel(result,cv2.CV_64F,1,0,ksize=5) 
  
# Calculation of Sobely 
sobely = cv2.Sobel(result,cv2.CV_64F,0,1,ksize=5) 
  
# Calculation of Laplacian 
laplacian = cv2.Laplacian(result,cv2.CV_64F) 
_, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
# show it
plt.imshow(binary, cmap="gray")
img_erosion = cv2.erode(result, kernel2, iterations=1) 
img_dilation = cv2.dilate(img_erosion, kernel2, iterations=1) 
attp = cv2.erode(img_dilation, kernel2, iterations=1) 
  
#cv2.imshow('Input', image) 
#cv2.imshow('Erosion', img_erosion) 
#cv2.imshow('Dilation', img_dilation) 
#cv2.imshow('attempt', attp)
  
#cv2.imshow('Result',result)
#cv2.waitKey(0)
cv2.imwrite(sys.argv[2],img_dilation)


#cv2.destroyAllWindows()

#img = cv2.imread(sys.argv[1])
#Z = img.reshape((-1,3))

## convert to np.float32
#Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
#criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
#K = 7
#ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
#center = np.uint8(center)
#res = center[label.flatten()]
#res2 = res.reshape((img.shape))

#cv2.imwrite(sys.argv[2],res2)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

######################3
#