#gametestfun.py
# THIS is just a demo alpha version of our project

#___________________________________________________________________________________
from pygame import*
from random import*
from math import*

screen=display.set_mode((1000,800))
init()
myClock=time.Clock()
init()   #must have for font
arialFontstart = font.SysFont("Times New Roman", 50)
arialFont2 = font.SysFont("Times New Roman", 70)
damagep1=0
damagep2=0
damagerect1=Rect(300,700,100,100)
damagerect2=Rect(600,700,100,100)
replayrect=Rect(400,500,200,100)
txtPosStartRect=Rect(500,300,30,30)
colour=((0,0,0))
colour2=((0,0,0))
red=((255,0,0))
blue=((0,0,255))

##def startmatch():
##    for i in range(4):
##        myClock.tick(5)

##        txtPosStart=arialFontstart.render(str(i-1),True,(0,0,0))
##        screen.blit(txtPosStart,txtPosStartRect)
##        break
    
def damagedisplay():
    global txtPos,txtPos1, colour, colour2
    txtPos=arialFont2.render(str(damagep1),True,(colour))
    txtPos2=arialFont2.render(str(damagep2),True,(colour2))
    screen.blit(txtPos2,damagerect2)
    screen.blit(txtPos,damagerect1)
    


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

def walk(direction):
    global x1,y1,frame
    keys=key.get_pressed()
    if keys[K_d]:
        direction = "right"
        x1+=10

    if keys[K_a]:
        direction = "left"
        x1-=10

def walk2(direction2):
    global x2,y2,frame
    keys=key.get_pressed()
    if keys[K_RIGHT]:
        direction2 = "right"
        x2+=10


    if keys[K_LEFT]:
        direction2 = "left"
        x2-=10




running=True
ONGROUND=True
ONGROUND2=True
x1=300
y1=400

x2=700
y2=400

vy1=2
vy2=2
frame=0
damage1=0
damage2=0

player="Captian Falcon"

player2="fox"
direction=""
direction2=""
if x1==300:
    direction="right"

if x2==700:
    direction2="left"
move=""
move2=""
while running:
    
    dis1=((x1-x2)**2+(y1-y2)**2)**.5
    dis2=((x1-x2)**2+(y1-y2)**2)**.5
    ONGROUND=True
    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False
    keys = key.get_pressed()
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    #startmatch()
    screen.fill((255,255,255))
    damagedisplay()
    colour=((0,0,0))
    colour2=((0,0,0))
    
    if player=="Captian Falcon":
        if  keys[K_d] or keys[K_a]:
            walk(direction)
        if keys[K_w] or ONGROUND==False:
            move="jump"      
        


    if move=="jump":
        y1-=20
        ONGROUND=False
        if ONGROUND==False: # if sprite is of the ground
            y1+=vy1    
            if y1 >= 400:
                y1 = 400
                vy1= 0
                ONGROUND=True
                move=""
            vy1+=1

    circle=draw.circle(screen,(0,255,0),(x1,int(y1)),10)

    if keys[K_SPACE] and dis1<=80:
        damage1=1
        myClock.tick(15)
        
    if keys[K_KP1] and dis2<=80:
        damage2=1
        myClock.tick(15)
        
#----------------------------------------------------------------------------------

    if player2=="fox":
        if keys[K_LEFT] or keys[K_RIGHT]:
            walk2(direction2)
        if keys[K_UP] or ONGROUND2==False:
                move2="jump"

        
            
    if move2=="jump":
        y2-=20
        ONGROUND2=False
        if ONGROUND2==False: # if sprite is of the ground
            y2+=vy2    
            if y2 >= 400:
                y2 = 400
                vy2= 0
                ONGROUND2=True
                move2=""
            vy2+=1
    if keys[K_KP0] and dis2<=100:
        damage2=1


    
    circle2=draw.circle(screen,(0,0,255),(x2,int(y2)),10)
    if damage1==1:
        circle2=draw.circle(screen,(200,0,0),(x2,int(y2)),10)
        damage1=0
        damagep2+=200
        colour2=((255,0,0))
        damagedisplay()
      
    if damage2==1:
        circle=draw.circle(screen,(200,0,0),(x1,int(y1)),10)
        damage2=0
        damagep1+=200
        colour=((255,0,0))
        damagedisplay()

        
    
        
    if damagep1>=1000:
        screen.fill((0,0,0))
        txtPosp1=arialFont2.render(("You lose Player 1! GAME OVER!"),True,(red))
        screen.blit(txtPosp1,(0,200,100,100))
        txtPosReplay=arialFont2.render(("Replay"),True,(blue))
        screen.blit(txtPosReplay,(replayrect))
        if replayrect.collidepoint(mx,my):
            draw.rect(screen,(red),(replayrect),3)
            if mb[0]==1:
                damagep1=0
                damagep2=0
                screen.fill((255,255,255))
            
    elif damagep2>=1000:
        screen.fill((0,0,0))
        txtPosp2=arialFont2.render(("You lose Player 2! GAME OVER!"),True,(red))
        screen.blit(txtPosp2,(0,200,100,100))
        txtPosReplay=arialFont2.render(("Replay"),True,(blue))
        screen.blit(txtPosReplay,(replayrect))

        if replayrect.collidepoint(mx,my):
            draw.rect(screen,(red),(replayrect),3)
            if mb[0]==1:
                damagep1=0
                damagep2=0
                screen.fill((255,255,255))
        
    print(damagep1,damagep2)
    display.flip()
    myClock.tick(60) 
                      #start match function not working--the function damagedisplay is flawed
    
quit()
