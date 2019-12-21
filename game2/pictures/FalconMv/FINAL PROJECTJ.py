from pygame import*
screen = display.set_mode((1000,800))
init()
myClock = time.Clock()

def crouch1(x,y,direct,charactersymbol):
    Rightpic=image.load(charactersymbol+"CrouchR.png" )
    Leftpic=image.load(charactersymbol+"CrouchL.png" )
    if keys[K_s] :
        if direct=="Right":
            screen.blit(Rightpic,(x,y))
        elif direct=="Left":
            screen.blit(Leftpic,(x,y))
    elif keys[K_DOWN] :
        if direct=="Right":
            screen.blit(Rightpic,(x,y))
        elif direct=="Left":
            screen.blit(Leftpic,(x,y))        

            
picStandRight=image.load("standingcaptR.png")
picStandLeft=image.load("standingcaptL.png")
picJumpRight=image.load("jumpright.png") #changed image from jump to jumpright
picJumpLeft=image.load("jumpleft.png")
PosePic=image.load("captainfalconshowurmoves.png")
CrouchRightPic=image.load("specialmoveright21.png")
CrouchLeftPic=image.load("specialmoveleft0.png")

RunR=False#right now he not running either direction 
RunL=False#right now he not running either direction
Punch=False
running = True
n=10
ONGROUND=True #to show whether or not the sprite is on the ground or not
x = 300 #starting position(middle)
y = 400 #
vy=2
RunRFrame = 0 #running Right frames
RunRPic = []  #Running right picture list 
RunLFrame = 0 #running Left frames
RunLPic = []  #Running Left picture list
L=0 #looking to the left side
R=0 #look to the right side
jumpL=False #the character is not jumping 
jumpR=False #

PunchRPic=[]
PunchLPic=[]

PunchRFrame=0
PunchLFrame=0

FPunchRFrame=0
FPunchLFrame=0
PoseStand=False
crouch=False
FlyingPunchR=[]
FlyingPunchL=[]

rfpunch=[]
lfpunch=[]

LowKickR=[]
LowKickL=[]
LowLKickFrame=0
LowRKickFrame=0
fpframer=0
fpframel=0

while running:
    PoseStand=False
    RunR=False#right now he not running either direction 
    RunL=False#right now he not running either direction
    Punch=False
    crouch=False
    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False
    keys = key.get_pressed()
    screen.fill((255,255,255))


    if ONGROUND==False and keys[K_LEFT]: #if the sprite is not the ground and the left key was pressed
        jumpL=True  # the sprite is jumping left 
        jumpR=False #the sprite is not jumping right
    if ONGROUND==False and keys[K_RIGHT]: #if the sprite is not the ground and the right key was pressed
        jumpL=False #the sprite is not jumping left
        jumpR=True #the sprite is jumping right 

#when user clicks right 
    if keys[K_RIGHT] and x <999:
        RunR=True   #when the sprite runs right. RunR is now true
        RunL=False  #since he is running right, he is no longer running left
        L=0
        R=1
        n=10
        x+=n

        if ONGROUND==True:
            n=30
            x+=n
            for i in range(5): #input all the running pictures into RunRPic list 
                RunRPic.append(image.load("runcaptright" + str(i) + ".png"))


#when user clicks left
    if keys[K_LEFT] and x > 1:
        RunR=False #when the sprite runing left. RunL is now true
        RunL=True  #since he is running left, he is no longer running right
        R=0
        L=1
        n=10
        x-=n
 
       
        if ONGROUND==True:
            n=30
            x-=n
            for i in range(5): #input all the running pictures into RunRPic list 
                RunLPic.append(image.load("runcaptleft" + str(i) + ".png")) #changed image to runcaptright
#if the go off screen, he respond

    
    elif x>=1000:
        x=500
        y=400
    elif x<=0:
        x=500
        y=400

#if he jumps 

    if keys[K_UP] and ONGROUND==True: #if the sprite is on the ground and you press up 
        vy-=20
        ONGROUND=False #as soon as he jumps, he is no longer on the ground
    if ONGROUND==False: # if sprite is of the ground
        y+=vy    
        if y >= 400:
            y = 400
            vy = 0
            ONGROUND=True #when the the sprite hits the floor, he is now on the ground 
        vy+=1.5


     #rapid jump   
    if ONGROUND==True and keys[K_KP1] :
        if R==1 or x==300 and R==0 and L==0 :
            
            Punch=True
            for i in range(7):
                PunchRPic.append(image.load("rapidfalconR" + str(i) + ".png")) #changed punch testpunch to rapidfalconR
        if L==1 or x==700 and R==0 and L==0:
            
            Punch=True
            for i in range(7):
                PunchLPic.append(image.load("rapidfalconL" + str(i) + ".png"))#changed punch testpunch to rapidfalconL

    #diver punch
    if ONGROUND==True and keys[K_KP2]:
        if RunR==False and RunL==False or RunR==False and RunL==True or RunR==True and RunL==False:
            Punch=True
            if R==1 or x==300 and R==0 and L==0:
                R=1
                x+=20
                for i in range(3):
                    FlyingPunchR.append(image.load("raptorboostright" + str(i) + ".png"))

            if L==1 or x==700 and R==0 and L==0:
                L=1
                x-=20
                for i in range(3):
                    FlyingPunchL.append(image.load("raptorboostleft" + str(i) + ".png"))

    #low kick
    if ONGROUND==True and keys[K_KP3] :
        if RunR==False and RunL==False or RunR==False and RunL==True or RunR==True and RunL==False:
            Punch=True
            if R==1 or x==300 and R==0 and L==0:
                R=1
                x+=10
                for i in range(2):
                    LowKickR.append(image.load("specialmoveright" + str(i) + ".png"))
            if L==1 or x==700 and R==0 and L==0:
                L=1
                x-=10
                for i in range(2):
                    LowKickL.append(image.load("specialmoveleft2" + str(i) + ".png"))       

    elif ONGROUND==True and keys[K_KP4] :#
        if R==1:
            for i in range(6):
                rfpunch.append(image.load("falpunchpt" + str(i) + ".png"))
        if L==1:
            for i in range(6):
                lfpunch.append(image.load("fpunchleft" + str(i) + ".png"))

    if keys[K_DOWN]:
        if ONGROUND==True and RunR==False and RunL==False:
            if R==1:
                screen.fill((255,255,255))
                PoseStand=True
                crouch1(x,y,"Right","capt")
                
            if L==1:
                screen.fill((255,255,255))
                PoseStand=True
                crouch1(x,y,"Left","capt")
               
#jumping Left
    if jumpL==True and ONGROUND==False and L==1 or L==1 and  ONGROUND==False or x==700 and L==0 and R==0 and ONGROUND==False:
        
        L=1
        RunR=False
        RunL=False
        screen.blit(picJumpLeft,(x,y))
        myClock.tick(60)
        if y >= 400:
            jumpL=False
            RunL=True
#jumping Right
    if jumpR==True and ONGROUND==False and R==1 or R==1 and ONGROUND==False or x==300 and L==0 and R==0 and ONGROUND==False:

        R=1
        RunR=False
        RunL=False
        screen.blit(picJumpRight,(x,y))
        myClock.tick(60)
        if y >= 400:
            jumpR=False
            RunR=True
    
    #the image of him running right 

    if RunR==False and RunL==False and ONGROUND==True and PoseStand==False and Punch==False and crouch==False: #if the character is not moving
        if R==1 and L==0 and PoseStand==False:
            screen.blit(picStandRight,(x,y))
        if L==1 and R==0 and PoseStand==False:
            screen.blit(picStandLeft,(x,y))
        if x==300 and L==0 and R==0 and PoseStand==False: #when the character spawns on the left
            screen.blit(picStandRight,(x,y))
        if x==700 and L==0 and R==0 and PoseStand==False:#when the character spawns on the right
            screen.blit(picStandLeft,(x,y))

    if RunR==True and RunL==False and R==1 and ONGROUND==True and Punch==False or keys[K_RIGHT] and Punch==True and  ONGROUND==True:
        screen.blit(RunRPic[RunRFrame],(x,y))#blit the new image
        RunRFrame += 1 #continuously add one to frame to help it rotate
        myClock.tick(15)
        if RunRFrame == 5: RunRFrame = 0 #when the frame # reaches 5, go to 0

    if keys[K_KP_ENTER] and RunL==False and RunR==False  and ONGROUND==True and Punch==False:
        PoseStand=True

        screen.fill((255,255,255))
        screen.blit(PosePic,(x-10,y-15))
        
    if RunL==True and RunR==False and L==1 and ONGROUND==True and Punch==False or Punch==True and keys[K_LEFT]  and ONGROUND==True: #if the user clicked LEFT
        screen.blit(RunLPic[RunLFrame],(x,y))#blit the new image
        RunLFrame += 1 #continuously add one to frame to help it rotate
        myClock.tick(15)
        if RunLFrame == 5: RunLFrame = 0 #when the frame # reaches 5, go to 0


    if ONGROUND==True and keys[K_KP1] and R==1 and Punch==True and keys[K_RIGHT]!=1 or x==300 and keys[K_RIGHT]!=1 and R==0 and L==0 and Punch==True:
        screen.blit(PunchRPic[PunchRFrame],(x,y))
        PunchRFrame += 1
        if PunchRFrame == 7:PunchRFrame = 0
        myClock.tick(14)

    if ONGROUND==True and keys[K_KP1] and L==1 and Punch==True and keys[K_LEFT]!=1 or x==700 and keys[K_LEFT]!=1 and R==0 and L==0 and Punch==True:
        screen.blit(PunchLPic[PunchLFrame],(x,y))
        PunchLFrame += 1
        if PunchLFrame == 7:PunchLFrame = 0
        myClock.tick(14)

    if ONGROUND==True and keys[K_KP2] and R==1 and Punch==True:
        screen.fill((255,255,255))
        screen.blit(FlyingPunchR[FPunchRFrame],(x,y))
        FPunchRFrame += 1
        if FPunchRFrame == 3:
            FPunchRFrame = 0
        myClock.tick(5)
    if ONGROUND==True and keys[K_KP2] and L==1 and Punch==True: 
        screen.fill((255,255,255))
        screen.blit(FlyingPunchL[FPunchLFrame],(x,y))
        FPunchLFrame += 1
        if FPunchLFrame == 3:
            FPunchLFrame = 0
        myClock.tick(5)

    if ONGROUND==True and keys[K_KP3] and R==1 and Punch==True: # 
        screen.fill((255,255,255))
        screen.blit(LowKickR[LowLKickFrame],(x,y))
        LowLKickFrame += 1
        if LowLKickFrame == 2:LowLKickFrame = 0
        myClock.tick(7)
        
    if ONGROUND==True and keys[K_KP3] and L==1 and Punch==True:   # 
        screen.fill((255,255,255))
        screen.blit(LowKickL[LowRKickFrame],(x,y))
        LowRKickFrame += 1
        if LowRKickFrame == 2:LowRKickFrame = 0
        myClock.tick(7)
        
    if ONGROUND==True and keys[K_KP4] and R==1:   # 
        screen.fill((255,255,255))
        screen.blit(rfpunch[fpframer],(x,y))
        fpframer += 1
        if fpframer == 6:
            fpframer = 0
        myClock.tick(100) 

    if ONGROUND==True and keys[K_KP4] and L==1:   # 
        screen.fill((255,255,255))
        screen.blit(lfpunch[fpframel],(x,y))
        fpframel += 1
        if fpframel == 6:
            fpframel = 0
        myClock.tick(100)     

    
    display.flip()
    myClock.tick(60) 


        ### PATCH----we need to fix the layout of entire code-->not efficient
    ###  WE need functions to splt the code into sections and 3d lists
    
quit()
