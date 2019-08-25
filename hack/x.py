import cv2
img1=cv2.imread("pikachu_copy.png")
w,h=img1.shape[:2]
for i in range(3):
	for j in range(3):
		color=img1[i,j]
		print(color)
