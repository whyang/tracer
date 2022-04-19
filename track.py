# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 13:31:55 2022

@author: whyang
"""

import pygame, sys
from math import *

pygame.init()
font1 = pygame.font.SysFont('microsoftyaheimicrosoftyaheiui', 23)
textc = font1.render('*', True, (0, 255, 0))
screen = pygame.display.set_mode((800, 700), 0, 32)
missile = pygame.image.load('rect1.png').convert_alpha()
height = missile.get_height()
width = missile.get_width()
pygame.mouse.set_visible(0)
x1, y1 = 100, 600 #導彈的初始發射位置
velocity = 800 #導彈速度
time = 1 / 1000 #每個時間片的長度
clock=pygame.time.Clock()
A=()
B=()
C=()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #pygame.quit()
            #sys.exit()
        clock.tick(300)
        x, y = pygame.mouse.get_pos() #獲取滑鼠位置，滑鼠就是需要打擊的目標
        distance = sqrt(pow(x1 - x, 2) + pow(y1 - y, 2)) #兩點距離公式
        section = velocity * time #每個時間片需要移動的距離
        sina = (y1 - y) / distance
        cosa = (x - x1) / distance
        angle = atan2(y - y1, x - x1) #兩點間線段的弧度值
        fangle = degrees(angle) #弧度轉角度
        x1, y1 = (x1 + section * cosa, y1 - section * sina)
        missiled = pygame.transform.rotate(missile, -(fangle))
        if 0 <= -fangle <= 90:
            A = (width*cosa+x1-width, y1-height/2)
            B = (A[0]+height*sina, A[1]+height*cosa)
        if 90 < -fangle <= 180:
            A = (x1 - width, y1 - height / 2 + height * (-cosa))
            B = (x1 - width + height * sina, y1 - height / 2)
        if -90 <= -fangle < 0:
            A = (x1 - width + missiled.get_width(), y1 - height / 2 + missiled.get_height() - height * cosa)
            B = (A[0] + height * sina, y1 - height / 2 + missiled.get_height())
        if -180 < -fangle < -90:
            A = (x1 - width - height * sina, y1 - height / 2 + missiled.get_height())
            B = (x1 - width, A[1] + height * cosa)
            C = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
        screen.fill((0, 0, 0))
        screen.blit(missiled, (x, y)) #(x1-width+(x1-C[0]), y1-height/2+(y1-C[1])))
        screen.blit(textc, (x, y)) #滑鼠用一個紅色*代替
        pygame.display.update()

pygame.quit()
sys.exit()