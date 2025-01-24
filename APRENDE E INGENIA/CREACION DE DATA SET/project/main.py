import torch
import cv2
import os
import numpy as np
import pandas

current_directory = os.getcwd()

#Leer modelo
model = torch.hub.load('ultralytics/yolov5', 'custom', path=f'{current_directory}/APRENDE E INGENIA/CREACION DE DATA SET/project/models/best.pt')

#model = torch.hub.load('ultralytics/yolov5', 'custom', path=f'{current_directory}/APRENDE E INGENIA/CREACION DE DATA SET/project/models/last.pt')

cap = cv2.VideoCapture(0)

while True:
    #Lectura de frames
    ret, frame = cap.read()
    
    # Guardar la informacion del objeto
    info = detect.pandas().xyxy[0]
    print(info)
    
    #realizar deteccciones
    detect = model(frame)
    
    #mostrar fps
    cv2.imshow('detector de balones', np.squeeze(detect.render()))
    
    #cerrar con teclado
    exit = cv2.waitKey(5)
    if exit == 27:
        break
cap.relase()
cv2.destroyAllWindows()  #cerrar todas las ventanas