from pygame import*
from random import*
from math import*

screen=display.set_mode((1000,800))
init()
myClock=time.Clock()

picStandRight=image.load("standingcaptR.png")
picStandLeft=image.load("standingcaptL.png")
picJumpRight=image.load("jumpright.png") 
picJumpLeft=image.load("jumpleft.png")
#-------------------------------------------------------------------------
def walk1(direction):
    global x1,y1,RunRPic,RunRFrame,RunLPic,RunLFrame,RunL,RunR,ONGROUND,move
    keys=key.get_pressed()
    if RunL==True and RunR==False and move=="" or RunL==False and RunR==True and move=="":
        if keys[K_d] and direction=="right" and RunL==False and RunR==True and ONGROUND!=False:
            direction = "right"
            x1+=30

            for i in range(5):
                RunRPic.append(image.load("runcaptright" + str(i) + ".png"))
            screen.blit(RunRPic[RunRFrame],(x1,y1))
            RunRFrame += 1
            if RunRFrame == 5:
                RunRFrame = 0

        if keys[K_a] and direction=="left" and RunL==True and RunR==False  and ONGROUND!=False:
            direction = "left"
            x1-=30
            for i in range(5):
                RunLPic.append(image.load("runcaptleft" + str(i) + ".png"))
            screen.blit(RunLPic[RunLFrame],(x1,y1))   
            RunLFrame += 1 
            if RunLFrame == 5: RunLFrame = 0
        myClock.tick(14)

    if move=="jump":
        if direction=="right":
            x1+=10
            screen.blit(picJumpRight,(x1,y1))
        if direction=="left":
            x1-=10
            screen.blit(picJumpLeft,(x1,y1))
            


def stand1(direction):
    global x1,y1
    if direction=="right":
        screen.blit(picStandRight,(x1,y1))
    if direction=="left":
        screen.blit(picStandLeft,(x1,y1))


def jump1(direction):
    global x1, y1, jumpR,jumpL
    if direction =="right" and jumpR==True and jumpL==False:
        screen.blit(picJumpRight,(x1,y1))
    elif direction=="left" and jumpL==True and jumpR==False:
        screen.blit(picJumpLeft,(x1,y1))




def walk2(direction2):
    global x2,y2
    keys=key.get_pressed()
    if keys[K_RIGHT]:
        direction2 = "right"
        x2+=10


    if keys[K_LEFT]:
        direction2 = "left"
        x2-=10




running=True

ONGROUND2=True
x1=300
y1=400

x2=700
y2=400

RunRFrame=0
RunRPic=[]

RunLFrame=0
RunLPic=[]

vy1=2
vy2=2

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
    jumpL=False
    jumpR=False
    RunL=False
    RunR=False
    dis1=((x1-x2)**2+(y1-y2)**2)**.5
    ONGROUND=True
    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False
    keys = key.get_pressed()


    screen.fill((255,255,255))
    if player=="Captian Falcon":
        if keys[K_d] and keys[K_w] and keys[K_a]!=1:
            direction="right"
            jumpR=True
            jumpL=False
            x1+=10
            jump1(direction)
        if keys[K_a] and keys[K_w] and keys[K_d]!=1:
            direction="left"
            jumpL=True
            jumpR=False
            x1-=10
            jump1(direction)
            

        if  keys[K_d] and keys[K_w]!=1:
            if jumpR==False:
                RunR=True
                direction="right"
                walk1(direction)


        if keys[K_a] and keys[K_w]!=1:
            if jumpL==False:
                RunL=True
                direction="left"
                walk1(direction)


        if keys[K_w] or ONGROUND==False:
            if direction=="right":
                jumpR=True
                jumpL=False
                move="jump"
                jump1(direction)


            if direction=="left":
                jumpL=True
                jumpR=False
                move="jump"
                jump1(direction)


        if RunL==False and RunR==False and jumpL==False and jumpR==False:
            stand1(direction)
        
        if keys[K_SPACE] and dis1<=100:
            damage1=1
        
        
#----------------------------------------------------------------------------------

    if player2=="fox":
        if keys[K_LEFT] or keys[K_RIGHT]:
            walk2(direction2)
        if keys[K_UP] or ONGROUND2==False:
                move2="jump"




# Moves ----------------------------------------------------------------------------------

    if move=="jump":
        y1-=15
        ONGROUND=False
        if ONGROUND==False: # if sprite is of the ground
            y1+=vy1    
            if y1 == 400:
                y1 = 400
                vy1= 0
                jumpL=False
                jumpR=False
                ONGROUND=True
                move=""
            vy1+=1

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


    
    circle2=draw.circle(screen,(0,255,0),(x2,int(y2)),10)
    if damage1==1:
        circle2=draw.circle(screen,(200,0,0),(x2,int(y2)),10)
        damage1=0
    if damage2==1:
        circle=draw.circle(screen,(200,0,0),(x1,int(y1)),10)
        damage2=0        
        
    display.flip()
    myClock.tick(60) 
                           
    
quit()
