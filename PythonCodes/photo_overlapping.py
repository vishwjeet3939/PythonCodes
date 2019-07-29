import cv2
x=cv2.VideoCapture(0)
ret,pic=x.read()
ret1,pic1=x.read()

pic = cv2.imread("pic.png")
pic1=cv2.imread("pic1.png")

cv2.imwrite("pic.png",pic)
cv2.imwrite("pic1.png",pic1)

pic1[0:100,0:100]=pic[200:300,300:400]

cv2.imshow("hi",pic1)
cv2.waitKey()
cv2.destroyAllWindows()

