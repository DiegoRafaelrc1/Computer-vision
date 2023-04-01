# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 21:36:40 2022

@author: rafae
"""

import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier("Harcast/haarcascade_frontalface_default.xml")
eye_classifier = cv2.CascadeClassifier("Harcast/haarcascade_eye.xml")

def face_detector(img,sixe=0.5):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray , 1.3 ,5)
    if faces ==():
        return img
    
    for (x,y,w,h) in faces:
     x=x-50
     w=w+50
     y=y-50
     h=h+50
     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
     roi_gray =gray[y:y+h,x:x+w]
     roi_color = img[y:y+h,x:x+w]
     eyes= eye_classifier.detectMultiScale(roi_gray)
     for (ex,ey,ew,eh) in eyes:
       cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)
       
    roi_color = cv2.flip(roi_color,1)
    return roi_color

cap= cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    cv2.imshow("Estract ",face_detector(frame))
    if cv2.waitKey(1)== 13:# es la tecla enter
        break
    
cap.release()
cv2.destroyAllWindows()          