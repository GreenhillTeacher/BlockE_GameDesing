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
os.system('cls')
name=input("What is your name? ")
#initialize pygame
pygame.init()

#Declare constants, variables, list, dictionaries, any object
#scree size
WIDTH=700
HEIGHT=700
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Level 2')

#Declare all variables  yr game 
