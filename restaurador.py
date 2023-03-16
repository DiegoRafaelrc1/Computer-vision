# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 14:28:46 2022

@author: rafae
"""
import numpy as np
import cv2

#Cargando imagen dañada
image = cv2.imread("C:/Users/rafae/OneDrive/Documentos/Projects_programming/CV/Restauracion/star3.png")
cv2.imshow("imagen",image)
cv2.waitKey(0)

#cargar foto con areas dañadas
market_damages = cv2.imread("C:/Users/rafae/OneDrive/Documentos/Projects_programming/CV/Restauracion/star3.png",0)
cv2.imshow("daños",market_damages)
cv2.waitKey(0)


"""
image = cv2.imread("C:/Users/rafae/OneDrive/Documentos/Projects_programming/CV/Restauracion/star2.png")
cv2.imshow("imagen",image)
cv2.waitKey(0)

#cargar foto con areas dañadas
market_damages = cv2.imread("C:/Users/rafae/OneDrive/Documentos/Projects_programming/CV/Restauracion/star2.png",0)
cv2.imshow("daños",market_damages)
cv2.waitKey(0)
"""



#cambiar los colores a negro todos los que no son blancos
ret ,thres1=cv2.threshold(market_damages,254,255,cv2.THRESH_BINARY)
cv2.imshow("daños",thres1)
cv2.waitKey(0)

#Hacer gruesas las marcas ya que el paso anterior las extrecho

kernel =np.ones((7,7),np.uint8)
mask = cv2.dilate(thres1,kernel,iterations=1)
cv2.imshow("mask",mask)
cv2.imwrite("Restauracion/star2_mask.png",mask)

cv2.waitKey(0)
restored = cv2.inpaint(image,mask,3,cv2.INPAINT_TELEA)

cv2.imshow("restaurada",restored)
cv2.waitKey(0)
cv2.destroyAllWindows()     
     