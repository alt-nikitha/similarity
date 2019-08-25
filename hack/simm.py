import cv2
import numpy as np
def dist(xa,ya,za,xb,yb,zb):
    dist = np.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb)+(za-zb)*(za-zb))
    return dist
#f1 is the first image
#f2 is the second image
img1 = cv2.imread("f1.png")
img20 = cv2.imread("f2.png")
h1,w1=img1.shape[:2]
#w2,h2=img20.shape[:2]
#if(w1>w2):
#    w=w1
#else:
#    w=w2
#if(h1>h2):
#    h=h1
#else:
#    h=h2


img2=cv2.resize(img20,(w1,h1))
#print(img2.shape,img1.shape)
img = np.zeros((h1,w1,3))
count=0
for i in range(h1):
    for j in range(w1):
        color1=img1[i,j]
        color2=img2[i,j]

#         p=[0,0,0]
#        for k in range(3):
#            if(abs(color1[k]-color2[k])<20):
#                p[k]=1
#        if(sum(p)>=2):
        d=dist(color1[0],color1[1],color1[2],color2[0],color2[1],color2[2])
        if(d<0.2):
            count+=1
            img[i,j]=[0,255,0]
        elif(d<0.4):
            count+=1
            img[i,j]=[255,0,0]
        elif(d<0.6):
            count+=1
            img[i,j]=[0,0,255]



percentage=count/(h1*w1)*100
print(percentage)
cv2.imshow("outputimg",img)
cv2.waitKey(0)



