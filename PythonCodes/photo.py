#!/usr/bin/python36
import cv2
import os
cap=cv2.VideoCapture(0)
ret,photo = cap.read()
cv2.imwrite("/root/Desktop/menu.png", photo)
cap.release()

