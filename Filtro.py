import math 
import cv2
import numpy as n
im=cv2.imread('plantilla.jpg',0)
i=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

template = cv2.imread("MS6.jpg",0)
w, h = template.shape[::-1]
methods = ['cv2.TM_CCORR_NORMED']
for meth in methods:
    method = eval(meth)
res = cv2.matchTemplate(i,template,method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)


p=i
img=i[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0]]
print(top_left[1],bottom_right[1],top_left[0],bottom_right[0])
cv2.imshow('Hola',p)

if (cv2.waitKey(1) & 0xFF==ord('q')):
                                cv2.imwrite("MS.jpg",p)

                                cv2.destroyAllWindows()
                                break 
