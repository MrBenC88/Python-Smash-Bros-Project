from pygame import*
screen = display.set_mode((1000,800))
init()
myClock = time.Clock()

picStandRight=image.load("standingcaptR.png")
picStandLeft=image.load("standingcaptL.png")
picJumpRight=image.load("jumpright.png") #changed image from jump to jumpright
picJumpLeft=image.load("jumpleft.png")
PosePic=image.load("captainfalconshowurmoves.png")

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
PunchRFrame=0
PunchLPic=[]
PunchLFrame=0
PoseStand=False
flyingpunchr=[]
flyingpunchl=[]
spmove2l=[]
spmove2r=[]
rfpunch=[]
lfpunch=[]
tim0=0#variables for keeping track of the special move, punches and flying kick
tim=0
time=0
time0=0
times=0
times1=0
fpframer=0
fpframel=0

background=((255,0,0))
while running:
    PoseStand=False
    RunR=False#right now he not running either direction 
    RunL=False#right now he not running either direction
    Punch=False
    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False
    keys = key.get_pressed()


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
        vy-=25
        ONGROUND=False #as soon as he jumps, he is no longer on the ground

    if ONGROUND==False: # if sprite is of the ground
        y+=vy    
        if y >= 400:
            y = 400
            vy = 0
            ONGROUND=True #when the the sprite hits the floor, he is now on the ground 
        vy+=1.5


    if ONGROUND==True and keys[K_KP1]:
        if R==1 or x==300 and R==0 and L==0 :
            Punch=True
            for i in range(7):
                PunchRPic.append(image.load("rapidfalconR" + str(i) + ".png")) #changed punch testpunch to rapidfalconR
        if L==1 or x==700 and R==0 and L==0:
            Punch=True
            for i in range(7):
                PunchLPic.append(image.load("rapidfalconL" + str(i) + ".png"))#changed punch testpunch to rapidfalconL

    elif ONGROUND==True and keys[K_KP2]:#
        if R==1:
            for i in range(3):
                flyingpunchr.append(image.load("raptorboostright" + str(i) + ".png"))#
        if L==1:
            for i in range(3):
                flyingpunchl.append(image.load("raptorboostleft" + str(i) + ".png"))#
        
            
    elif ONGROUND==True and keys[K_KP3] :#
        if R==1:
            for i in range(2):
                spmove2r.append(image.load("specialmoveright" + str(i) + ".png"))
        if L==1:
            for i in range(2):
                spmove2l.append(image.load("specialmoveleft2" + str(i) + ".png"))#
            
    elif ONGROUND==True and keys[K_KP4] :#
        if R==1:
            for i in range(6):
                rfpunch.append(image.load("falpunchpt" + str(i) + ".png"))
        if L==1:
            for i in range(6):
                lfpunch.append(image.load("fpunchleft" + str(i) + ".png"))



    screen.fill((255,255,255))
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

    if RunR==False and RunL==False and ONGROUND==True and PoseStand==False and Punch==False: #if the character is not moving
        if R==1 and L==0 and PoseStand==False:
            screen.blit(picStandRight,(x,y))
        if L==1 and R==0 and PoseStand==False:
            screen.blit(picStandLeft,(x,y))
        if x==300 and L==0 and R==0 and PoseStand==False: #when the character spawns on the left
            screen.blit(picStandRight,(x,y))
        if x==700 and L==0 and R==0 and PoseStand==False:#when the character spawns on the right
            screen.blit(picStandLeft,(x,y))

    if RunR==True and RunL==False and R==1 and ONGROUND==True and Punch==False or keys[K_RIGHT] and Punch==False and  ONGROUND==True:
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


    if  ONGROUND==True and keys[K_KP1] and R==1  and Punch==True and keys[K_RIGHT]!=1 or keys[K_RIGHT]!=1 and  x==300 and R==0 and L==0 and Punch==True:
        screen.blit(PunchRPic[PunchRFrame],(x,y))
        PunchRFrame += 1
        if PunchRFrame == 7:PunchRFrame = 0
        myClock.tick(14)

    if ONGROUND==True and keys[K_KP1] and L==1 and Punch==True and keys[K_LEFT]!=1 or x==700 and keys[K_LEFT]!=1 and R==0 and L==0 and Punch==True:
        screen.blit(PunchLPic[PunchLFrame],(x,y))
        PunchLFrame += 1
        if PunchLFrame == 7:PunchLFrame = 0
        myClock.tick(14)

    if ONGROUND==True and keys[K_KP2] and R==1 :#
        screen.fill(background)
        screen.blit(flyingpunchr[time0],(x,y))
        time0 += 1
        if time0 == 3:
            time0 = 0
        myClock.tick(3)
        
    if ONGROUND==True and keys[K_KP2] and L==1 :# 
        screen.fill(background)
        screen.blit(flyingpunchl[time],(x,y))
        time += 1
        if time == 3:
            time = 0
        myClock.tick(3)
        
    if ONGROUND==True and keys[K_KP3] and R==1 : # 
        screen.fill(background)
        screen.blit(spmove2r[tim0],(x,y))
        tim0 += 1
        if tim0 == 2:
            tim0 = 0
        myClock.tick(3)
        
    if ONGROUND==True and keys[K_KP3] and L==1:   # 
        screen.fill(background)
        screen.blit(spmove2l[tim],(x,y))
        tim += 1
        if tim == 2:
            tim = 0
        myClock.tick(3)

    if ONGROUND==True and keys[K_KP4] and R==1:   # 
        screen.fill(background)
        screen.blit(rfpunch[fpframer],(x,y))
        fpframer += 1
        if fpframer == 6:
            fpframer = 0
        myClock.tick(100) 

    if ONGROUND==True and keys[K_KP4] and L==1:   # 
        screen.fill(background)
        screen.blit(lfpunch[fpframel],(x,y))
        fpframel += 1
        if fpframel == 6:
            fpframel = 0
        myClock.tick(100)     


    display.flip()
    myClock.tick(60) 
                           
    
quit()
