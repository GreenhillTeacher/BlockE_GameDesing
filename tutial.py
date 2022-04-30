#Katie Frymire
#4/5/22


import os, random, math,datetime, time
import pygame as p
os.system('cls')

#intailize p
p.init()

#Constants
JUMP=False
RIP=False
WIDTH=700
HEIGHT=700

#screen
screen=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("Final Project")

#characters and images
walkRight = [p.image.load('ClassStuff\CircleEatsSquare\Images\Pygame-Tutorials-master\Game\R1.png'), p.image.load('ClassStuff\CircleEatsSquare\Images\Pygame-Tutorials-master\Game\R2.png'), p.image.load('ClassStuff\CircleEatsSquare\Images\Pygame-Tutorials-master\Game\R3.png'), p.image.load('ClassStuff\CircleEatsSquare\Images\Pygame-Tutorials-master\Game\R4.png'), p.image.load('ClassStuff\CircleEatsSquare\Images\Pygame-Tutorials-master\Game\R5.png'), p.image.load('ClassStuff\CircleEatsSquare\Images\Pygame-Tutorials-master\Game\R6.png'), p.image.load('ClassStuff\CircleEatsSquare\Images\Pygame-Tutorials-master\Game\R7.png'), p.image.load('ClassStuff\CircleEatsSquare\Images\Pygame-Tutorials-master\Game\R8.png'), p.image.load('ClassStuff\CircleEatsSquare\Images\Pygame-Tutorials-master\Game\R9.png')]
walkLeft = [p.image.load('ClassStuff\CircleEatsSquare\Images\Pygame-Tutorials-master\Game\L1.png'), p.image.load('ClassStuff\CircleEatsSquare\Images\Pygame-Tutorials-master\Game\L2.png'), p.image.load('ClassStuff\CircleEatsSquare\Images\Pygame-Tutorials-master\Game\L3.png'), p.image.load('ClassStuff\CircleEatsSquare\Images\Pygame-Tutorials-master\Game\L4.png'), p.image.load('ClassStuff\CircleEatsSquare\Images\Pygame-Tutorials-master\Game\L5.png'), p.image.load('ClassStuff\CircleEatsSquare\Images\Pygame-Tutorials-master\Game\L6.png'), p.image.load('ClassStuff\CircleEatsSquare\Images\Pygame-Tutorials-master\Game\L7.png'), p.image.load('ClassStuff\CircleEatsSquare\Images\Pygame-Tutorials-master\Game\L8.png'), p.image.load('ClassStuff\CircleEatsSquare\Images\Pygame-Tutorials-master\Game\L9.png')]
biM=p.image.load('ClassStuff\CircleEatsSquare\Images\\bi mountain.jpg')
brW=p.image.load('ClassStuff\CircleEatsSquare\Images\\broke window.jpg')
chara=p.image.load("ClassStuff\CircleEatsSquare\Images\Pygame-Tutorials-master\Game\standing.png")
rip=p.image.load("ClassStuff\CircleEatsSquare\Images\RIP.jpg")
rip=p.transform.scale(rip,(50,50))
#clock
clock = p.time.Clock()
MAX=15
x=30
y=636
wc=64
hc=64
move= 5
check=True
jumpCount=MAX
left= False
right=False
walkCount=0
bg=biM
def drawWindow():
    global walkCount
    screen.blit(bg,(0,0))
    if RIP:
        screen.blit(rip,(WIDTH-100,HEIGHT-75))
        
    if walkCount + 1 >= 27:
         walkCount = 0

    if left:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount +=1
    else:
        screen.blit(chara, (x,y))
    
    p.display.update()
xm=0
ym=0

#main loop
while check:
    clock.tick(27)
    for event in p.event.get():
        if event.type == p.QUIT:
            check = False
        if event.type == p.MOUSEBUTTONDOWN:
            mse_p=p.mouse.get_pos()
            xm=mse_p[0]
            ym=mse_p[1]
    print(xm,ym)
    keys=p.key.get_pressed()
    if keys[p.K_LEFT] and x >=-14:
        x -= move
        left=True
        right=False
    elif keys[p.K_RIGHT] and x<= WIDTH-50:
        x += move
        right=True
        left=False
    else:
        left=False
        right=False
        walkCount=0
    if x>= WIDTH-50:
        bg=brW
        x=30
    if x<=10:
        bg=biM
        x=WIDTH-50
    if not JUMP:
        if keys[p.K_SPACE]:
            JUMP=True
    else:
        if jumpCount>=-MAX:
            y -= jumpCount*abs(jumpCount)/2
            jumpCount-=1
        else:
            jumpCount=MAX
            JUMP=False
        if x>520 and y>70 and y<400:
            y=HEIGHT
            RIP=True
    drawWindow()
    
    if RIP:
        p.time.delay(1000)
        print("Game er")
        check=False

