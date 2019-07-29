



import cv2

x=cv2.VideoCapture(0)
face=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    ret,pic=x.read()
    co=face.detectMultiScale(pic)
    if len(co)>=1:
         for i in co:
		x1=co[i][0]
       		x2=co[i][0]+co[i][2]
       		y1=co[i][1]
        	y2=co[i][1]+co[i][3]
        	cv2.rectangle(pic,(x1,y1),(x2,y2),(255,255,255),1)
        cv2.imshow("hi",pic)
        if cv2.waitKey(1)==13:
            break
cv2.destroyAllWindows()
x.release()
print("Number of faces=" + len(co))

