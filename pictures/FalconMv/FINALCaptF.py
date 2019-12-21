from pygame import*
from random import*
from math import*

screen=display.set_mode((1000,800))
init()
myClock=time.Clock()

#extra needed pictures===============================================================
picStandRight=image.load("standingcaptR.png")
picStandLeft=image.load("standingcaptL.png")
picJumpRight=image.load("jumpright.png") 
picJumpLeft=image.load("jumpleft.png")
picCrouchRight=image.load("captcrouchr.png")
picCrouchLeft=image.load("captcrouchl.png")
TauntPic=image.load("captainfalconshowurmoves.png")

#picture================================================================
def MovementPic():
#run to the right ===================================================================
    global RunRFrame,RunRPic, RunR, RunL,direction
    if keys[K_RIGHT] and RunR==True:
        for i in range(5):
            RunRPic.append(image.load("runcaptright" + str(i) + ".png"))
        screen.blit(RunRPic[RunRFrame],(xCapt-10,yCapt))
        RunRFrame += 1
        if RunRFrame == 5:
            RunRFrame = 0
        myClock.tick(10)

#run to the left ====================================================================
    global RunLFrame,RunLPic, RunL
    if keys[K_LEFT] and RunL==True:
        for i in range(5):
            RunLPic.append(image.load("runcaptleft" + str(i) + ".png"))
        screen.blit(RunLPic[RunLFrame],(xCapt-50,yCapt))   
        RunLFrame += 1 
        if RunLFrame == 5: RunLFrame = 0
        myClock.tick(10)

#standing and Crouching ==================================================================================
    global direction, crouch, Taunt
    if RunL==False and RunR==False:
        if Taunt==True and keys[K_KP_ENTER]:
            screen.blit(TauntPic,(xCapt-25,yCapt-15))
            
        if direction=="right" and crouch==True and Taunt==False:
            screen.blit(picCrouchRight,(xCapt-20,yCapt+20))
            
        if direction=="left" and crouch==True and Taunt==False:
            screen.blit(picCrouchLeft,(xCapt-20,yCapt+20))
            
        if direction=="right" and crouch==False and Taunt==False:
            screen.blit(picStandRight,(xCapt-20,yCapt))

        if direction=="left" and crouch==False and Taunt==False:
            screen.blit(picStandLeft,(xCapt-20,yCapt))    

#movement ===================================================================================================
def Walk():
    global xCapt
    #move to the Left
    if keys[K_LEFT]:
        #if not jumping
        if RunL==True and Jump==False:
            xCapt-=30
        #if jumping 
        if Jump==True:
            xCapt-=10
    #move to the right 
    if keys[K_RIGHT]:
        #if not jumping 
        if RunR==True and Jump==False:
            xCapt+=30
        #if jumping 
        if Jump==True:
            xCapt+=10

def Attack1(Attack, direction):
    global xCapt, yCapt
    global Pun1RPic,Pun1RFrame,Pun2RPic,Pun2RFrame ,Pun3RPic,Pun3RFrame
    if direction=="right":
        if Attack==1:
            for i in range(7):
                Pun1RPic.append(image.load("rapidfalconR" + str(i) + ".png"))
            screen.blit(Pun1RPic[Pun1RFrame],(xCapt-20,yCapt-10))
            Pun1RFrame += 1
            if Pun1RFrame == 7:
                Pun1RFrame = 0
            myClock.tick(10)

        if Attack==2:
            for i in range(3):
                Pun2RPic.append(image.load("raptorboostright" + str(i) + ".png"))
            screen.blit(Pun2RPic[Pun2RFrame],(xCapt-20,yCapt-10))
            Pun2RFrame += 1
            xCapt+=20
            if Pun2RFrame == 4:
                Pun2RFrame = 0
            myClock.tick(5)
            
        if Attack==3:
            for i in range(6):
                Pun3RPic.append(image.load("falpunchpt" + str(i) + ".png"))
            screen.blit(Pun3RPic[Pun3RFrame],(xCapt-20,yCapt+10))
            Pun3RFrame += 1
            if Pun3RFrame == 6:
                Pun3RFrame = 0
            myClock.tick(5)
                
    global Pun1LPic,Pun1LFrame,Pun2LPic,Pun2LFrame,Pun3LPic,Pun3LFrame
    if direction=="left":
        if Attack==1:
            for i in range(7):
                Pun1LPic.append(image.load("rapidfalconL" + str(i) + ".png"))
            screen.blit(Pun1LPic[Pun1LFrame],(xCapt-20,yCapt-10))
            Pun1LFrame += 1

            if Pun1LFrame == 7:
                Pun1LFrame = 0
            myClock.tick(10)

        if Attack==2:
            for i in range(3):
                Pun2LPic.append(image.load("raptorboostleft" + str(i) + ".png"))
            screen.blit(Pun2LPic[Pun2LFrame],(xCapt-20,yCapt-10))
            Pun2LFrame += 1
            xCapt-=20
            if Pun2LFrame == 4:
                Pun2LFrame = 0
            myClock.tick(5)

        if Attack==3:
            for i in range(6):
                Pun3LPic.append(image.load("fpunchleft" + str(i) + ".png"))
            screen.blit(Pun3LPic[Pun3LFrame],(x-20,yCapt+10))
            Pun3LFrame += 1
            if Pun3LFrame == 6:
                Pun3LFrame = 0
            myClock.tick(5)

running=True
ONGROUND=True
xCapt=300 #
yCapt=400 #position 
vyCapt=2 #speed

RunRFrame=0 ## of frames
RunRPic=[] #list of pictures

RunLFrame=0
RunLPic=[]

Pun1RFrame=0
Pun1RPic=[]
Pun2RFrame=0
Pun2RPic=[]
Pun3RFrame=0
Pun3RPic=[]

Pun1LFrame=0
Pun1LPic=[]
Pun2LFrame=0
Pun2LPic=[]
Pun3LFrame=0
Pun3LPic=[]


move=""
direction="right"
while running:

    Punch=True
    Stand=True
    Attack=0 
    crouch=False
    Jump=False
    RunL=False
    RunR=False
    Taunt=False
    
    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False
    keys = key.get_pressed()
    screen.fill((255,255,255))

    if xCapt>1000 or xCapt<0:
        xCapt=500

#Attacks===============================================================================
    if crouch==False and Jump==False and Punch==True:

        if keys[K_KP1] or keys[K_KP2] or keys[K_KP3]:

                Stand=False
                RunL=False
                RunR=False

                if keys[K_KP1]:
                    Attack=1
                if keys[K_KP2] and keys[K_UP]!=1 and ONGROUND==True:
                     Attack=2
                if keys[K_KP3] and keys[K_UP]!=1 and ONGROUND==True:
                    Attack=3
            
                Attack1(Attack,direction)
            
#Jumping===========================================================================
    if keys[K_UP] or ONGROUND==False:
        if keys[K_KP1]!=1:
            if keys[K_LEFT]!=1 and keys[K_RIGHT]!=1:
                if direction=="left":
                    Jump=True
                    screen.blit(picJumpLeft,(xCapt-20,yCapt))
                if direction=="right":
                    Jump=True
                    screen.blit(picJumpRight,(xCapt-20,yCapt))
            if keys[K_LEFT] and RunR==False:
                RunL=True
                Jump=True
                direction="left"
                screen.blit(picJumpLeft,(xCapt,yCapt))
            if keys[K_RIGHT] and RunL==False:
                RunR=True
                Jump=True
                direction="right"
                screen.blit(picJumpRight,(xCapt,yCapt))
        if keys[K_KP1]:
            Walk()
            
        Walk()
        move="jump"
        
# Walking ================================================================================
    elif ONGROUND==True and Attack==0:
        if keys[K_LEFT] or keys[K_RIGHT]:
            if keys[K_RIGHT] and RunL==False:
                direction="right"
                RunR=True
                MovementPic()
                Walk()
            elif keys[K_LEFT] and RunR==False:
                direction="left"
                RunL=True
                MovementPic()
                Walk()
            
#Standing===============================================================================
        if RunL==False and RunR==False and Stand==True:
            if keys[K_DOWN]:
                crouch=True

            if keys[K_KP_ENTER]:
                #taunt
                Taunt=True
            MovementPic()                

#exCapttra moves===========================================================================

    if move=="jump":
        yCapt-=17
        ONGROUND=False
        if ONGROUND==False: # if sprite is of the ground
            yCapt+=vyCapt    
            if yCapt == 400:
                yCapt = 400
                vyCapt= 0
                ONGROUND=True
                move=""
            vyCapt+=1
            myClock.tick(60)

    display.flip()                      
quit()
