# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 20:32:04 2022

@author: jina
"""

import cv2
import pygame

def set_ball(screen,ball,core):
    screen.blit(ball,core)
    pygame.display.update()

def proccess_img(camara):
    ref,img=camara.read()
    face = cv2.CascadeClassifier(r"D:\app data\anaconda\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml")
    settings = {
        'scaleFactor': 1.3, 
        'minNeighbors': 3, 
        'minSize': (50, 50), 
    }
    img=cv2.flip(img, 1)
    detected=face.detectMultiScale(img,**settings)
    if len(detected)!=0:
        for fx,fy,fw,fh in detected:
            core=(int(fx+fw/2),int(fy+fh/2))
            return core
    else:
        return 0
            
    
        
if __name__=="__main__":
    camara=cv2.VideoCapture(0)
    pygame.init()
    white=(255,255,255)
    ball=pygame.image.load(r"C:\Users\jina\Desktop\desktop files\img2.png")
    screen= pygame.display.set_mode((800,600))
    clock=pygame.time.Clock()
    fps=300
    running=1
    while running:
        event = pygame.event.get()
        if(event is not None):
            #返回一个元组，里面是一堆bool数据
            pressed = pygame.key.get_pressed()
            #pygame.K_q表示q的常量113，按下pressed里面对应的值变成1，用来退出
            if(pressed[pygame.K_q]):
                running = False
        
        if cv2.waitKey(5) == 113:
            camara.release()
            cv2.destroyAllWindows()
            break
        screen.fill(white)
        core=proccess_img(camara)
        if core!=0:
            set_ball(screen,ball,core)
        else:
            print("no face")
        clock.tick(fps)
    cv2.destroyAllWindows()
    camara.release()
    pygame.quit()
    
        
   
        
        