from pygame import*
from random import*
from math import*

## need level editor

screen=display.set_mode((1000,800))
init()
myClock=time.Clock()

txtPosStartRect=Rect(500,300,30,30)
arialFontstart = font.SysFont("Times New Roman", 60)

#extra needed pictures===============================================================
Map=image.load("final destination.jpg")
picStandRight=image.load("Falcon/standingcaptR.png")
picStandLeft=image.load("Falcon/standingcaptL.png")
picJumpRight=image.load("Falcon/jumpright.png") 
picJumpLeft=image.load("Falcon/jumpleft.png")
picCrouchRight=image.load("Falcon/captcrouchr.png")
picCrouchLeft=image.load("Falcon/captcrouchl.png")
TauntPic=image.load("Falcon/captainfalconshowurmoves.png")

#picture================================================================
def MovementPic():
#run to the right ===================================================================
    global RunRFrame,RunRPic, RunR, RunL,direction
    if keys[K_RIGHT] and RunR==True:
        for i in range(5):
            RunRPic.append(image.load("Falcon/runcaptright" + str(i) + ".png"))
        screen.blit(RunRPic[RunRFrame],(x-10,y))
        RunRFrame += 1
        if RunRFrame == 5:
            RunRFrame = 0
        myClock.tick(10)

#run to the left ====================================================================
    global RunLFrame,RunLPic, RunL
    if keys[K_LEFT] and RunL==True:
        for i in range(5):
            RunLPic.append(image.load("Falcon/runcaptleft" + str(i) + ".png"))
        screen.blit(RunLPic[RunLFrame],(x-50,y))   
        RunLFrame += 1 
        if RunLFrame == 5: RunLFrame = 0
        myClock.tick(10)

#standing and Crouching ==================================================================================
    global direction, crouch, Taunt
    if RunL==False and RunR==False:
        if Taunt==True and keys[K_KP_ENTER]:
            screen.blit(TauntPic,(x-25,y-15))
            
        if direction=="right" and crouch==True and Taunt==False:
            screen.blit(picCrouchRight,(x-20,y+20))
            
        if direction=="left" and crouch==True and Taunt==False:
            screen.blit(picCrouchLeft,(x-20,y+20))
            
        if direction=="right" and crouch==False and Taunt==False:
            screen.blit(picStandRight,(x-20,y))

        if direction=="left" and crouch==False and Taunt==False:
            screen.blit(picStandLeft,(x-20,y))    

def startmatch():
    screen.fill((255,255,255))
    time.wait(200)
    for i in range(0,4):
        screen.fill((255,255,255))
        num=3-i
        txtPosStart=arialFontstart.render(str(num),True,(255,0,0))
        if num==0:
            txtPosStart=arialFontstart.render(str("FIGHT"),True,(255,0,0))
            screen.blit(txtPosStart,(450,300,200,200))
        time.wait(1000)
        if num!=0:
            screen.blit(txtPosStart,txtPosStartRect)
        display.flip()
#movement ===================================================================================================
def Walk():
    global x
    #move to the Left
    if keys[K_LEFT]:
        #if not jumping
        if RunL==True and Jump==False:
            x-=30
        #if jumping 
        if Jump==True:
            x-=10
    #move to the right 
    if keys[K_RIGHT]:
        #if not jumping 
        if RunR==True and Jump==False:
            x+=30
        #if jumping 
        if Jump==True:
            x+=10

def Attack1(Attack, direction):
    global x, y
    global Pun1RPic,Pun1RFrame,Pun2RPic,Pun2RFrame ,Pun3RPic,Pun3RFrame
    if direction=="right":
        if Attack==1:
            for i in range(7):
                Pun1RPic.append(image.load("Falcon/rapidfalconR" + str(i) + ".png"))
            screen.blit(Pun1RPic[Pun1RFrame],(x-20,y-10))
            Pun1RFrame += 1
            if Pun1RFrame == 7:
                Pun1RFrame = 0
            myClock.tick(10)

        if Attack==2:
            for i in range(3):
                Pun2RPic.append(image.load("Falcon/raptorboostright" + str(i) + ".png"))
            screen.blit(Pun2RPic[Pun2RFrame],(x-20,y-10))
            Pun2RFrame += 1
            x+=20
            if Pun2RFrame == 4:
                Pun2RFrame = 0
            myClock.tick(5)
            
        if Attack==3:
            for i in range(6):
                Pun3RPic.append(image.load("Falcon/falpunchpt" + str(i) + ".png"))
            screen.blit(Pun3RPic[Pun3RFrame],(x-20,y+10))
            Pun3RFrame += 1
            if Pun3RFrame == 6:
                Pun3RFrame = 0
            myClock.tick(5)
                
    global Pun1LPic,Pun1LFrame,Pun2LPic,Pun2LFrame,Pun3LPic,Pun3LFrame
    if direction=="left":
        if Attack==1:
            for i in range(7):
                Pun1LPic.append(image.load("Falcon/rapidfalconL" + str(i) + ".png"))
            screen.blit(Pun1LPic[Pun1LFrame],(x-20,y-10))
            Pun1LFrame += 1

            if Pun1LFrame == 7:
                Pun1LFrame = 0
            myClock.tick(10)

        if Attack==2:
            for i in range(3):
                Pun2LPic.append(image.load("Falcon/raptorboostleft" + str(i) + ".png"))
            screen.blit(Pun2LPic[Pun2LFrame],(x-20,y-10))
            Pun2LFrame += 1
            x-=20
            if Pun2LFrame == 4:
                Pun2LFrame = 0
            myClock.tick(5)

        if Attack==3:
            for i in range(6):
                Pun3LPic.append(image.load("Falcon/fpunchleft" + str(i) + ".png"))
            screen.blit(Pun3LPic[Pun3LFrame],(x-20,y+10))
            Pun3LFrame += 1
            if Pun3LFrame == 6:
                Pun3LFrame = 0
            myClock.tick(5)

running=True
ONGROUND=True


x=300 #
y=400 #position 
vy=2 #speed

dx=700
dy=400
dvy=2
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

DollRPic=[]
DollRFrame=0
DollLPic=[]
DollLFrame=0
for i in range(3):
    DollRPic.append(image.load("doll/trainingdollRight" + str(i) + ".png"))
for i in range(3):
    DollLPic.append(image.load("doll/trainingdollLeft" + str(i) + ".png"))
move=""
direction="right"

startmatch()
init()
music=mixer.music.load("Fairy Tail Soundtrack - Released Power.mp3")

mixer.music.play(-1)

while running:

    Punch=True
    Stand=True
    Attack=0 
    crouch=False
    Jump=False
    RunL=False
    RunR=False
    Taunt=False
    DONGROUND=True
    
    dist1=((x-dx)**2+(y-dy)**2)**0.5
    dist2=((x-dx)**2+(y-dy)**2)**0.5
    dist3=((x-dx)**2+(y-dy)**2)**0.5
    
    for evnt in event.get():                
        if evnt.type == QUIT:
            import mainmenu
            running = False
    keys = key.get_pressed()
    screen.blit(Map,(0,0))
    #screen.fill((255,255,255))

    if x>1000 or x<0:
        x=500
    if dx>1000 or dx<0:
        dx=500

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
                    screen.blit(picJumpLeft,(x-20,y))
                if direction=="right":
                    Jump=True
                    screen.blit(picJumpRight,(x-20,y))
            if keys[K_LEFT] and RunR==False:
                RunL=True
                Jump=True
                direction="left"
                screen.blit(picJumpLeft,(x,y))
            if keys[K_RIGHT] and RunL==False:
                RunR=True
                Jump=True
                direction="right"
                screen.blit(picJumpRight,(x,y))
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

#extra moves===========================================================================

    if move=="jump":
        y-=17
        ONGROUND=False
        if ONGROUND==False: # if sprite is of the ground
            y+=vy    
            if y == 400:
                y = 400
                vy= 0
                ONGROUND=True
                move=""
            vy+=1
            myClock.tick(60)


    if direction=="right":
        screen.blit(DollRPic[0],(dx,dy))
    if direction=="left":
        screen.blit(DollLPic[0],(dx,dy))        
    if Attack==1 and dist1<=50 or Attack==2 and dist2<=10 or Attack==3 and dist3<=50 and Pun3LFrame==5 or Attack==3 and dist3<=50 and Pun3RFrame==5 or DONGROUND==False:

        if direction =="right":
            dx+=70
            dy-=50

            screen.blit(DollRPic[DollRFrame],(dx,dy))
            DollRFrame += 1
            if DollRFrame == 3: DollRFrame = 0
            myClock.tick(50)

        if direction =="left":
            dx-=70
            dy-=50

            screen.blit(DollLPic[DollLFrame],(dx,dy))
            DollLFrame += 1
            if DollLFrame == 3: DollLFrame = 0
            myClock.tick(50)
    if dy<400:
        dy+=dvy
        DONGROUND==False
        if DONGROUND==False:
            if dy==400:
                dy==400
                dy=0
                DONGROUND=True
            dvy+=1


    display.flip()
quit()
