
import cv2

cap=cv2.VideoCapture(0)

face_model=cv2.CascadeClassifier('/root/Desktop/haarcascade_frontalface_default.xml')

while True :
    ret,photo=cap.read()
    coord=face_model.detectMultiScale(photo)    
    if len(coord)>=1:       #if coord is empty and no face detected then pass
        x1=coord[0][0]
        y1=coord[0][1]
        x2=coord[0][0] + coord[0][2]
        y2=coord[0][1] + coord[0][3]
        photo =cv2.rectangle(photo,(x1,y1),(x2,y2),(255,0,0),1)    
        cv2.imshow('hi',photo)
        if cv2.waitKey(1)==13:
            break
cv2.destroyAllWindows()
cap.release()

