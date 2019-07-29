#!/usr/bin/env python

# In[1]:


import cv2

cap = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



while True:
    ret , photo  = cap.read()
    coord = face_detector.detectMultiScale(photo)
    if len(coord) > 0:
        i=0
        for j in coord :
            x1=coord[i][0]
            y1=coord[i][1]
            x2=coord[i][2]+x1
            y2=coord[i][3]+y1
            i=i+1
            final = cv2.rectangle(photo , (x1 , y1),(x2 , y2),(0,255,0),3)
            cv2.imshow('hi',photo)
    if cv2.waitKey(1)==13:
        break
        
cv2.destroyAllWindows()
cap.release()




