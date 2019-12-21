from pygame import*
from random import*
from math import*
init()
keys=key.get_pressed()
Right1=True
Left1=False
Right2=False
Left2=True
vy2=2
vy1=2
ONGROUND=True                             
  #tickvalue is the value in myClock.tick(value)


def punch(character,spritefile,playernumber):
    screen.blit(character+spritefile,+".png",(x+playernumber,y+playernumber))

def crouch1(x1,y1,direct,charactersymbol,playernumber):
    Rightpic=image.load(charactersymbol+"CrouchR.png" )
    Leftpic=image.load(charactersymbol+"CrouchL.png" )
    if keys[K_s] and playernumber==1:
        if direct==Right:
            screen.blit(Rightpic)
        elif direct==Left:
            screen.blit(Leftpic)
    elif keys[K_DOWN] and playernumber==2:
        if direct==Right:
            screen.blit(Rightpic)
        elif direct==Left:
            screen.blit(Leftpic)        

def crouch2(x2,y2,direct,charactersymbol,playernumber):
    Rightpic=image.load(charactersymbol+"CrouchR.png" )
    Leftpic=image.load(charactersymbol+"CrouchL.png" )
    if keys[K_s] and playernumber==1:
        if direct==Right:
            screen.blit(Rightpic)
        elif direct==Left:
            screen.blit(Leftpic)
    elif keys[K_DOWN] and playernumber==2:
        if direct==Right:
            screen.blit(Rightpic)
        elif direct==Left:
            screen.blit(Leftpic)
                

def frame(spritelist,rang,playernumber,tickvalue): #frange=rang == range! player number is either player 1 or player 2
    screen.fill((255,255,255))
    frame=0
    screen.blit(spritelist[frame],(x1,y1))
    frame+=1
    if frame== rang:
        frame=0
    myClock.tick(tickvalue)

def frame2(spritelist,rang,playernumber,tickvalue): #frange=rang == range! player number is either player 1 or player 2
    screen.fill((255,255,255))
    frame=0
    screen.blit(spritelist[frame],(x2,y2))
    frame+=1
    if frame== rang:
        frame=0
    myClock.tick(tickvalue)
    
def loadMove(foldername,frange):
    filepics=[]
    for p in range(frange):
        filepics.append(image.load((foldername)+str(p)+".png"))
    return filepics

def player1move(charname): #may need sprites in parameter
    keys=key.get_pressed()
    global ONGROUND, x1, y1, vy1
    if keys[K_d] and x1 <999:
        x1+=10
        Right2=True
        Left2=False
        
    elif keys[K_a] and x1 > 1:
        x1-=10
        Right2=False
        Left2=True
        
##    if keys[K_w] and ONGROUND==True: #if the sprite is on the ground and you press up 
##        vy1-=20
##        ONGROUND=False #as soon as he jumps, he is no longer on the ground
##        if ONGROUND==False: # if sprite is of the ground
##            y1+=vy1    
##            if y1 >= 400:
##                y1 = 400
##                vy1 = 0
##                ONGROUND=True #when the the sprite hits the floor, he is now on the ground 
##            vy1+=1.5        
   
    
def player2move(charname,sprite1,frange): #may need sprites in parameter--sprite 1 is used for testing purposes
    global ONGROUND, x2, y2, vy2
    keys=key.get_pressed()
    if keys[K_RIGHT] and x2 <999:
        x2+=10
        Right2=True
        Left2=False
        #screen.blit(testsprite(x2,y2))
        frame2(testsprite,5,2,15)
    elif keys[K_LEFT] and x2 > 1:
        x2-=10
        Right2=False
        Left2=True
        
##    if keys[K_UP] and ONGROUND==True: #if the sprite is on the ground and you press up 
##        vy2-=20
##        ONGROUND=False #as soon as he jumps, he is no longer on the ground
##        if ONGROUND==False: # if sprite is of the ground
##            y2+=vy2    
##            if y2 >= 400:
##                y2 = 400
##                vy2 = 0
##                ONGROUND=True #when the the sprite hits the floor, he is now on the ground 
##            vy2+=1.5        

def jump1():
    global ONGROUND, x1, y1, vy1
    if keys[K_w]:
        y1-=20
        ONGROUND=False
        if ONGROUND==False:
            y1+=vy1
            if y1 >= 400:
                y1 = 400
                vy1= 0
                ONGROUND=True
                move=""
            vy1+=1

        
screen = display.set_mode((1000,800))
init()
myClock = time.Clock()
running=True
x2 = 300 #starting position(middle)
y2 = 400 #
x1 = 600 #starting position(middle)
y1 = 400 #
c="circle"              
b="rcirc"

ONGROUND=True


while running:

    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False
    keys = key.get_pressed()
    ONGROUND=True
    screen.fill((255,255,255))
    
    testsprite=loadMove("runcaptright",5)
    
    if c=="circle":
        circle=draw.circle(screen,(0,255,0),(int(x2),int(y2)),10)
        player2move("circle",testsprite,5)
        if keys[K_w] or ONGROUND==False:
            jump1()
        
        
    if b=="rcirc":
        circle=draw.circle(screen,(0,0,255),(int(x1),int(y1)),10)
        player1move("rcirc")


    display.flip()
    myClock.tick(60) 
                           
    
quit()

