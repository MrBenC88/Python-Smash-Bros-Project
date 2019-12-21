#NEWpvp.py
#============================================
#FIX   #         
# FIX image loading-make it in the sprite list
#
#
#
#
#============================================
from pygame import*
from random import*
from math import*
#from game import*
from spritelist import* #import the spritelist program for 3d list references

init() #init all of pygame and python that needs initialting
screen=display.set_mode((1000,800))#set screen size
myClock=time.Clock()#sets the time module

lives1,lives2=3,3 #lives each player has
damagep1,damagep2=0,0

#mixer.music.load("Fairy Tail Natsu's Theme Extended   YouTube-[www_flvto_com].mp3")       # load a MUSIC object       
#mixer.music.play(-1) 
 
MAP=image.load("final destination.jpg") #load the map
Cscreen="Character Selection"
##mixer.music.load("Fairy Tail Soundtrack - Released Power.mp3") #play music infinite times
##mixer.music.play(-1)

xp1,yp1=300,400 #player 1 coordinates
xp2,yp2=700, 400 #player 2 coordinates

vyp1=2 #velocity
vyp2=2
#----------------------------------------
#Set Rectangle Coordinates and Height and Width
txtPosStartRect=Rect(500,300,30,30)
livesrect1=Rect(290,690,100,100)
livesrect2=Rect(590,690,100,100)
chaNAMErect1=Rect(300,770,100,100)
chaNAMErect2=Rect(600,770,100,100)

damagerect1=Rect(300,700,100,100)
damagerect2=Rect(600,700,100,100)
replayrect=Rect(400,500,200,100)
Quitrect=Rect(400,400,200,100)

#----------------------------------------

arialFontstart = font.SysFont("Times New Roman", 60) #Get font from system
arialFont2 = font.SysFont("Times New Roman", 70)
livestxt=font.SysFont("Times New Roman", 14)
NAMEStxt=font.SysFont("Times New Roman", 16)

frame=0 #frame in which the characters move-Animation 
DAMAGECOLOUR=((255,0,0)) #the damage colour
LIFECOLOUR=((255,255,255)) #the lifecolour

frameF=0 #frame counters for the range attacks
frameF1=0
waterF=0
waterF1=0
arrowframe1=0
arrowframe2=0
#=======================================
#Flags essential for direction, if character
#on the ground,if character gets hit, etc.
#Marks all conditions that could be presented
ONGROUND1=True
ONGROUND2=True
hit1=False
hit2=False
stand1=True
stand2=True
RunL=False
RunR=False
RunL2=False
RunR2=False
lhit1=False
rhit1=False
lhit2=False
rhit2=False

Jump1=False
Jump2=False
hit=False #a flag marking if the player is hit or not-used for miss hits
right1=True
left1=False
right2=False
left2=True
move=False
Moving=False
move1=False
move2=False
Attacking1=False
Attacking2=False

Block1R=False
Block2R=False
Block1L=False
Block2L=False
#===================================
#Range Attack Flags
#Natsu
FireballAtkR2=False
FireballAtkL2=False
FireballAtkR1=False
FireballAtkL1=False
#Gajeel
MetalAtkR1=False
MetalAtkL1=False
MetalAtkR2=False
MetalAtkL2=False
#Wendy
WaterAtkR1=False
WaterAtkL1=False
WaterAtkR2=False
WaterAtkL2=False
WaterRoarAtkR1=False
WaterRoarAtkL1=False
WaterRoarAtkR2=False
WaterRoarAtkL2=False
#Grey
BowAtkR1=False
BowAtkL1=False
BowAtkR2=False
BowAtkL2=False


#===================================
#Range Attacks Added values to the "x"
addon=10
addon1=10
#===================================
Attackone=0 #attack one and attacktwo are 0 which is a "no" attack
Attacktwo=0
#frame counters for all the other moves
frame=0
frame1=0
frame2=0
total1=0
total2=0
pictures1=0
pictures2=0

direct1="right" #the default direction of the 2 players
direct2="left"

attacktypep1="" #there is no attacktype when the match begins
attacktypep2=""

display.init()   # <--Must have for caption
display.set_caption("Clash of The FairyTail") #displays the caption

#font for the Character Selection Screen
font = font.SysFont("Times New Roman", 20)
background=image.load("CharacterSelect.png")
background2=image.load("CharacterSelect.png")
background3=image.load("CharacterSelect.png")
background4=image.load("CharacterSelect.png")
screen.blit(background,(0,0))

#load character images 
napic=image.load("natzupic.png")
erpic=image.load("erzapic.png")
grepic=image.load("greypic.png")
gajpic=image.load("gajeelpic2.png")
frpic=image.load("freedpic.png")
lupic=image.load("lucypic.png")
wepic=image.load("wendypic.png")


##Character Rects
NatRect=Rect(49,121,140,121)
GreyRect=Rect(49,294,140,121)
ErRect=Rect(49,459,140,121)
GajRect=Rect(824,121,140,121)
FreRect=Rect(824,294,140,121)
LuRect=Rect(824,459,140,121)
WenRect=Rect(431,605,140,121)
##Player 1 Select and Player 2 Select
Player1Rect=Rect(300,676,145,33)
Player2Rect=Rect(650,676,145,33)
###Options and Back Rects and Intructions Rect
optionRect=Rect(414,11,173,44)
backRect=Rect(801,11,173,44)
intructions1Rect=(12,674,200,100)
intructions2Rect=(780,674,200,100)
#==============================================================================

blue=((0,100,255))

char1SELECT=""   #character that player 1 selects
char2SELECT=""  #character that player 2 selects

char1=""
char2=""
cha1=0
cha2=0

running=True
count=0
click=False
click1=False
click2=False
#==============================================================================

def confirm(char1,char2): #confirm blits the character's pics and return
    global cha1,cha2
    if char1=="Na":
        cha1=0
        screen.blit(napic,(260,21,300,500))
    elif char1=="Gr":
        cha1=1        
        screen.blit(grepic,(220,160,300,500))
    elif char1=="Er":
        cha1=2
        screen.blit(erpic,(300,160,300,500))
    elif char1=="Ga":
        cha1=4
        screen.blit(gajpic,(300,160,300,500))
    elif char1=="Fr":
        cha1=5
        screen.blit(frpic,(0,50,300,500))
    elif char1=="Lu":
        cha1=6
        screen.blit(lupic,(355,160,300,500))
    elif char1=="We":
        cha1=3
        screen.blit(wepic,(300,235,300,500))
        
    if char2=="Na":
        cha2=0
        screen.blit(napic,(550,21,300,500))
    elif char2=="Gr":
        cha2=1
        screen.blit(grepic,(540,160,300,500))
    elif char2=="Er":
        cha2=2
        screen.blit(erpic,(600,160,300,500))
    elif char2=="Ga":
        cha2=4
        screen.blit(gajpic,(600,160,300,500))
    elif char2=="Fr":
        cha2=5
        screen.blit(frpic,(280,50,300,500))
    elif char2=="Lu":
        cha2=6
        screen.blit(lupic,(650,160,300,500))
    elif char2=="We":
        cha2=3
        screen.blit(wepic,(600,235,300,500))

    return cha1,cha2 #returns the cha1 and cha2 which are positions
    # in the 3d list that helps in selection of moves
#==============================================================================
#=============================EVENT LOOP=======================================
#==============================================================================
    
while running:
    for evnt in event.get():                
        if evnt.type == QUIT:
            if char1 !="" and char2 !="":
                
                break
                #import Newpvp
                running = False
            else:
                break

            
    keys = key.get_pressed()
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    if mb[0]==1 or mb[2]==1 or mb[0]==1 and mb[2]==1: #ensures that mouse got clicked
        click=True #then click
    
    if NatRect.collidepoint(mx,my): # if mouse hovers over the Character pic
        draw.rect(screen,blue,NatRect,2) #draws a blue rectangle in the location of the picture
        if mb[0]==1:
            screen.blit(background,(0,0))
            char1SELECT="Natsu" #variables that are essentila for loading the specific sprites
            char1="Na" #of each character

        if mb[2]==1:
            screen.blit(background,(0,0))
            char2SELECT="Natsu"
            char2="Na"
          
            
    elif GreyRect.collidepoint(mx,my):
        draw.rect(screen,blue,GreyRect,2)
        if mb[0]==1:
            screen.blit(background,(0,0))            
            char1SELECT="Grey"
            char1="Gr"

        if mb[2]==1:
            screen.blit(background,(0,0))
            char2SELECT="Grey"
            char2="Gr"

            
    elif ErRect.collidepoint(mx,my):
        draw.rect(screen,blue,ErRect,2)
        if mb[0]==1:
            screen.blit(background,(0,0))
            char1SELECT="Erza"
            char1="Er"
           
        if mb[2]==1:
            screen.blit(background,(0,0))
            char2SELECT="Erza"
            char2="Er"
             
            
    elif GajRect.collidepoint(mx,my):
        draw.rect(screen,blue,GajRect,2)
        if mb[0]==1:
            screen.blit(background,(0,0))
            char1SELECT="Gajeel"
            char1="Ga"

        if mb[2]==1:
            screen.blit(background,(0,0))
            char2SELECT="Gajeel"
            char2="Ga"

            
    elif FreRect.collidepoint(mx,my):
        draw.rect(screen,blue,FreRect,2)
        if mb[0]==1:
            screen.blit(background,(0,0))
            char1SELECT="Freed"
            char1="Fr"

        if mb[2]==1:
            screen.blit(background,(0,0))
            char2SELECT="Freed"
            char2="Fr"

            
    elif LuRect.collidepoint(mx,my):
        draw.rect(screen,blue,LuRect,2)
        if mb[0]==1:
            screen.blit(background,(0,0))
            char1SELECT="Lucy"
            char1="Lu"

        if mb[2]==1:
            screen.blit(background,(0,0))
            char2SELECT="Lucy"
            char2="Lu"

            
    elif WenRect.collidepoint(mx,my):
        draw.rect(screen,blue,WenRect,2)
        if mb[0]==1:
            screen.blit(background,(0,0))
            char1SELECT="Wendy"
            char1="We"

        if mb[2]==1:
            screen.blit(background,(0,0))
            char2SELECT="Wendy"
            char2="We"
#==============================================================================  
    elif backRect.collidepoint(mx,my): #if mouse hovers over the back rectangle
        draw.rect(screen,blue,backRect,2) #draw blue rectangle
        if mb[0]==1 or mb[2]==1 and click==True: #if they click switch screens
            import FINALgame
            
    if keys[K_RETURN]: #press enter key and breaks this loop
        if char1 != "" and char2 != "":  #makes sure that characters are chosen :)
            break
            
    elif click==True: 
        confirm(char1,char2)#calls confirm to let us get variables from the character select
#==============================================================================
        
    txtp1=font.render((char1SELECT),True,(0,100,255)) #render the text so user knows what to do
    txtp2=font.render((char2SELECT),True,(0,100,255))
    txtintructions1=font.render("Left Click for Player 1",True,(0,100,255))
    txtintructions2=font.render("Right Click for Player 2",True,(0,100,255))
    screen.blit(txtintructions1,intructions1Rect)
    screen.blit(txtintructions2,intructions2Rect)
    screen.blit(txtp1,Player1Rect)
    screen.blit(txtp2,Player2Rect)#blit the text

    display.flip()
    


#=============================================================================
#===============================Functions=====================================
#=============================================================================


def startmatch(): # startmatch functions to blit the countdown before the match commences
    screen.fill((255,255,255)) #fills screen with white
    time.wait(200)
    for i in range(0,4): #for i in range for because it displays 3 numbers and a word
        screen.fill((255,255,255))
        num=3-i #subtract 3 so that it starts with 3 and decreases to zero
        txtPosStart=arialFontstart.render(str(num),True,(255,0,0)) #render the number
        if num==0: #if the number=0 then render the word FIGHT so that zero is not displayed
            txtPosStart=arialFontstart.render(str("FIGHT"),True,(255,0,0))
            screen.blit(txtPosStart,(450,300,200,200))#blit the text
        time.wait(1000)
        if num!=0:
            screen.blit(txtPosStart,txtPosStartRect)# if number is not equal to zero then blit the number
        display.flip()

def walk():
    global xp1,xp2, RunR, RunL,RunR2,RunL2
    #move to the Left
    if keys[K_a]: #funtions to move player to right,left for both players whenever a specific key is pressed
        Moving=True
        RunR=False
        RunL=True        
        move1=True
        left1=True
        right1=False
        direct1="left"
        xp1-=30

            
    #move to the right 
    if keys[K_d]:
        direct1="right"
        Moving=True
        RunR=True
        RunL=False        
        move1=True
        left1=False
        right1=True
        xp1+=30

#________________________________
    if keys[K_LEFT]:
        direct2="left"
        Moving=True
        RunR2=False
        RunL2=True       
        move2=True
        left2=True
        right2=False        
        xp2-=30

            
 
    if keys[K_RIGHT]:
        direct2="right"
        Moving=True
        RunR2=True
        RunL2=False
        move2=True
        left2=False
        right2=True
        xp2+=30


    move1=False #move is false if key isn't pressed anymore
    move2=False
    Moving=False

def Taunt(xp1,yp1,xp2,yp2,cha1,cha2):
    global Jump1, Jump2
    tauntpicp1=image.load(char1SELECT+"\\"+char1+"Taunt.png" ) #load taunt pics
    tauntpicp2=image.load(char2SELECT+"\\"+char2+"Taunt.png" )
    
    if keys[K_SPACE] and Jump1==False and ONGROUND1==True and keys[K_a]!=1 and keys[K_d]!=1 and keys[K_s]!=1 and keys[K_g]!=1 and keys[K_h]!=1 and keys[K_k]!=1:
        screen.blit(tauntpicp1,(xp1,yp1))#if above conditions are met then blit desired taunt pic

    if keys[K_KP0] and Jump2==False and ONGROUND2==True and keys[K_RIGHT]!=1 and keys[K_LEFT]!=1 and keys[K_DOWN]!=1 and keys[K_KP1]!=1 and keys[K_KP2]!=1 and keys[K_KP3]!=1:
        screen.blit(tauntpicp2,(xp2,yp2))
            
def MovementPic1(xp1,yp1,xp2,yp2,cha1,cha2):
#run to the right ===================================================================
    global RunR, RunL,direction,crouch,frame, direct1, direct2,Attacking1,Attacking2, Jump1, Jump2
                          
    if keys[K_d]and RunR==True and Attacking1==False and Jump1==False :
        direct1="right" #sets direction to the right
        stand1=False #stand is now false since the player is moving
        total=len(sprite[cha1][1]) #the total  number of sprites in the 3d sprite list
        if frame >= total: #this prevents the list"frame" from going out of range
            frame = 0   #sets frame to zero      
        pictures=sprite[cha1][1][frame] # a 3d list that goes character, move, frame
        screen.blit(pictures,(xp1,yp1))#blit the pics
        frame+=1 #add 1 to the frame until it reaches the total 

#run to the left ====================================================================
    if keys[K_a] and RunL==True and Attacking1==False and Jump1==False:
        stand1=False  #stand is now false since the player is moving
        direct1="left" #sets direction to the left 
        total=len(sprite[cha1][0]) #the total  number of sprites in the 3d sprite list
        if frame >= total: #this prevents the list"frame" from going out of range
            frame = 0    #sets frame to zero     
        pictures=sprite[cha1][0][frame] # a 3d list that goes chaacter, move, frame
        screen.blit(pictures,(xp1,yp1))
        frame+=1


    RunL=False
    RunR=False

def MovementPic2(xp1,yp1,xp2,yp2,cha1,cha2):
#run to the right ===================================================================
    
    global RunR, RunL,direction,crouch,frame, direct1, direct2,Attacking1,Attacking2, Jump1, Jump2
    
#run to the right ===================================================================
    if keys[K_RIGHT] and RunR2==True and Attacking2==False and Jump2==False: #comments are same as MovementPic1
        direct2="right"
        stand2=False
        total=len(sprite[cha2][1])
        if frame >= total:
            frame = 0        
        pictures=sprite[cha2][1][frame] # a 3d list that goes chaacter, move, frame
        screen.blit(pictures,(xp2,yp2))
        frame+=1


#run to the left ====================================================================
    if keys[K_LEFT] and RunL2==True and Attacking2==False and Jump2==False:
        direct2="left"
        stand2=False
        total=len(sprite[cha2][0])
        if frame >= total:
            frame = 0        
        pictures=sprite[cha2][0][frame] # a 3d list that goes chaacter, move, frame
        screen.blit(pictures,(xp2,yp2))
        frame+=1    
            
    
def crouch(xp1,yp1,xp2,yp2,right1,left1,right2,left2,char1,char2):
    '''crouch animation'''
    global Jump1,Jump2
 
    ch1pic=image.load(char1SELECT+"\\"+char1+"CrouchR.png" ) #load crouch pic
    ch2pic=image.load(char2SELECT+"\\"+char2+"CrouchL.png" )
    if keys[K_s] and Jump1==False and keys[K_a]!=1 and keys[K_d]!=1 and keys[K_g]!=1 and keys[K_h]!=1 and keys[K_k]!=1 and keys[K_t]!=1:
        screen.blit(ch1pic,(xp1,yp1))#if it satifies above conditions then blit the crouch

    if keys[K_DOWN]and Jump2==False and keys[K_RIGHT]!=1 and keys[K_LEFT]!=1 and keys[K_KP1]!=1 and keys[K_KP2]!=1 and keys[K_KP3]!=1 and keys[K_KP_ENTER]!=1:
        screen.blit(ch2pic,(xp2,yp2))

            
def damagedisplay(char1SELECT,char2SELECT): #this function displays the damage taken per player
    '''dislays damage percentage that both players have gained'''
    global txtPos,txtPos1
    damgdisplay1=image.load(char1SELECT+".png") #loads the character's pic 
    damgdisplay2=image.load(char2SELECT+".png")
    txtPos=arialFont2.render((str(damagep1)+"%"),True,(DAMAGECOLOUR)) #render the damage value
    txtPos2=arialFont2.render((str(damagep2)+"%"),True,(DAMAGECOLOUR))
    screen.blit(txtPos2,damagerect2)#blit the text 
    screen.blit(txtPos,damagerect1)
    screen.blit(damgdisplay1,(250,700,100,100))#blit the picture of character next to the damage
    screen.blit(damgdisplay2,(550,700,100,100))
    chadisplayname1=NAMEStxt.render((char1SELECT),True,(LIFECOLOUR))#render the character's name
    chadisplayname2=NAMEStxt.render((char2SELECT),True,(LIFECOLOUR))
    screen.blit(chadisplayname1,(chaNAMErect1))#blit the character's name underneath the damage value
    screen.blit(chadisplayname2,(chaNAMErect2))
    
def livesdisplay(): #this shows the number of lives each player has remaining
    '''dislays lives of the players'''
    global lifetxt1,lifetxt2
    lifetxt1=livestxt.render(("Player 1 Lives: "+(str(lives1))),True,(LIFECOLOUR)) #render the value for lives
    lifetxt2=livestxt.render(("Player 2 Lives: "+(str(lives2))),True,(LIFECOLOUR))
    screen.blit(lifetxt1,livesrect1)#blit the life text
    screen.blit(lifetxt2,livesrect2)

#=========================================================================================================
#=========================================================================================================
#=========================================================================================================
#=========================================================================================================
#=========================================================================================================    
def EndGame(lives1,lives2):
    '''displays the game over screen'''
    global LIFECOLOUR, xp1,yp1,xp2,yp2
    if lives1==0 or lives2==0:
        screen.fill((0,0,0))
    if lives1==0:
        endgametxt=arialFont2.render(("Player 2 Wins!"),True,(255,255,255))
        screen.blit(endgametxt,(300,200,100,100))
        txtPosReplay=arialFont2.render(("Replay"),True,(0,0,255))
        screen.blit(txtPosReplay,(replayrect))
        txtPosQuit=arialFont2.render((" Quit"),True,(0,0,255))
        screen.blit(txtPosQuit,(Quitrect))
        if Quitrect.collidepoint(mx,my):
            draw.rect(screen,(255,0,0),(Quitrect),3)
            #Import Menu/ switch screens
            if mb[0]==1:
                import FINALgame
        elif replayrect.collidepoint(mx,my):
            draw.rect(screen,(255,0,0),(replayrect),3)
            if mb[0]==1:
                import NEWpvp
                lives1=3
                lives2=3
                xp1,yp1=300,400
                xp2,yp2=700,400
                damagep1,damagep2=0,0
            
                
    elif lives2==0:
        endgametxt=arialFont2.render(("Player 1 Wins!"),True,(255,255,255))
        screen.blit(endgametxt,(300,200,100,100))
        txtPosReplay=arialFont2.render(("Replay"),True,(0,0,255))
        screen.blit(txtPosReplay,(replayrect))
        txtPosQuit=arialFont2.render((" Quit"),True,(0,0,255))
        screen.blit(txtPosQuit,(Quitrect))
        if Quitrect.collidepoint(mx,my):
            draw.rect(screen,(255,0,0),(Quitrect),3)
            #Import Menu/ switch screens
            if mb[0]==1:
                import FINALgame
        elif replayrect.collidepoint(mx,my):
            draw.rect(screen,(255,0,0),(replayrect),3)
            if mb[0]==1:
                import NEWpvp
                lives1=3
                lives2=3
                xp1,yp1=300,400
                xp2,yp2=700,400
                damagep1,damagep2=0,0        
                        

    return lives1,lives2

#=========================================================================================================
#=========================================================================================================
#=========================================================================================================
#=========================================================================================================
#=========================================================================================================         


        
def stand(name,charactersym,x,y,playernum,direct):
    sRightpic=image.load(name+"\\"+charactersym+"StandR.png" )#load stand pics
    sLeftpic=image.load(name+"\\"+charactersym+"StandL.png" )
    
    if playernum==1: #if player is 1st player
        stand1=False #stand1=False
        if direct=="right":
            screen.blit(sRightpic,(x,y))#blits the Right Stand Picture

        elif direct=="left":
            screen.blit(sLeftpic,(x,y))                
    if playernum==2:
        stand2=False
        if direct=="right":
            screen.blit(sRightpic,(x,y))

        elif direct=="left":
            screen.blit(sLeftpic,(x,y))              


def Attack1(Attack, direction,cha,dist):
    global xp1, yp1,frame, xp2,yp2, right1,left1, damagep2,hit1, FireballAtkR1,FireballAtkL1,MetalAtkR1,MetalAtkL1,WaterAtkR1,WaterAtkL1,WaterRoarAtkR1,WaterRoarAtkL1,BowAtkR1,BowAtkL1,Block2R,Block2L
#=========================================================================================================
    # These are the range attacks 
    if char1=="Na" and Attack==3 and direction=="right" :
        FireballAtkR1=True
        
    if char1=="Na" and Attack==3 and direction=="left" :
        FireballAtkL1=True
    if char1=="Ga" and Attack==3 and direction=="right" :
        MetalAtkR1=True
        
    if char1=="Ga" and Attack==3 and direction=="left" :
        MetalAtkL1=True

    if char1=="We" and Attack==3 and direction=="right" :
        WaterAtkR1=True
        
    if char1=="We" and Attack==3 and direction=="left":
        WaterAtkL1=True
        
    if char1=="We" and Attack==2 and direction=="right" :
        WaterRoarAtkR1=True
        
    if char1=="We" and Attack==2 and direction=="left"  :
        WaterRoarAtkL1=True

    if char1=="Gr" and Attack==2 and direction=="right" :
        BowAtkR1=True
        
    if char1=="Gr" and Attack==2 and direction=="left" :
        BowAtkL1=True
#=========================================================================================================
       
        
    if direction=="right" :
        if Attack==1:
            total=len(sprite[cha1][1]) #gets total of the list selected
            if frame >= total: #ensures list doesn't go out of range
                frame = 0       #sets frame to 0 
            pictures=sprite[cha1][5][frame] # a 3d list that goes character, move, frame
            screen.blit(pictures,(xp1,yp1)) #blits the picture
            frame+=1 #add 1 to the frame until it reaches thr total

            if xp2>xp1 : #if 2nd player is on the right side of player1
                if char1=="Na"and dist<=48 and Block2L!=True: #if player is the set range (dis) away from player 
                    damagep2+=4+damagep2//1000 #then deal the set amount of damage which varies depending on the damaged player's damgage already
                    hit1=True #hit is true since the hit has inflicted damage
                if char1=="Gr"and dist<=55 and Block2L!=True:
                    damagep2+=7+damagep2//1000
                    hit1=True
                if char1=="Er"and dist<=48 and Block2L!=True:
                    damagep2+=3+damagep2//1000
                    hit1=True
                if char1=="Ga"and dist<=45 and Block2L!=True:
                    damagep2+=8+damagep2//1000
                    hit1=True
                if char1=="Fr"and dist<=46 and Block2L!=True:
                    damagep2+=2+damagep2//1000
                    hit1=True
                if char1=="Lu" and dist<=81 and Block2L!=True:
                    damagep2+=4+damagep2//1000
                    hit1=True
                if char1=="We" and dist<=43 and Block2L!=True:
                    damagep2+=2+damagep2//1000
                    hit1=True

        if Attack==2: #same comments as Attack1
            total=len(sprite[cha1][7])
            if frame >= total:
                frame = 0            
            pictures=sprite[cha1][7][frame] # a 3d list that goes character, move, frame
            screen.blit(pictures,(xp1,yp1))
            frame+=1
            if xp2>xp1:
                if char1=="Na"and dist<=50 and Block2L!=True:
                    damagep2+=8+damagep2//1000
                    hit1=True

                if char1=="Er"and dist<=42 and Block2L!=True:
                    damagep2+=10+damagep2//1000
                    hit1=True
                if char1=="Ga"and dist<=121 and Block2L!=True:
                    damagep2+=5+damagep2//1000
                    hit1=True
                if char1=="Fr"and dist<=45 and Block2L!=True:
                    damagep2+=14+damagep2//1000
                    hit1=True
                if char1=="Lu" and dist<=40 and Block2L!=True:
                    damagep2+=12+damagep2//1000
                    hit1=True

            
        if Attack==3: #same comments as Attack1
            total=len(sprite[cha1][9])
            if frame >= total:
                frame = 0            
            pictures=sprite[cha1][9][frame] # a 3d list that goes chaacter, move, frame
            screen.blit(pictures,(xp1,yp1))
            frame+=1
            if xp2>xp1:
                if char1=="Gr"and dist<=75 and Block2L!=True:
                    damagep2+=14+damagep2//1000
                    hit1=True
                if char1=="Er"and dist<=45 and Block2L!=True:
                    damagep2+=10+damagep2//1000
                    hit1=True

                if char1=="Fr"and dist<=46 and Block2L!=True:
                    damagep2+=19+damagep2//1000
                    hit1=True
                if char1=="Lu" and dist<=80 and Block2L!=True:
                    damagep2+=14+damagep2//1000
                    hit1=True

    if direction=="left":
        if Attack==1:
            total=len(sprite[cha1][4]) #total values in the 3d list
            if frame >= total:#sets limit so that frame never goes out of range
                frame = 0         #if limit is reached then sets the frame "list" to 0   
            pictures=sprite[cha1][4][frame] # a 3d list that goes chaacter, move, frame
            screen.blit(pictures,(xp1,yp1)) #blit the picture
            frame+=1# add 1 to frame to switch the picture
            if xp1>xp2:#if the 2nd player is on left side of 1st player 
                if char1=="Na"and dist<=48  and Block2R!=True: #same comments as Attack1
                    damagep2+=4+damagep2//1000
                    hit1=True
                if char1=="Gr"and dist<=55 and Block2R!=True:
                    damagep2+=7+damagep2//1000
                    hit1=True
                if char1=="Er"and dist<=48 and Block2R!=True:
                    damagep2+=3+damagep2//1000
                    hit1=True
                if char1=="Ga"and dist<=45 and Block2R!=True:
                    damagep2+=8+damagep2//1000
                    hit1=True
                if char1=="Fr"and dist<=46 and Block2R!=True:
                    damagep2+=2+damagep2//1000
                    hit1=True
                if char1=="Lu" and dist<=81 and Block2R!=True:
                    damagep2+=4+damagep2//1000
                    hit1=True
                if char1=="We" and dist<=43 and Block2R!=True:
                    damagep2+=2+damagep2//1000
                    hit1=True

        if Attack==2: #same comments as Attack1
            total=len(sprite[cha1][6])
            if frame >= total:
                frame = 0            
            pictures=sprite[cha1][6][frame] # a 3d list that goes chaacter, move, frame
            screen.blit(pictures,(xp1,yp1))
            frame+=1
            if xp1>xp2:
                if char1=="Na"and dist<=50 and Block2R!=True:
                    damagep2+=8+damagep2//1000
                    hit1=True

                if char1=="Er"and dist<=42 and Block2R!=True:
                    damagep2+=10+damagep2//1000
                    hit1=True
                if char1=="Ga"and dist<=121 and Block2R!=True:
                    damagep2+=5+damagep2//1000
                    hit1=True
                if char1=="Fr"and dist<=45 and Block2R!=True:
                    damagep2+=14+damagep2//1000
                    hit1=True
                if char1=="Lu" and dist<=40 and Block2R!=True:
                    damagep2+=12+damagep2//1000
                    hit1=True



        if Attack==3: #same comments as Attack1
            total=len(sprite[cha1][8])
            if frame >= total:
                frame = 0            
            pictures=sprite[cha1][8][frame] # a 3d list that goes chaacter, move, frame
            screen.blit(pictures,(xp1,yp1))
            frame+=1
            if xp1>xp2:

                if char1=="Gr"and dist<=75 and Block2R!=True:
                    damagep2+=14+damagep2//1000
                    hit1=True
                if char1=="Er"and dist<=45 and Block2R!=True:
                    damagep2+=10+damagep2//1000
                    hit1=True
                if char1=="Fr"and dist<=46 and Block2R!=True:
                    damagep2+=19+damagep2//1000
                    hit1=True
                if char1=="Lu" and dist<=80 and Block2R!=True:
                    damagep2+=14+damagep2//1000
                    hit1=True
            return damagep2 #return the damage inflicted 
        
def Attack2(Attack, direction,cha,dist): #same comments as Attack1

    global xp2, yp2, frame, xp2, yp2,right2,left2,damagep1,hit2,FireballAtkR2,FireballAtkL2,MetalAtkR2,MetalAtkL2,WaterAtkR2,WaterAtkL2,WaterRoarAtkR2,WaterRoarAtkL2,BowAtkR2,BowAtkL2,Block1R,Block1L

    
    if char2=="Na" and Attack==3 and direction=="right" :
        FireballAtkR2=True
        
    if char2=="Na" and Attack==3 and direction=="left"  :
        FireballAtkL2=True
    if char2=="Ga" and Attack==3 and direction=="right"  :
        MetalAtkR2=True
        
    if char2=="Ga" and Attack==3 and direction=="left"  :
        MetalAtkL2=True

    if char2=="We" and Attack==3 and direction=="right"  :
        WaterAtkR2=True
        
    if char2=="We" and Attack==3 and direction=="left"  :
        WaterAtkL2=True

    if char2=="We" and Attack==2 and direction=="right"  :
        WaterRoarAtkR2=True
        
    if char2=="We" and Attack==2 and direction=="left" :
        WaterRoarAtkL2=True

    if char2=="Gr" and Attack==2 and direction=="right"  :
        BowAtkR2=True
        
    if char2=="Gr" and Attack==2 and direction=="left"  :
        BowAtkL2=True         
        
    if direction=="right":
        if Attack==1:
            total=len(sprite[cha2][5])
            if frame >= total:
                frame = 0            
            pictures=sprite[cha2][5][frame] # a 3d list that goes character, move, frame
            screen.blit(pictures,(xp2,yp2))
            frame+=1

            if xp1>xp2:
                if char2=="Na"and dist<=48  and Block1L!=True:
                    damagep1+=4+damagep1//1000
                    hit2=True
                if char2=="Gr"and dist<=55 and Block1L!=True:
                    damagep1+=7+damagep1//1000
                    hit2=True
                if char2=="Er"and dist<=48 and Block1L!=True:
                    damagep1+=3+damagep1//1000
                    hit2=True
                if char2=="Ga"and dist<=45 and Block1L!=True:
                    damagep1+=8+damagep1//1000
                    hit2=True
                if char2=="Fr"and dist<=46 and Block1L!=True:
                    damagep1+=2+damagep1//1000
                    hit2=True
                if char2=="Lu" and dist<=81 and Block1L!=True:
                    damagep1+=4+damagep1//1000
                    hit2=True
                if char2=="We" and dist<=43 and Block1L!=True:
                    damagep1+=2+damagep1//1000
                    hit2=True

        if Attack==2:
            total=len(sprite[cha2][7])
            if frame >= total:
                frame = 0            
            pictures=sprite[cha2][7][frame] # a 3d list that goes character, move, frame
            screen.blit(pictures,(xp2,yp2))
            frame+=1
            
            if xp1>xp2:
                if char2=="Na"and dist<=50 and Block1L!=True:
                    damagep1+=8+damagep1//1000
                    hit2=True

                if char2=="Er"and dist<=42 and Block1L!=True:
                    damagep1+=10+damagep1//1000
                    hit2=True
                if char2=="Ga"and dist<=121 and Block1L!=True:
                    damagep1+=5+damagep1//1000
                    hit2=True
                if char2=="Fr"and dist<=45 and Block1L!=True:
                    damagep1+=14+damagep1//1000
                    hit2=True
                if char2=="Lu" and dist<=40 and Block1L!=True:
                    damagep1+=12+damagep1//1000
                    hit2=True
            
        if Attack==3:
          
            total=len(sprite[cha2][9])
            if frame >= total:
                frame = 0            
            pictures=sprite[cha2][9][frame] # a 3d list that goes character, move, frame
            screen.blit(pictures,(xp2,yp2))
            frame+=1
            if xp1>xp2:
                    
                if char2=="Gr"and dist<=75 and Block1L!=True:
                    damagep1+=14+damagep1//1000
                    hit2=True
                if char2=="Er"and dist<=45 and Block1L!=True:
                    damagep1+=10+damagep1//1000
                    hit2=True
                if char2=="Fr"and dist<=46 and Block1L!=True:
                    damagep1+=19+damagep1//1000
                    hit2=True
                if char2=="Lu" and dist<=80 and Block1L!=True:
                    damagep1+=14+damagep1//1000
                    hit2=True
                
    if direction=="left":
        if Attack==1:
            total=len(sprite[cha2][4])
            if frame >= total:
                frame = 0            
            pictures=sprite[cha2][4][frame] # a 3d list that goes character, move, frame
            screen.blit(pictures,(xp2,yp2))
            frame+=1
            if xp2>xp1:
                if char2=="Na"and dist<=48 and Block1R!=True:
                    damagep1+=4+damagep1//1000
                    hit2=True
                if char2=="Gr"and dist<=55 and Block1R!=True:
                    damagep1+=7+damagep1//1000
                    hit2=True
                if char2=="Er"and dist<=48 and Block1R!=True:
                    damagep1+=3+damagep1//1000
                    hit2=True
                if char2=="Ga"and dist<=45 and Block1R!=True:
                    damagep1+=8+damagep1//1000
                    hit2=True
                if char2=="Fr"and dist<=46 and Block1R!=True:
                    damagep1+=2+damagep1//1000
                    hit2=True
                if char2=="Lu" and dist<=81 and Block1R!=True:
                    damagep1+=4+damagep1//1000
                    hit2=True
                if char2=="We" and dist<=43 and Block1R!=True:
                    damagep1+=2+damagep1//1000
                    hit2=True

        if Attack==2:
            total=len(sprite[cha2][6])
            if frame >= total:
                frame = 0            
            pictures=sprite[cha2][6][frame] # a 3d list that goes character, move, frame
            screen.blit(pictures,(xp2,yp2))
            frame+=1
            if xp2>xp1:
                if char2=="Na"and dist<=50 and Block1R!=True:
                    damagep1+=8+damagep1//1000
                    hit2=True

                if char2=="Er"and dist<=42 and Block1R!=True:
                    damagep1+=10+damagep1//1000
                    hit2=True
                if char2=="Ga"and dist<=121 and Block1R!=True:
                    damagep1+=5+damagep1//1000
                    hit2=True
                if char2=="Fr"and dist<=45 and Block1R!=True:
                    damagep1+=14+damagep1//1000
                    hit2=True
                if char2=="Lu" and dist<=40 and Block1R!=True:
                    damagep1+=12+damagep1//1000
                    hit2=True

        if Attack==3:
            total=len(sprite[cha2][8])
            if frame >= total:
                frame = 0            
            pictures=sprite[cha2][8][frame] # a 3d list that goes character, move, frame
            screen.blit(pictures,(xp2,yp2))
            frame+=1
            if xp2>xp1:

                if char2=="Gr"and dist<=75 and Block1R!=True:
                    damagep1+=14+damagep1//1000
                    hit2=True
                if char2=="Er"and dist<=45 and Block1R!=True:
                    damagep1+=10+damagep1//1000
                    hit2=True

                if char2=="Fr"and dist<=46 and Block1R!=True:
                    damagep1+=19+damagep1//1000
                    hit2=True
                if char2=="Lu" and dist<=80 and Block1R!=True:
                    damagep1+=14+damagep1//1000
                    hit2=True

            return damagep1 #returns the damage inflicted
        
def jumpPic(name,charactersym,x,y,playernum,direct): # the Jump function which loads and blits the picture
    jumpingR=image.load(name+"\\"+charactersym+"JumpR.png" )#load image
    jumpingL=image.load(name+"\\"+charactersym+"JumpL.png" )
    
    if playernum==1:
        stand1=False
        if direct=="right":
            screen.blit(jumpingR,(x,y))

        elif direct=="left":
            screen.blit(jumpingL,(x,y))

    if playernum==2:
        stand2=False
        if direct=="right":
            screen.blit(jumpingR,(x,y))

        elif direct=="left":
            screen.blit(jumpingL,(x,y))
                
def jumpMove(): # a function that allows user to jump and control jump in mid air

    global xp1,xp2, RunR, RunL,RunR2,RunL2
    #move to the Left
    if keys[K_a]:
        Moving=True
        RunR=False
        RunL=True        
        move1=True
        left1=True
        stand1=False
        right1=False
        direct1="left"
        xp1-=10

            
    #move to the right 
    if keys[K_d]:
        direct1="right"
        Moving=True
        RunR=True
        RunL=False        
        move1=True
        left1=False
        stand1=False
        right1=True
        xp1+=10
#_______________________________
    if keys[K_LEFT]:
        direct2="left"
        Moving=True
        RunR2=False
        RunL2=True       
        move2=True
        left2=True
        stand2=False
        right2=False        
        xp2-=10          
 
    if keys[K_RIGHT]:
        direct2="right"
        Moving=True
        RunR2=True
        RunL2=False
        move2=True
        stand2=False
        left2=False
        right2=True
        xp2+=10

    move1=False # if the key for mving is no longer pressed then move =False
    move2=False
    Moving=False    

def hitback(playernum,x,y,cha,char,direct,hit,ox): #ox is opponent x
    #the function hitback makes the player being hit move back 
    global lhit1,rhit1,lit2,rhit2, stand1, stand2
    if playernum==1 and hit==True:
        stand=False
        frame=0
        if char!="Na": #if character isn't Natsu then:
            if direct=="left" and x>ox and keys[K_KP_ENTER]!=1:
                stand1=False
                total=len(sprite[cha][10]) # total value of values in the 3d list
                if frame >= total: #ensures list doesn't go out of range
                    frame = 0            #sets the frame back to zero
                pictures=sprite[cha][10][frame] # a 3d list that goes character, move, frame
                screen.blit(pictures,(x,y)) #blit the pictures 
                frame+=1 #add 1 to the frame
                lhit1=True #the hit is True
                
            elif direct=="right"and x<ox  and keys[K_KP_ENTER]!=1: # same comments as above^
                stand1=False
                total=len(sprite[cha][11])
                if frame >= total:
                    frame = 0            
                pictures=sprite[cha][11][frame] # a 3d list that goes character, move, frame
                screen.blit(pictures,(x,y))
                frame+=1
                
                rhit1=True
                
                
        if char=="Na" : # same comments as above^
            if direct=="left" and x>ox  and keys[K_KP_ENTER]!=1:
                stand1=False
                total=len(sprite[cha][12])
                if frame >= total:
                    frame = 0            
                pictures=sprite[cha][12][frame] # a 3d list that goes character, move, frame
                screen.blit(pictures,(x,y))
                frame+=1
                lhit1=True
                
                
            elif direct=="right" and x<ox  and keys[K_KP_ENTER]!=1:
                stand1=False
                total=len(sprite[cha][13])
                if frame >= total:
                    frame = 0            
                pictures=sprite[cha][13][frame] # a 3d list that goes character, move, frame
                screen.blit(pictures,(x,y))
                frame+=1
                rhit1=True
        
        #Attacking1=False
                
    if playernum==2 and hit==True:# same comments as above^
        stand=False
        frame=0
        if char!="Na":
            if direct=="left" and x>ox  and keys[K_t]!=1:
                stand2=False
                total=len(sprite[cha][10])
                if frame >= total:
                    frame = 0            
                pictures=sprite[cha][10][frame] # a 3d list that goes character, move, frame
                screen.blit(pictures,(x,y))
                frame+=1
                lhit2=True
                
                
            elif direct=="right" and x<ox  and keys[K_t]!=1: # same comments as above^
                stand2=False
                total=len(sprite[cha][11])
                if frame >= total:
                    frame = 0            
                pictures=sprite[cha][11][frame] # a 3d list that goes character, move, frame
                screen.blit(pictures,(x,y))
                frame+=1
                rhit2=True
            
                
                
        if char=="Na":# same comments as above^
            if direct=="left" and x>ox  and keys[K_t]!=1:
                stand2=False
                total=len(sprite[cha][12])
                if frame >= total:
                    frame = 0            
                pictures=sprite[cha][12][frame] # a 3d list that goes character, move, frame
                screen.blit(pictures,(x,y))
                frame+=1
                lhit2=True
                
                
            elif direct=="right" and x<ox and keys[K_t]!=1:
                stand2=False
                total=len(sprite[cha][13])
                if frame >= total:
                    frame = 0            
                pictures=sprite[cha][13][frame] # a 3d list that goes character, move, frame
                screen.blit(pictures,(x,y))
                frame+=1
                rhit2=True

def block(name,charactersym,x,y,playernum,direct):
    global Block1R, Block2R,Block1L, Block2L,ONGROUND1, ONGROUND2,stand1,stand2
    sRightpic=image.load("Block\\"+charactersym+"BlockR.png" )#load stand pics
    sLeftpic=image.load("Block\\"+charactersym+"BlockL.png" )
    
    if playernum==1 and keys[K_t] and keys[K_w]!=1 and keys[K_SPACE]!=1 and keys[K_a]!=1 and keys[K_d]!=1 and keys[K_s]!=1 and keys[K_g]!=1 and keys[K_h]!=1 and keys[K_k]!=1 and ONGROUND1==True: #if player is 1st player
        stand1=False
        if direct=="right":
            screen.blit(sRightpic,(x,y))#blits the Right Stand Picture
            Block1R=True

        elif direct=="left":
            screen.blit(sLeftpic,(x,y))
            Block1L=True
    if playernum==2 and keys[K_KP_ENTER] and keys[K_UP]!=1 and keys[K_KP0]!=1 and keys[K_RIGHT]!=1 and keys[K_LEFT]!=1 and keys[K_DOWN]!=1 and keys[K_KP1]!=1 and keys[K_KP2]!=1 and keys[K_KP3]!=1 and ONGROUND2==True:
        stand2=False
        if direct=="right":
            screen.blit(sRightpic,(x,y))
            Block2R=True

        elif direct=="left":
            screen.blit(sLeftpic,(x,y))
            Block2L=True

    return Block1R, Block2R,Block1L, Block2L

#=============================================================================
#=========================End of Functions====================================
#=============================================================================

  
startmatch()    #calls the startmatch function which is the count down
running=True #running is True

#============================EVENT LOOP=======================================

while running:
    dist1=((xp1-xp2)**2+(yp1-yp2)**2)**0.5# the distance formula that represents the p1 range
    dist2=((xp2-xp1)**2+(yp2-yp1)**2)**0.5 # the distance formula that represents the p2 range

    for evt in event.get(): 
        if evt.type == QUIT:
            running =False

        if evt.type !=KEYDOWN: #if event type is not key down which means a key isn't pressed 
            if ONGROUND1==True : #then the player is on the ground
                stand1=True #if player is o nthe ground then he/she is standing
                rhit=False #and is not being hit
            if ONGROUND2==True :
                stand2=True
                rhit=False

    keys = key.get_pressed() #defines keys
    screen.blit(MAP,(0,0)) #blit the battle map
    mx,my=mouse.get_pos() # sets position of the mouse
    mb=mouse.get_pressed() #defines the mouse click
    
    if stand1==True: # if character is standing then
        hit1=False #he/she is not being hit
        Attacking1=False # and not attacking
        stand(char1SELECT,char1,xp1,yp1,1,direct1)#call the stand function
        Block1R,Block1L=False,False

    if stand2==True : #same comments as stand1==True(above)^
        hit2=False
        Attacking2=False
        stand(char2SELECT,char2,xp2,yp2,2,direct2)
        Block2R,Block2L=False,False
            
    if ONGROUND1==True:#if player1 is on the ground
        if keys[K_w]: #and the "w" key is pressed then jump move has initiated
            Jump1=True#therefore jump is True
            stand1=False #stand is False 
        if keys[K_s] or keys[K_SPACE]: #if player1 then player is not standing as those keys are taunt and crouch
            stand1=False
    if ONGROUND2==True: #same comments as above ^
        if keys[K_UP]:
            Jump2=True
            stand2=False
        if keys[K_DOWN] or keys[K_KP0]:#if player2 then player is not standing as those keys are taunt and crouch
            stand2=False          

    if Jump1==True: #if the jump is true
        yp1-=17 #make the position of the player's y-value decrease to make the jumping movement
        ONGROUND1=False #therefore the player isn't on the ground
        if ONGROUND1==False: # if sprite is off of the ground
            yp1+=vyp1    #add the velocity to the y-value 
            if yp1 == 400: # to ensure that the player doesn't fall offscreen 
                yp1 = 400 # sets y-vale of character to 400 
                vyp1= 0 #resets the velocity
                ONGROUND1=True #therefore character is on the ground
                Jump1=False # the jump has finished which means that jump will be false
            vyp1+=1 #keeping ading 1 to velocity-acts as gravity unti lthe player reaches the ground(400) again
            
        if ONGROUND1==False and Jump1==True : #if jump is true
            if Attacking1==False:#and attacking is False
                jumpPic(char1SELECT,char1,xp1,yp1,1,direct1)#call function to display the jump pic
            jumpMove()#allow the player to move or control the jump

    if Jump2==True: #same comments as Jump2
        yp2-=17
        ONGROUND2=False
        if ONGROUND2==False: # if sprite is of the ground
            yp2+=vyp2    
            if yp2 == 400:
                yp2 = 400
                vyp2= 0
                ONGROUND2=True
                Jump2=False
            vyp2+=1
            
        if ONGROUND2==False and Jump2==True: #if player 2 is not on ground then
            if Attacking2==False:
                jumpPic(char2SELECT,char2,xp2,yp2,2,direct2)#blit jump pic
            jumpMove() #allow user to comtrol jump

    if ONGROUND1==True: # if onground 
        if keys[K_a] or keys[K_d]:
            walk()#and the keys "a" or "d" are pressed then player can move-call walk function
            move1=True#move is true
            stand1=False#player is no longer standing
            MovementPic1(xp1,yp1,xp2,yp2,cha1,cha2) #call the movement pic for the animations

    if ONGROUND2==True: #same comments as above^
        if keys[K_LEFT] or keys[K_RIGHT]:
            walk()
            move2==True
            stand2=False
            MovementPic2(xp1,yp1,xp2,yp2,cha1,cha2)

    if ONGROUND1==True or ONGROUND2==True or ONGROUND1==True and ONGROUND2==True:
        if move1 and move2==False or move1==False or move2==False :
            crouch(xp1,yp1,xp2,yp2,right1,left1,right2,left2,char1,char2)#if all those conditions above^ are satisfied then call the function
            
    if keys[K_s] or keys[K_SPACE]: # if this key is pressed then player is crouching or taunting
        stand1=False
        move1=False
        Attacking1=False
    if keys[K_KP0]or keys[K_DOWN]: # if this key is pressed then player is taunting or crouching
        stand2=False
        move2=False
        Attacking2=False
    
    if keys[K_KP1] or keys[K_KP2] or keys[K_KP3]: #means attack move has been prssed
        Attacking2=True
        Stand=False
        stand2=False
        move2=True            
        RunL=False
        RunR=False
    #this part below defines which attack wil be initiated and displayed
        if keys[K_KP1]:
            Attacktwo=1
        elif keys[K_KP2] and keys[K_UP]!=1 and ONGROUND1==True:
            Attacktwo=2
        elif keys[K_KP3] and keys[K_UP]!=1 and ONGROUND1==True:
            Attacktwo=3
            
        Attack2(Attacktwo,direct2,cha2,dist2)#call the attack function for player2
       
    if keys[K_g] or keys[K_h] or keys[K_k]:#same comments as above
        Attacking1=True
        Stand=False
        stand1=False
        move1=True

        RunL=False
        RunR=False

        if keys[K_g]:
            Attackone=1           
        elif keys[K_h] and keys[K_w]!=1 and ONGROUND2==True:
            Attackone=2
        elif keys[K_k] and keys[K_w]!=1 and ONGROUND2==True:
            Attackone=3
        
        Attack1(Attackone,direct1,cha1,dist1)

    if xp1>1010 or xp1<-100:# if player is 10pixels off the screen then the player respawns and gains 500damage
        xp1=300
        damagep1+=500
    if xp2>1010 or xp2<-100:
        xp2=700
        damagep2+=500
    if yp1>800 or yp1<0:
        xp1=400
        damagep1+=500
    if yp2>800 or yp2<0:
        xp2=400
        damagep2+=500

    if damagep1>=3500: #if player reaches 3500 damager
        damagep1=0 #they respawn
        lives1-=1 #and lose 1 life
        xp1,yp1=300,400

    if damagep2>=3500: #same as above^
        damagep2=0
        lives2-=1
        xp2,yp2=700,400
 
#============================================================
#=================Double Sprites For Range Attacks===========       
    if FireballAtkR1==True: #if this attack is chosen
        total1=len(sprite[cha1][11]) #total is total values of list
        if frameF1==8:#sets limit
            frameF1=0 #and sets to 0
        addon1+=30 #add 30 to the x coordinate of the attack
        distance1=xp1+addon1 #the total distance of the range attack
        flameRect1=Rect(distance1,yp1,75,50) #the flame rect which is the damage area
        flamepic1=sprite[cha1][11][frameF1]# get the flame pics in list
        frameF1+=1# add 1 to frame to change the fire pic

        
        screen.blit(flamepic1,(distance1,yp1)) #blit the fire pic
        FireballAtkR1=False #the attack is false as it is done

        if flameRect1.collidepoint(xp2,yp2) : # if the oppoonent hits the rect then he/she accumulates 
            if Block2L!=True:
                damagep2+=18+damagep2//1000
            addon1=10
            hit1=True
        if distance1>=1000: #if the fire goes off the screen, then distance addon is reset
            addon1=10
            FireballAtkR1=False #attack will be false
        elif hit2==True and hit1==True:
            hit1=False# the hit will be false
           
            
    if FireballAtkL1==True : #same comments as above^
        total1=len(sprite[cha1][10])
        if frameF1==8:
            frameF1=0
        addon1-=30
        
        distance1=xp1+addon1
        flameRect1=Rect(distance1,yp1,75,50)
        flamepic1=sprite[cha1][10][frameF1]
        frameF1+=1

        
        screen.blit(flamepic1,(distance1,yp1))
        FireballAtkL1=False


        if flameRect1.collidepoint(xp2,yp2) :
            if Block2R!=True:
                damagep2+=18+damagep2//1000
            addon1=10
            hit2=True
        elif hit1==True and hit2==True:
            hit1=False
        if distance1<=0:
            addon1=10
            FireballAtkL1=False

            
    if FireballAtkR2==True :#same comments as above^
        total=len(sprite[cha2][11])
        if frameF==8:
            frameF=0
        addon+=30
        distance=xp2+addon
        flameRect=Rect(distance,yp2,75,50)
        flamepic=sprite[cha2][11][frameF]
        frameF+=1

        
        screen.blit(flamepic,(distance,yp2))
        FireballAtkR2=False

        if flameRect.collidepoint(xp1,yp1) :
            if Block1L!=True:
                damagep1+=18+damagep1//1000
            addon=10
            hit2=True
        if distance>=1000:
            addon=10
            FireballAtkR2=False
        elif hit1==True and hit2==True:
            hit2=False
           
            
    if FireballAtkL2==True:#same comments as above^
        place=yp2
        total=len(sprite[cha2][10])
        if frameF==8:
            frameF=0
        addon-=30
        
        distance=xp2+addon
        flameRect=Rect(distance,place,75,50)
        flamepic=sprite[cha2][10][frameF]
        frameF+=1

        
        screen.blit(flamepic,(distance,place))
        FireballAtkL2=False


        if flameRect.collidepoint(xp1,yp1):
            if Block1R!=True:
                damagep1+=18+damagep1//1000
            addon=10
            hit2=True
        elif hit1==True and hit2==True:
            hit2=False
        if distance<=0:
            addon=10
            FireballAtkL2=False
            
    if MetalAtkR2==True: #same comments as above^
        total=len(sprite[cha2][14])
        if frameF==7:
            frameF=0
        addon+=30
        distance=xp2+addon
        flameRect=Rect(distance,yp2,75,50)
        flamepic=sprite[cha2][14][frameF]
        frameF+=1

        
        screen.blit(flamepic,(distance,yp2))
        MetalAtkR2=False

        if flameRect.collidepoint(xp1,yp1) :
            if Block1L!=True:
                damagep1+=12+damagep1//1000
            addon=10
            hit2=True
        if distance>=1000:
            addon=10
            MetalAtkR2=False
        elif hit1==True and hit2==True:
            hit2=False
           
            
    if MetalAtkL2==True: #same comments as above^
        place=yp2
        total=len(sprite[cha2][13])
        if frameF==7:
            frameF=0
        addon-=30
        
        distance=xp2+addon
        flameRect=Rect(distance,place,75,50)
        flamepic=sprite[cha2][13][frameF]
        frameF+=1

        
        screen.blit(flamepic,(distance,place))
        MetalAtkL2=False


        if flameRect.collidepoint(xp1,yp1):
            if Block1R!=True:
                damagep1+=12+damagep1//1000
            addon=10
            hit2=True
        elif hit1==True and hit2==True:
            hit2=False
        if distance<=0:
            addon=10
            MetalAtkL2=False

    if MetalAtkR1==True: #same comments as above^
        total1=len(sprite[cha1][14])
        if frameF1==7:
            frameF1=0
        addon1+=30
        distance1=xp1+addon1
        flameRect1=Rect(distance1,yp1,75,50)
        flamepic1=sprite[cha1][14][frameF1]
        frameF1+=1

        
        screen.blit(flamepic1,(distance1,yp1))
        MetalAtkR1=False

        if flameRect1.collidepoint(xp2,yp2):
            if Block2L!=True:
                damagep2+=18+damagep2//1000
            addon1=10
            hit1=True
        if distance1>=1000:
            addon1=10
            MetalAtkR1=False
        elif hit2==True and hit1==True:
            hit1=False
           
            
    if MetalAtkL1==True: #same comments as above^
        total1=len(sprite[cha1][13])
        if frameF1==7:
            frameF1=0
        addon1-=30
        
        distance1=xp1+addon1
        flameRect1=Rect(distance1,yp1,75,50)
        flamepic1=sprite[cha1][13][frameF1]
        frameF1+=1

        
        screen.blit(flamepic1,(distance1,yp1))
        MetalAtkL1=False


        if flameRect1.collidepoint(xp2,yp2) :
            if Block2R!=True:
                damagep2+=18+damagep2//1000
            addon1=10
            hit2=True
        elif hit1==True and hit2==True:
            hit1=False
        if distance1<=0:
            addon1=10
            MetalAtkL1=False            

    if WaterAtkR1==True: #same comments as above^
        total1=len(sprite[cha1][16])
        if frameF1==3:
            frameF1=0
        addon1+=45
        distance1=xp1+addon1
        flameRect1=Rect(distance1,yp1,75,50)
        flamepic1=sprite[cha1][16][frameF1]
        frameF1+=1

        
        screen.blit(flamepic1,(distance1,yp1))
        WaterAtkR1=False

        if flameRect1.collidepoint(xp2,yp2):
            if Block2L!=True:
                damagep2+=18+damagep2//1000
            addon1=10
            hit1=True
        if distance1>=1000:
            addon1=10
            WaterAtkR1=False
        elif hit2==True and hit1==True:
            hit1=False
           
            
    if WaterAtkL1==True: #same comments as above^
        total1=len(sprite[cha1][15])
        if frameF1==3:
            frameF1=0
        addon1-=45
        
        distance1=xp1+addon1
        flameRect1=Rect(distance1,yp1,75,50)
        flamepic1=sprite[cha1][15][frameF1]
        frameF1+=1

        
        screen.blit(flamepic1,(distance1,yp1))
        WaterAtkL1=False


        if flameRect1.collidepoint(xp2,yp2):
            if Block2R!=True:
                damagep2+=18+damagep2//1000
            addon1=10
            hit2=True
        elif hit1==True and hit2==True:
            hit1=False
        if distance1<=0:
            addon1=10
            WaterAtkL1=False  

    if WaterAtkR2==True: #same comments as above^
        total=len(sprite[cha2][16])
        if frameF==3:
            frameF=0
        addon+=45
        distance=xp2+addon
        flameRect=Rect(distance,yp2,75,50)
        flamepic=sprite[cha2][16][frameF]
        frameF+=1

        
        screen.blit(flamepic,(distance,yp2))
        WaterAtkR2=False

        if flameRect.collidepoint(xp1,yp1):
            if Block1L!=True:
                damagep1+=18+damagep1//1000
            addon=10
            hit2=True
        if distance>=1000:
            addon=10
            WaterAtkR2=False
        elif hit1==True and hit2==True:
            hit2=False

    if WaterAtkL2==True: #same comments as above^
        place=yp2
        total=len(sprite[cha2][15])
        if frameF==3:
            frameF=0
        addon-=45
        
        distance=xp2+addon
        flameRect=Rect(distance,place,75,50)
        flamepic=sprite[cha2][15][frameF]
        frameF+=1

        
        screen.blit(flamepic,(distance,place))
        WaterAtkL2=False


        if flameRect.collidepoint(xp1,yp1) :
            if Block1R!=True:
                damagep1+=12+damagep1//1000
            addon=10
            hit2=True
        elif hit1==True and hit2==True:
            hit2=False
        if distance<=0:
            addon=10
            WaterAtkL2=False           

    if WaterRoarAtkR2==True : #same comments as above^
        total=len(sprite[cha2][14])
        if waterF==4:
            waterF=0
        addon+=30
        distance=xp2+addon
        waterRect=Rect(distance,yp2,75,50)
        waterpic=sprite[cha2][14][waterF]
        waterF+=1

        
        screen.blit(waterpic,(distance,yp2))
        WaterRoarAtkR2=False

        if waterRect.collidepoint(xp1,yp1):
            if Block1L!=True:
                damagep1+=18+damagep1//1000
            addon=10
            hit2=True
        if distance>=1000:
            addon=10
            WaterRoarAtkR2=False
        elif hit1==True and hit2==True:
            hit2=False

    if WaterRoarAtkL2==True: #same comments as above^
        place=yp2
        total=len(sprite[cha2][13])
        if waterF==4:
            waterF=0
        addon-=30
        
        distance=xp2+addon
        waterRect=Rect(distance,place,75,50)
        waterpic=sprite[cha2][13][waterF]
        waterF+=1

        
        screen.blit(waterpic,(distance,place))
        WaterRoarAtkL2=False


        if waterRect.collidepoint(xp1,yp1) :
            if Block1R!=True:
                damagep1+=12+damagep1//1000
            addon=10
            hit2=True
        elif hit1==True and hit2==True:
            hit2=False
        if distance<=0:
            addon=10
            WaterRoarAtkL2=False
            
    if WaterRoarAtkR1==True: #same comments as above^
        total=len(sprite[cha1][14])
        if waterF1==4:
            waterF1=0
        addon1+=30
        distance1=xp1+addon1
        waterRect1=Rect(distance1,yp1,75,50)
        waterpic1=sprite[cha1][14][waterF1]
        waterF1+=1

        
        screen.blit(waterpic1,(distance1,yp1))
        WaterRoarAtkR1=False

        if waterRect1.collidepoint(xp2,yp2):
            if Block2L!=True:
                damagep2+=18+damagep2//1000
            addon1=10
            hit1=True
        if distance1>=1000:
            addon1=10
            WaterRoarAtkR1=False
        elif hit1==True and hit2==True:
            hit1=False

    if WaterRoarAtkL1==True: #same comments as above^
        place=yp1
        total=len(sprite[cha1][13])
        if waterF1==4:
            waterF1=0
        addon1-=30
        
        distance1=xp1+addon1
        waterRect1=Rect(distance1,place,75,50)
        waterpic1=sprite[cha1][13][waterF1]
        waterF1+=1

        
        screen.blit(waterpic1,(distance1,place))
        WaterRoarAtkL1=False


        if waterRect1.collidepoint(xp2,yp2):
            if Block2R!=True:
                damagep2+=12+damagep2//1000
            addon1=10
            hit1=True
        elif hit1==True and hit2==True:
            hit1=False
        if distance1<=0:
            addon1=10
            WaterRoarAtkL1=False           

    if hit1==True and direct1=="right": 
        xp2+=2+damagep2//100000
        
    elif hit1==True and direct1=="left":
        xp2-=2+damagep2//100000
        
    if hit2==True and direct2=="right":
        xp1+=2+damagep1//100000
        
    elif hit2==True and direct2=="left":
        xp1-=2+damagep1//100000
        
    if BowAtkR1==True:     # if the bow attack is selected   
        addon1+=30 #add on distance +30
        distance1=xp1+addon1 #same comments as above^
        arrowRect1=Rect(distance1,yp1,30,30)
        arrowdamageRect=Rect(distance1,yp1+30,43,20)
        arrowframe1+=1            
        screen.blit(arrowR,arrowRect1)
        BowAtkR1=False

        if arrowRect1.collidepoint(xp2,yp2):
            if Block2L!=True:
                damagep2+=8+damagep2//1000
            addon1=12
            hit1=True
        if distance1>=1000:
            addon1=12
            BowAtkR1=False
        elif hit1==True and hit2==True:
            hit1=False
    if BowAtkL1==True: #same comments as above^
        
        addon1-=30
        distance1=xp1+addon1
        arrowRect1=Rect(distance1,yp1,30,30)
        arrowdamageRect=Rect(distance1,yp1+30,43,20)
        arrowframe1+=1
        screen.blit(arrowL,arrowRect1)
        BowAtkL1=False

        if arrowRect1.collidepoint(xp2,yp2):
            if Block2R!=True:
                damagep2+=8+damagep2//1000
            addon1=12
            hit1=True
        if distance1<=0:
            addon1=12
            BowAtkL1=False
        elif hit1==True and hit2==True:
            hit1=False

    if BowAtkR2==True: #same comments as above^
        
        addon+=30
        distance=xp2+addon
        arrowRect=Rect(distance,yp2,30,30)
        arrowdamageRect2=Rect(distance,yp2+30,43,20)
        arrowframe2+=1
        
        
        
        screen.blit(arrowR,arrowRect)
        BowAtkR2=False

        if arrowRect.collidepoint(xp1,yp1):
            if Block1L!=True:
                damagep1+=8+damagep1//1000
            addon=12
            hit2=True
        if distance>=1000:
            addon=12
            BowAtkR2=False
        elif hit1==True and hit2==True:
            hit2=False
    if BowAtkL2==True:#same comments as above^
        
        addon-=30
        distance=xp2+addon
        arrowRect=Rect(distance,yp2,30,30)
        arrowdamageRect=Rect(distance,yp2+30,43,20)
        arrowframe1+=1
        
        
        
        screen.blit(arrowL,arrowRect)
        BowAtkL2=False

        if arrowRect.collidepoint(xp1,yp1):
            if Block1R!=True:
                damagep1+=8+damagep1//1000
            addon=12
            hit2=True
        if distance<=0:
            addon=12
            BowAtkL2=False
        elif hit1==True and hit2==True:
            hit2=False   
    
    hitback(1,xp1,yp1,cha1,char1,direct1,hit2,xp2)#call function hitback 
    hitback(2,xp2,yp2,cha2,char2,direct2,hit1,xp1)
    block(char1SELECT,char1,xp1,yp1,1,direct1)
    block(char2SELECT,char2,xp2,yp2,2,direct2)
    hit1=False#hit is false
    hit2=False    
    Taunt(xp1,yp1,xp2,yp2,cha1,cha2)# call taunt function
    damagedisplay(char1SELECT,char2SELECT) #call damage display
    livesdisplay()#call lives display
    EndGame(lives1,lives2) #call endgame function
    myClock.tick(11)# set the in game running time
    display.flip()
quit()



