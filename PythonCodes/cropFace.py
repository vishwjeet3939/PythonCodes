import cv2

x=cv2.VideoCapture(0)
face=cv2.CascadeClassifier("/root/Desktop/haarcascade_frontalface_default.xml")
ret,pic=x.read()
co=face.detectMultiScale(pic)

x=co[0][0]
w=co[0][0]+co[0][2]
y=co[0][1]
h=co[0][1]+co[0][3]
cv2.rectangle(pic,(x,y),(w,h),(255,255,255),1)
cv2.imshow("hi",pic)
cv2.waitKey()
cv2.destroyAllWindows()

cropped=pic[y:h,x:w]
cv2.imshow("hi",cropped)
cv2.waitKey()
cv2.destroyAllWindows()
x.release()


