#MAria I SUarez
#learning how to draw circles and rectangles
#use keys to move objects
#Using Dictionaries

#Objective of the game is for the rect to run away fom the circle, if they collide the circle etas the square, 
#circle will  get larger, and a new rect should appear somewhere on the screen
# K_UP                  up circle
# K_DOWN                down circle
# K_RIGHT               right circle
# K_LEFT                left circle
# K_a                   left square
# K_d                   right square
# K_w                   up square
# K_s                   down square
# K_SPACE               jump
#initialize pygame

import os, random, time, pygame, math, datetime
from numpy import character
os.system('cls')

#initialize pygame
pygame.init()

#Declare constants, variables, list, dictionaries, any object
#scree size
WIDTH=700
HEIGHT=700
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('LEVEL II')
bg=pygame.image.load('ClassStuff\CircleEatsSquare\Images\\bgSmaller.jpg')
chart=pygame.image.load('ClassStuff\CircleEatsSquare\Images\Pygame-Tutorials-master\Game\standing.png')

pygame.display.update()
move=5
check=True
x=200
y=200
while check:
    screen.blit(bg,(0,0))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            check=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= move
    if keys[pygame.K_RIGHT] :
        x += move
    if keys[pygame.K_DOWN] :
        y += move
    if keys[pygame.K_UP] :
        y -= move
    screen.blit(chart,(x,y))
    pygame.display.update()


