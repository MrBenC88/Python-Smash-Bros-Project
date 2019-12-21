#gametestfun.py
# THIS is just a demo alpha version of our project

# PATCH
    #start match function not working--

    ###### IMPORTANT--gravity needs TO BE FIXED Line--388-436 !!!!! 
   


#___________________________________________________________________________________
from pygame import*
from random import*
from math import*

screen=display.set_mode((1000,800))
init()
myClock=time.Clock()
init()   #must have for font
arialFontstart = font.SysFont("Times New Roman", 60)
arialFont2 = font.SysFont("Times New Roman", 70)
background=image.load("MAINMENUselectNONE.png")
screen.blit(background,(0,0))

advRect=Rect(46,237,142,33)
trainRect=Rect(46,309,142,33)
pvpRect=Rect(46,377,142,33)
optionRect=Rect(46,450,142,33)
controlRect=Rect(46,523,142,33)

advpic=image.load("MAINMENUselectadventure.png")
trainpic=image.load("MAINMENUselecttraining.png")
pvppic=image.load("MAINMENUselectPvP.png")
optionpic=image.load("MAINMENUselectoptions.png")
controlpic=image.load("MAINMENUselectcontrols.png")
            
running=True

while running:

    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False
    keys = key.get_pressed()
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    if advRect.collidepoint(mx,my):
        screen.blit(advpic,(0,0))
        if mb[0]==1:
            import adventure
    elif trainRect.collidepoint(mx,my):
        screen.blit(trainpic,(0,0))
    elif pvpRect.collidepoint(mx,my):
        screen.blit(pvppic,(0,0))
        if mb[0]==1:
            import gametestfun
    elif optionRect.collidepoint(mx,my):
        screen.blit(optionpic,(0,0))
    elif controlRect.collidepoint(mx,my):
        screen.blit(controlpic,(0,0))        
    else:
        screen.blit(background,(0,0))
        

    
    

    display.flip()
    myClock.tick(60)
    

quit()
