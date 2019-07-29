import requests
import numpy
import cv2

while True:
    url="http://mobileIp/shot.jpg"
    data=requests.get(url)
    photo=data.content
    myphoto=bytearray(photo)
    my=numpy.array(myphoto)
    pic=cv2.imdecode(my,-1)   #-1 for converting into 3d array
    cv2.imshow("hi",pic)
    if cv2.waitKey(1)==13:
        break
cv2.destroyAllWindows()
