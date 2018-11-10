
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import imutils
def detect(c): 
  shape = "unidentified"
  peri = cv2.arcLength(c, True)
  approx = cv2.approxPolyDP(c, 0.015 * peri, True)
  if len(approx) == 3:
      shape = "ujgen"

  elif len(approx) == 4:
      (a,b,d,e)= cv2.boundingRect(approx)
      ar = d / float(e)
      shape = "sungerbob" if ar >=0.95 and ar <1.05 else "durtgen"

  elif len(approx) == 5:    
      shape = "bejgen"

  elif len(approx) == 6:
      shape = "atligen"

  elif len(approx) == 8:
      shape = "zekizgen"

  elif len(approx) == 10:
      shape = "ongen"
       
  else :
      shape = "dayre"

    
  return shape  

img = cv2.imread('2.jpeg',1)
resized = imutils.resize(img, width=350)
ratio = img.shape[0] /float(resized.shape[0])

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
thresh= cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)[1]

sigma = 0.33
v = np.median(img)
low = int(max(0, (1.0 - sigma) * v))
high = int(min(255, (1.0 + sigma) * v))

edges = cv2.Canny(resized, low, high)

cnts= cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnts= cnts[0] if imutils.is_cv2()  else cnts[1]                  

for c in cnts:

    M = cv2.moments(c)
    cX = int((M["m10"] / (M["m00"]+0.011)) * ratio)
    cY = int((M["m01"] / (M["m00"]+0.011)) * ratio)
    shape = detect(c)             
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")
    cv2.drawContours(img, [c], 0, (255, 0, 255), 2)
    cv2.putText(img, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255,0 ), 2)
    
      
cv2.imshow("asd", img)
#cv2.imshow("aswd", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
    



  







