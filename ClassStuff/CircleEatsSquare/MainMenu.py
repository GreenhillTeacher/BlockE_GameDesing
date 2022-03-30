#MAria Suarez
#03/23/2022
#Main Menu f the game creating funct f menu


import pygame, time,os
os.system('cls')
pygame.init()
#Variables
WIDTH=700
HEIGHT=700
xMs=50
yMs=250
wb=30
hb=30

#List f messages
MenuList=['Instructions','Settings', " ssfsdf","dasdas",'fdgdfg','asdasd','asdasd']
#Get colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
background= colors.get('white')
randColor=''
sqM_color=colors.get('pink')

#SCREEN
wind=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Circle Eats Square")

#create fifferent type 
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 30)

#Create Title
text=TITLE_FNT.render('MENU', 1, (255,0,0))
wind.fill((255,255,255))
#get the width  the text 
#x value = WIDTH/2 - wText/2
xt=WIDTH/2-text.get_width()/2
wind.blit(text,(xt,50))

#Create First button


#Create square fr menu

squareM=pygame.Rect(xMs,yMs,wb,hb)
txty=243
for i in range(7):
    message=MenuList[i]
    text=INST_FNT.render(message,1,(51,131,51))
    wind.blit(text,(90,txty))
    pygame.draw.rect(wind,sqM_color, squareM )
    squareM.y +=50
    txty+=50
pygame.display.update()
pygame.time.delay(1000)

