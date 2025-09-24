import pyautogui
from ultralytics import YOLO
from PIL import ImageGrab
import numpy as np
import matplotlib.pyplot as plt
import time
import cv2 
import random

model = YOLO(r"D:\workspace\scripts\best.pt")
class_names = model.names

def withWait(func,wait_dur = 0.2):
    while True:
        func()
        time.sleep(wait_dur)
        # break

def loop():
    screen = ImageGrab.grab()
    frame = np.array(screen)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # result = model.predict(source=frame , show=True)[0]  
    result = model.predict(source=frame )[0]  
    boxes = result.boxes
    
    # checking for play button
    for box in boxes:
        if(class_names[int(box.cls[0])] == "play"):
            x1,y1,x2,y2 = box.xyxy[0]
            x = (x1+x2)/2
            y = (y1+y2)/2
            pyautogui.click(x , y)
            return 
    boxes = list(boxes)
    random.shuffle(boxes)
    for box in boxes:
        if(class_names[int(box.cls[0])] == "Mole"):
            x1,y1,x2,y2 = box.xyxy[0]
            x = (x1+x2)/2
            y = (y1+y2)/2
            pyautogui.click(x , y)
        
withWait(loop , 0)

# while True:
#     break