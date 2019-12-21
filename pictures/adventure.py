#adventure.py
#---------------------------------------------------------------
from pygame import* #import all the modules
from random import*
from pygame import*
init() #initiate all of the code 
screen=display.set_mode((1000,800)) #set screen size

display.init()   # <--Must have for Caption
display.set_caption("Clash of The FairyTail")


myClock=time.Clock() #set clock
enemypic=image.load("adventureENEMY.PNG") #load pics
ghost=image.load("ghostEN.png")
rageghost=image.load("RAGEghost.png")
hitghost=image.load("ghostENhit.png")
Map=image.load("final destination.jpg")

COLOUR=((255,255,255))
#----------------------------------------------------------------------------
speed=6


size=20
atkRANGE=20
atk=3
vy0=2
x0=100
y0=200

#velocities for the enemies
vx0=5
vy0=2
vx=5
vy=2
vx1=5
vy1=2
vx2=5
vy2=2
vx3=5
vy3=2
vx4=5
vy4=2
vx5=5
vy5=2

# coordinates/position of the enemies
x,y=10,0
x1,y1=200,0
x2,y2= 400,0
x3,y3= 600,0
x4,y4= 800,0
x5,y5= 990,0

#flags
running=True
ONGROUND=True
enemyon=True
Quit=False
ONGROUND=True
damaEN=False
dama=False
alive=True
againgame=False
Right=True
Left=False
block=False

score=0 #a counter for the score
xCapt=500 #position/coordinates of character
yCapt=400
scoreRect=Rect(850,10,100,100) #rectangle for the score text
healthp1=5000 #health of player's character


arialFontstart = font.SysFont("Times New Roman", 60) #get font from system
arialFontscore = font.SysFont("Times New Roman", 35)
arialFont2 = font.SysFont("Times New Roman", 70)

#set Rectangles sizes
healthrect=Rect(300,700,100,100)
enhealthrect=Rect(700,700,100,100)
replayrect=Rect(400,500,200,100)
Quitrect=Rect(400,400,200,100)
txtPosStartRect=Rect(500,300,30,30)
#colours
red=((255,0,0))
blue=((0,100,255))

player="P1"
move=""
enemyhealth=10000

     

    

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
direction="right"
#------------------------------FUNCTIONS------------------------------------

    
def startmatch():# af unctions that blits a countdown at start of game
    screen.blit(Map,(0,0))
    time.wait(200)
    for i in range(0,4):
        screen.blit(Map,(0,0))
        num=3-i
        txtPosStart=arialFontstart.render(str(num),True,(255,0,0))
        if num==0:
            txtPosStart=arialFontstart.render(str("FIGHT"),True,(255,0,0))
            screen.blit(txtPosStart,(450,300,200,200)) #blit text
        time.wait(1000)
        if num!=0:
            screen.blit(txtPosStart,txtPosStartRect)
        display.flip()
        
def healthdisplay(): #displays health
    '''dislays health percentage that player have gained'''
    global txtPos2, colour2, COLOUR
    txtPos2=arialFont2.render((str(healthp1)+"%"),True,(COLOUR))
    screen.blit(txtPos2,healthrect)
    txtPosEN=arialFont2.render((str(enemyhealth)+"%"),True,(COLOUR))
    screen.blit(txtPosEN,enhealthrect)
    
def scoredisplay(): #dsiplays score
    txtPosScore=arialFontscore.render((str(score)),True,(blue))
    screen.blit(txtPosScore,scoreRect)
    
def offscreen(xCapt,yCapt): 
    '''checks if player is offscreen'''
    global healthp1

    if xCapt>=1000 or xCapt<=0 or yCapt<=0 or yCapt>=1000:
        xCapt=500
        yCapt=400
        healthp1-=1000# if character is offscreen, then they lose


#----------------------------------------------------------------------------
#---------------------CAPTAIN FALCON STUFF-------------------------------------
#----------------------------------------------------------------------------        
#extra needed pictures===============================================================
#load the pics
picStandRight=image.load("FalconMv\\standingcaptR.png")
picStandLeft=image.load("FalconMv\\standingcaptL.png")
picJumpRight=image.load("FalconMv\\jumpright.png") 
picJumpLeft=image.load("FalconMv\\jumpleft.png")
picCrouchRight=image.load("FalconMv\\captcrouchr.png")
picCrouchLeft=image.load("FalconMv\\captcrouchl.png")
TauntPic=image.load("FalconMv\\captainfalconshowurmoves.png")
rightblockpic=image.load("FalconMv\\falconblockright.png")
leftblockpic=image.load("FalconMv\\falconblockleft.png")

#picture================================================================
def runsprite():
#run to the right ===================================================================
    global RunRFrame,RunRPic, RunR, RunL,direction, Right, Left
    if keys[K_RIGHT] and RunR==True:
        Right=True
        Left=False
        for i in range(5):
            RunRPic.append(image.load("FalconMv\\runcaptright" + str(i) + ".png"))
        screen.blit(RunRPic[RunRFrame],(xCapt-10,yCapt))
        RunRFrame += 1
        if RunRFrame == 5:
            RunRFrame = 0
        

#run to the left ====================================================================
    global RunLFrame,RunLPic, RunL
    if keys[K_LEFT] and RunL==True:
        Left==True
        Right=False
        for i in range(5):
            RunLPic.append(image.load("FalconMv\\runcaptleft" + str(i) + ".png"))
        screen.blit(RunLPic[RunLFrame],(xCapt-50,yCapt))   
        RunLFrame += 1 
        if RunLFrame == 5: RunLFrame = 0
       

#standing and Crouching ==================================================================================
    global direction, crouch, Taunt,healthp1
    if RunL==False and RunR==False:
        if Taunt==True and keys[K_KP_ENTER]:
            screen.blit(TauntPic,(xCapt-25,yCapt-15))
            healthp1+=3
            
        if direction=="right" and crouch==True and Taunt==False:
            screen.blit(picCrouchRight,(xCapt-20,yCapt+20))
            Right==True
            Left=False
            
        if direction=="left" and crouch==True and Taunt==False:
            screen.blit(picCrouchLeft,(xCapt-20,yCapt+20))
            Left==True
            Right=False
            
        if direction=="right" and crouch==False and Taunt==False:
            screen.blit(picStandRight,(xCapt-20,yCapt))
            Right==True
            Left=False

        if direction=="left" and crouch==False and Taunt==False:
            screen.blit(picStandLeft,(xCapt-20,yCapt))
            Left==True
            Right=False
    
            

#movement ===================================================================================================
def Walk(): # a function that changes the x coordinate of the player when
    #arrow key is pressed
    global xCapt
    
    if keys[K_LEFT]:
        
        if RunL==True and Jump==False:
            xCapt-=17
        
        if Jump==True:
            xCapt-=10
     
    if keys[K_RIGHT]:
         
        if RunR==True and Jump==False:
            xCapt+=17
        
        if Jump==True:
            xCapt+=10

def Attack1(Attack, direction):#the attack moves of the character
    global xCapt, yCapt, dama, enemyhealth, score, Right, Left
    global Pun1RPic,Pun1RFrame,Pun2RPic,Pun2RFrame ,Pun3RPic,Pun3RFrame
    global Pun1LPic,Pun1LFrame,Pun2LPic,Pun2LFrame,Pun3LPic,Pun3LFrame
    if direction=="right":
        if Attack==1 and dama==True:
            for i in range(7):
                Pun1RPic.append(image.load("FalconMv\\rapidfalconR" + str(i) + ".png"))
                # ^adds the pics into a list to be used as a sprite
            screen.blit(Pun1RPic[Pun1RFrame],(xCapt-20,yCapt-10)) #blit the pictures in the range of (7)
            Pun1RFrame += 1 #add one to the frame
            if dis1<61 and Right==True and Left==False:#if attack hits the enemy
                screen.blit(hitghost,(x0-20,y0-20)) #display a damaged pic
                enemyhealth-=5 #subtract enemy health
                score+=1 #add score
                dama=False
    
            if Pun1RFrame == 7: #this is here to make sure list never goes out of range
                Pun1RFrame = 0
           

        if Attack==2 and dama==True : # comments same as Attack1
            for i in range(3):
                Pun2RPic.append(image.load("FalconMv\\raptorboostright" + str(i) + ".png"))
            screen.blit(Pun2RPic[Pun2RFrame],(xCapt-20,yCapt-10))
            Pun2RFrame += 1
            if Pun2RFrame == 4:
                Pun2RFrame = 0
            
            if dis1<20 and Right==True and Left==False:
                screen.blit(hitghost,(x0-20,y0-20))
             
                enemyhealth-=8
                score+=2

                dama=False                
            
        if Attack==3 and dama==True: # comments same as Attack1
            for i in range(6):
                Pun3RPic.append(image.load("FalconMv\\falpunchpt" + str(i) + ".png"))
            screen.blit(Pun3RPic[Pun3RFrame],(xCapt-20,yCapt+10))
            Pun3RFrame += 1
            if Pun3RFrame == 6:
                Pun3RFrame = 0
          
            if dis1<15 and Right==True and Left==False:
                screen.blit(hitghost,(x0-20,y0-20))
             
                enemyhealth-=50
                score+=10
                dama=False 
                
    
    elif direction=="left": # comments same as Attack1
        if Attack==1:
            for i in range(7):
                Pun1LPic.append(image.load("FalconMv\\rapidfalconL" + str(i) + ".png"))
            screen.blit(Pun1LPic[Pun1LFrame],(xCapt-20,yCapt-10))
            Pun1LFrame += 1
            if dis1<61 and Left==True and Right==False:
                screen.blit(hitghost,(x0-20,y0-20))
           
                enemyhealth-=5
                score+=1

                dama=False            

            if Pun1LFrame == 7:
                Pun1LFrame = 0
          

        if Attack==2: # comments same as Attack1
            for i in range(3):
                Pun2LPic.append(image.load("FalconMv\\raptorboostleft" + str(i) + ".png"))
            screen.blit(Pun2LPic[Pun2LFrame],(xCapt-20,yCapt-10))
            Pun2LFrame += 1
            if dis1<20 and Left==True and Right==False:
                screen.blit(hitghost,(x0-20,y0-20))
               
                enemyhealth-=8
                score+=2

                dama=False              
            if Pun2LFrame == 4:
                Pun2LFrame = 0
        

        if Attack==3: # comments same as Attack1
            for i in range(6):
                Pun3LPic.append(image.load("FalconMv\\fpunchleft" + str(i) + ".png"))
            screen.blit(Pun3LPic[Pun3LFrame],(xCapt-20,yCapt+10))
            Pun3LFrame += 1
            if dis1<15 and Left==True and Right==False:
                screen.blit(hitghost,(x0-20,y0-20))
           
                enemyhealth-=50
                score+=10
                dama=False             
            if Pun3LFrame == 6:
                Pun3LFrame = 0
         


#----------------------------------------------------------------------------
#------------------------------Event Loop------------------------------------
 
startmatch() #call the function to have countdown before the match

while running:
    #defaut conditions /starting conditions as soon as game runs
    Punch=True
    Stand=True
    Attack=0 
    crouch=False
    Jump=False
    RunL=False
    RunR=False
    Taunt=False    
    screen.blit(Map,(0,0)) #blit map
    screen.blit(ghost,(x0-20,y0-20)) #blit enemy boss
    dis1=((xCapt-x0)**2+(yCapt-y0)**2)**.5 #distance formula to find range 
    dis2=((xCapt-x0)**2+(yCapt-y0)**2)**.5 #of attack and whether attak is hit or miss


    #============EVENT LOOP :D=================
    for evnt in event.get():                
        if evnt.type == QUIT:
            quit()
            break
            running = False
            
    keys = key.get_pressed() #sets keys
    mx,my=mouse.get_pos() #sets mouse position
    mb=mouse.get_pressed() #sets varible for mouse getting pressed
    
    if keys[K_KP1] or keys[K_KP2] or keys[K_KP3]: #if those keys are pressed,
        if dis1<51:# and the distance is in that range
            dama=True #attack has been hit and landed
        Stand=False
        RunL=False
        RunR=False

        #=====================================
        if keys[K_KP1]: # all the tings within this area are to set which direction
            if xCapt>x0: #the character is facing
                Right=False
                Left=True
            else:
                Left=False
                Right=True
            Attack=1 #this marks which attack is going to be blitted and what damage it gives
        elif keys[K_KP2] and keys[K_UP]!=1 and ONGROUND==True:
            if xCapt>x0:
                Right=False
                Left=True
            else:
                Left=False
                Right=True
            Attack=2#this marks which attack is going to be blitted and what damage it gives
        elif keys[K_KP3] and keys[K_UP]!=1 and ONGROUND==True:
            if xCapt>x0:
                Right=False
                Left=True
            else:
                Left=False
                Right=True
            Attack=3#this marks which attack is going to be blitted and what damage it gives
        #=====================================
        Attack1(Attack,direction) #calls the ATTACK function
        #=====================================
        
    if dis2<=atkRANGE: #The condition if the player is in range of Boss Attacks
        damaEN=True
        damage="boss"

# This is the AI of the Boss
    if xCapt > x0 +5:           
        x0+=speed                    
    elif xCapt < x0-5:   
        x0-=speed        
    if yCapt > y0 +5:
        y0+=speed
    elif yCapt < y0-5:
        y0-=speed
#===========================
    if alive==True: # as long as player is alive, score goes up by 5
        score+=5
    if x0<0 or x0>1000: #ensures boss doesn't go offscreen
        vx0*=-1 #velocity  
    if y0<0 or y0>800:
        vy0*=-1    
#==================================================
        #blit the pictures of Jump
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
#==================================================
        if keys[K_KP1]:# allows user to attack with the attack1 while jumping
            Walk() #allows movement/calls movement function
        Walk()
        move="jump"            

    elif ONGROUND==True and Attack==0: #if attack is nothing and run=True which means
        #left/right arrow keys are pressed
        #then blit the running sprite in the direction pressed
        if keys[K_LEFT] or keys[K_RIGHT]:
            if keys[K_RIGHT] and RunL==False:
                direction="right"
                RunR=True
                runsprite()
                Walk()
            elif keys[K_LEFT] and RunR==False:
                direction="left"
                RunL=True
                runsprite()
                Walk()
        if RunL==False and RunR==False and Stand==True:
            if keys[K_DOWN]:
                crouch=True

            if keys[K_KP_ENTER]: #if Enter key on keypad is pressed
                #taunt is true
                Taunt=True
            runsprite()  # allows for moving sprite
            #as long as the arrow keys for running are pressed   
        
        
    if move=="jump": # If move is jump
        yCapt-=17 #y coordinate of player is subtracted so image has jump motion
        ONGROUND=False # the flag for on  the ground is False
        if ONGROUND==False: # if sprite is off of the ground
            yCapt+=vyCapt    #add the velocity to get back to the Ground
            if yCapt == 400: #once the y coordinate is back to 400 which is on the ground
                yCapt = 400 
                vyCapt= 0# then the veolcity is back to 0 velocity is basicly gravity
                ONGROUND=True #the character would be on the ground again
                move="" #reset move
            vyCapt+=1 #add velocity by 1 to slowly bring character back to ground
            myClock.tick(60)
    
        
    if y0==800:
        y0=300

    if healthp1<=0: #if health of player is 0
        COLOUR=((0,0,0)) #colour of health text turns to black
        dama=False #damage is False
        damaEN=False
        enemyon=False
        alive=False
        screen.fill((0,0,0)) #fill screen with Black
        txtPosp2=arialFont2.render(("Game Over! Your score is "+str(score)),True,(red))#render text and show score
        screen.blit(txtPosp2,(0,200,100,100))
        txtPosReplay=arialFont2.render(("Replay"),True,(blue))#display replay option
        screen.blit(txtPosReplay,(replayrect))
        txtPosQuit=arialFont2.render((" Quit"),True,(blue))#display quit option
        screen.blit(txtPosQuit,(Quitrect))
        if Quitrect.collidepoint(mx,my): #if mouse hovers over the quit rectangle then 
            draw.rect(screen,(red),(Quitrect),3) #draw a red rectangle
            if mb[0]==1: #if they press it then quit =True
                Quit=True

        elif replayrect.collidepoint(mx,my): #if mouse hovers over this option
            draw.rect(screen,(red),(replayrect),3)#draws rect in Replay Rect
            if mb[0]==1:#if they click
                alive=True #resets match
                healthp1=5000#player health back to 5000
                enemyheath=10000 #enemy health back to 100000
                score=0 #score is rest
                againgame=True
                import adventure #imports this again so it will restart
                xCapt=500 #sets coordinates
                yCapt=400                

    if enemyhealth<=0 or score>=500000: #if the enemy dies or score reaches max score
        #same options as Loss just blits different Text
        dama=False
        damaEN=False
        enemyon=False
        alive=False
        screen.fill((0,0,0)) #fill screen with Black
        txtPosp2=arialFont2.render(("You WIN!!! Your score is "+str(score)),True,(red))
        screen.blit(txtPosp2,(0,200,100,100))
        txtPosReplay=arialFont2.render(("Replay"),True,(blue))
        screen.blit(txtPosReplay,(replayrect))
        txtPosQuit=arialFont2.render((" Quit"),True,(blue))
        screen.blit(txtPosQuit,(Quitrect))
        if Quitrect.collidepoint(mx,my):
            draw.rect(screen,(red),(Quitrect),3)
            if mb[0]==1:
                Quit=True                
                
            
                
        elif replayrect.collidepoint(mx,my):
            draw.rect(screen,(red),(replayrect),3)
            if mb[0]==1:
                alive=True
                healthp1=5000
                enemyheath=10000
                score=0

                againgame=True
                import adventure
                xCapt=500
                yCapt=400

              
    if againgame==True: #if "replay option is selected, resets all coordinates
        xCapt=300
        yCapt=400
        x0=500
        y0=0
        
        againgame=False
        startmatch() #calls the start match text function
        
    if damaEN==True: #if damage of enemy is true (evil small enemies)
        if damage=="e":
            healthp1-=5 #then player loses 5 health
            myClock.tick(30)
            damage=0 #resets damage which is the peron doing the damage
        
        elif damage=="boss":#if damage inflicted on player is boss then
            healthp1-=atk #player loses health based on the Boss's current atk stats
            myClock.tick(30)
            damage=0
            atk+=1
        damaEN=False

#=====================================
        #all the score and improvements to the Boss and Player
    if score==1000: 
        size+=1#size of boss increases
        atk+=1#attack of boss increases
        atkRANGE+=1#attack range of boss increases

    elif score>=5000 and score<=5500:
        screen.blit(rageghost,(x0-20,y0-20)) #blit the "RAGE" picture in the range mentioned
        atk+=1 #attack increases by 1
        
    elif score==10000: 
        atk+=4
        score+=20
        atkRANGE+=6
        speed+=1
        
    elif score==15000:
        enemyhealth+=200
        size-=5
        score+=20
        atk-=5
        
    elif score==20000:
        atk+=2
        speed+=1
        healthp1-=200
        score+=20

        atkRANGE+=2
        
    elif score>30000 and score <31000:
        healthp1+=1
        screen.blit(rageghost,(x0-20,y0-20))
        

    elif score>=50000 and score <=70000:
        screen.blit(rageghost,(x0-20,y0-20))
        healthp1+=1

    elif score>=60000 and score<=60700:
        atk+=1
        enemyhealth-=1
        healthp1-=1
        score+=1

    elif score==71000:
        atk+=1
        speed+=1
        score+=600
        
    elif score==50000:
        atk+=1
        healthp1-=2
        speed+=1
        score+=200

    elif score == 200000:
        enemyhealth-=5000
        score+=200        

    if enemyhealth==6000:
        score+=200
        speed+=1
        enemyhealth-=400
        
    elif enemyhealth==9000:
        score+=100
        atk+=2

    elif enemyhealth==4000:
        score+=100
        healthp1+=200
        speed+=2

    elif enemyhealth==0:
        score+=30000
#=====================================
        
    if Quit==True: #if the quit rect is preessed then
        quit() #quit program
        break

    if enemyon==True:
        #ditance formula for range of attacks for the small enemies
        dis=((xCapt-x)**2+(yCapt-y)**2)**.5
        dise1=((xCapt-x1)**2+(yCapt-y1)**2)**.5
        dise2=((xCapt-x2)**2+(yCapt-y2)**2)**.5
        dise3=((xCapt-x3)**2+(yCapt-y3)**2)**.5
        dise4=((xCapt-x4)**2+(yCapt-y4)**2)**.5
        dise5=((xCapt-x5)**2+(yCapt-y5)**2)**.5
        if dis<=30 or dise1<=30 or dise2<=30  or dise3<=30  or dise4<=30  or dise5<=30 :
            damaEN=True#damage is being inflicted if player is within range
            damage="e"

        # all the velocities of the small enemies
        x+=vx
        vy+=.1
        y+=vy
        x1+=vx1
        vy1+=.1
        y1+=vy1
        x2+=vx2
        vy2+=.1
        y2+=vy2
        x3+=vx3
        vy3+=.1
        y3+=vy3
      
        x4+=vx4
        vy4+=.1
        y4+=vy4
        x5+=vx5
        vy5+=.1
        y5+=vy5

        #blit pics at their locations
        screen.blit(enemypic,(x,int(y)))
        screen.blit(enemypic,(x1,int(y1)))
        screen.blit(enemypic,(x2,int(y2)))
        screen.blit(enemypic,(x3,int(y3)))
        screen.blit(enemypic,(x4,int(y4)))
        screen.blit(enemypic,(x5,int(y5)))

        # the boundaries of the screen 
       
        if x<0 or x>1000 :
            vx*=-1
        if y<0 or y>800:
            vy*=-1
        if x1<0 or x1>1000:
            vx1*=-1
        if y1<0 or y1>800:
            vy1*=-1
        if x2<0 or x2>1000:
            vx2*=-1
        if y2<0 or y2>800:
            vy2*=-1
        if x3<0 or x3>1000:
            vx3*=-1
        if y3<0 or y3>800:
            vy3*=-1
        if x4<0 or x4>1000:
            vx4*=-1
        if y4<0 or y4>800:
            vy4*=-1
        if x5<0 or x5>1000:
            vx5*=-1
        if y5<0 or y5>800:
            vy5*=-1
        #^ above makes enemies bounce off sides of walls
    
    healthdisplay() #call health display function
    scoredisplay()# call score display function
    offscreen(xCapt,yCapt) # call the function that checks if player is offscreen
    myClock.tick(30)
    display.flip()
quit()
            
