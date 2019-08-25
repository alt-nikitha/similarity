import cv2
import numpy as np
#filepath1=input()
#filepath2=input()
img1 = cv2.imread("pikachu_copy.png")
img2 = cv2.imread("pcopy.png")

w,h=img1.shape[:2]
img = np.ones((w,h,3))
count=0
for i in range(h):
    for j in range(w):
        color1=img1[i,j]
        color2=img2[i,j]
        
        p=[0,0,0]
        for k in range(3):
            if(abs(color1[k]-color2[k])<45):
                p[k]=1
        if(sum(p)>=2):
            count+=1
            img[i,j]=[0,0,0]
percentage=count/(h*w)*100
cv2.imshow("outputimg",img)
cv2.waitKey(0)
print(percentage)


