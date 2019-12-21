from pygame import*
from math import*
from random import*
from loadimage import* 
init()
screen=display.set_mode((1000,800))
myClock=time.Clock()

#==============================================================================
#Functions=====================================================================

#Main Menu=====================================================================
MeleeRect=Rect(91,87,187,66)
TrainRect=Rect(93,190,187,66)
SurRect=Rect(89,292,187,66)
ControlRect=Rect(89,389,187,66)

SurvivalPic=image.load("Menu pictures\\Main Menu\\Survival.png")
TrainingPic=image.load("Menu pictures\\Main Menu\\Training.png")
MeleePic=image.load("Menu pictures\\Main Menu\\Melee button.png")
ControlPic=image.load("Menu pictures\\Main Menu\\Control.png")

MainMenuPic=image.load("Menu pictures\\Main Menu\\Menu.jpg")

def Menu():
    global Cscreen,Tscreen
  
    if MeleeRect.collidepoint(mx,my):
        screen.blit(MeleePic,(91,87))
        if mb[0]==1:
            Cscreen="Character Melee"
                
    if TrainRect.collidepoint(mx,my):
        screen.blit(TrainingPic,(93,190))
        if mb[0]==1:
            Cscreen="Training"


    if SurRect.collidepoint(mx,my):
        screen.blit(SurvivalPic,(95,292))
        if mb[0]==1:
            Cscreen="Survival" 
 
    if ControlRect.collidepoint(mx,my):
        screen.blit(ControlPic,(89,389))
        if mb[0]==1:
            Cscreen="Control"
#Melee=========================================================================
    #Character Selection=======================================================
intructions1Rect=(12,674,200,100)
intructions2Rect=(780,674,200,100)

blue=((0,100,255))

font = font.SysFont("Times New Roman", 20)

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

CharacterbackRect=Rect(801,11,173,44)

CharacterSelPic=image.load("Selection pictures\\CharacterSelect.png")
CharacterBackSelPic=image.load("Selection pictures\\CharacterSelect back.png")
BackSelectRect=Rect(800,12,176,46)

def CharacterSel():
    global char1, char2, Cscreen
    if CharacterbackRect.collidepoint(mx,my):
        screen.blit(CharacterBackSelPic,(801,12))
        if mb[0]==1:
            char1=""
            char2=""
            Cscreen="Main Menu"

    if NatRect.collidepoint(mx,my):
        draw.rect(screen,blue,NatRect,2)
        if mb[0]==1:
            char1="Natsu"
        if mb[2]==1:
            char2="Natsu"
            
    elif GreyRect.collidepoint(mx,my):
        draw.rect(screen,blue,GreyRect,2)
        if mb[0]==1:
            char1="Grey"
        if mb[2]==1:
            char2="Grey"
            
    elif ErRect.collidepoint(mx,my):
        draw.rect(screen,blue,ErRect,2)
        if mb[0]==1:
            char1="Erza"
        if mb[2]==1:
            char2="Erza"
            
    elif GajRect.collidepoint(mx,my):
        draw.rect(screen,blue,GajRect,2)
        if mb[0]==1:
            char1="Gajeel"
        if mb[2]==1:
            char2="Gajeel"
            
    elif FreRect.collidepoint(mx,my):
        draw.rect(screen,blue,FreRect,2)
        if mb[0]==1:
            char1="Freed"
        if mb[2]==1:
            char2="Freed"

    elif LuRect.collidepoint(mx,my):
        draw.rect(screen,blue,LuRect,2)
        if mb[0]==1:
           char1="Lucy"
        if mb[2]==1:
            char2="Lucy"
       
    elif WenRect.collidepoint(mx,my):
        draw.rect(screen,blue,WenRect,2)
        if mb[0]==1:
            char1="Wendy"
        if mb[2]==1:
           char2="Wendy"

    if char1=="Natsu":
        screen.blit(napic,(260,21,300,500))
    if char2=="Natsu":
        screen.blit(napic,(550,21,300,500))
    if char1=="Grey":
        screen.blit(grepic,(220,160,300,500))
    if char2=="Grey":
         screen.blit(grepic,(540,160,300,500))
    if char1=="Erza":
        screen.blit(erpic,(300,160,300,500))        
    if char2=="Erza":
        screen.blit(erpic,(600,160,300,500))
    if char1=="Gajeel":
        screen.blit(gajpic,(300,160,300,500))       
    if char2=="Gajeel":
        screen.blit(gajpic,(600,160,300,500))           
    if char1=="Freed":
        screen.blit(frpic,(0,50,300,500))        
    if char2=="Freed":
        screen.blit(frpic,(280,50,300,500))           
    if char1=="Lucy":
        screen.blit(lupic,(355,160,300,500))    
    if char2=="Lucy":
        screen.blit(lupic,(650,160,300,500))
    if char1=="Wendy":
        screen.blit(wepic,(300,235,300,500)) 
    if char2=="Wendy":
        screen.blit(wepic,(600,235,300,500))
            
    txtp1=font.render((char1),True,(0,100,255))
    txtp2=font.render((char2),True,(0,100,255))
    txtintructions1=font.render("Left Click for Player 1",True,(0,100,255))
    txtintructions2=font.render("Right Click for Player 2",True,(0,100,255))
    screen.blit(txtintructions1,intructions1Rect)
    screen.blit(txtintructions2,intructions2Rect)
    screen.blit(txtp1,Player1Rect)
    screen.blit(txtp2,Player2Rect)

MapBackSelPic=image.load("selection pictures\Map selection back.png")
Map1Pic=image.load("selection pictures\Map selection map 1.png")
Map2Pic=image.load("selection pictures\Map selection map 2.png")
MapSelPic=image.load("selection pictures\Map selection copy.png")
Map1Rect=Rect(55,70,357,285)
Map2Rect=Rect(55,438,357,285)
MapbackRect=Rect(779,27,183,70)    

def MapSelection():
    global Cscreen

    if MapbackRect.collidepoint(mx,my):
        screen.blit(MapBackSelPic,(768,20))
        if mb[0]==1:
            GameMap=""
            Cscreen="Main Menu"
    if Map1Rect.collidepoint(mx,my):
        screen.blit(Map1Pic,(42,56))
        if mb[0]==1:
            GameMap="Map 1"
    if Map2Rect.collidepoint(mx,my):
        screen.blit(Map2Pic,(44,422))
        if mb[0]==1:
            GameMap="Map 2"
  
char1=""
char2=""
GameMap=""
#Captain Falcon================================================================
picStandRight=image.load("pictures\\Falcon\\standingcaptR.png")
picStandLeft=image.load("pictures\\Falcon\\standingcaptL.png")
picJumpRight=image.load("pictures\\Falcon\\jumpright.png") 
picJumpLeft=image.load("pictures\\Falcon\\jumpleft.png")
picCrouchRight=image.load("pictures\\Falcon\\captcrouchr.png")
picCrouchLeft=image.load("pictures\\Falcon\\captcrouchl.png")
TauntPic=image.load("pictures\\Falcon\\captainfalconshowurmoves.png")
#Training======================================================================
dist1=0
dist2=0
dist3=0
Tx=300
Ty=400
Tvy=1
direction="right"
TBackground=image.load("Maps\\final destination training.jpg")
TSBackgroundBack=image.load("Maps\\final destination back.jpg")
BackRect=Rect(713,25,240,100)

def TSGame():
    global dist1,dist2,dist3,Ty,Tvy,direction, TSRunR, TSRunL, TSmove, Cscreen, TSAttackType, TSONGROUND
    if BackRect.collidepoint(mx,my):
        screen.blit(TSBackgroundBack,(712,25))
        if mb[0]==1:
            Cscreen="Main Menu"
        
    if keys[K_a] or keys[K_d] and TSmove!="taunt":
        if keys[K_a] and TSRunR==False:
            direction="left"
            TSRunL=True

        if keys[K_d] and TSRunL==False:
            direction="right"
            TSRunR=True
    if keys[K_w]:
        TSmove="jump"

    if keys[K_s] and TSRunL==False and TSRunR==False and TSONGROUND==True:
        TSmove="crouch"

    if keys[K_SLASH]and TSRunL==False and TSRunR==False and TSONGROUND==True:
        TSmove="taunt"
        
    if (keys[K_j] or keys[K_k] or keys[K_l]) and TSONGROUND==True:
        if keys[K_j]:
            TSAttackType=1
        if keys[K_k]:
            TSAttackType=2
        if keys[K_l]:
            TSAttackType=3
        TAttack(TSAttackType, direction)
    if TSAttackType==0:
        TSmovement()
        TSPicture(direction, TSONGROUND, TSmove)                   

def TSmovement():
    global Tx,TSRunR,TSRunL,TSONGROUND
    if Tx>1000:
        Tx=0
    if Tx<0:
        Tx=1000
    if keys[K_a] and TSRunR==False and TSONGROUND==True:
        Tx-=30
    if keys[K_d]and TSRunL==False and TSONGROUND==True:
        Tx+=30
    if keys[K_a] and TSRunR==False and TSONGROUND==False:
        Tx-=10
    if keys[K_d]and TSRunL==False and TSONGROUND==False:
        Tx+=10
        
TSframeLeft=0
TSframeright=0
cool=0
def TSPicture(direction, TSONGROUND, TSmove):
    global TSframeLeft, TSframeright, TSRunR, TSRunL, TSAttackType, cool
    

    if TSRunR==False and TSRunL==False and TSONGROUND==True and TSmove=="" and TSAttackType==0:
        if direction=="left":
            screen.blit((sprite[7][11]),(Tx,Ty))
        if direction=="right":
           screen.blit((sprite[7][12]),(Tx,Ty))
        myClock.tick(15)

    if keys[K_a] and TSRunR==False and TSONGROUND==True:
        screen.blit((sprite[7][0])[TSframeLeft],(Tx+20,Ty))
        TSframeLeft+=1
        if TSframeLeft==5:
            TSframeLeft=0
        myClock.tick(15)

    if keys[K_d]and TSRunL==False and TSONGROUND==True:
        screen.blit((sprite[7][1])[TSframeright],(Tx,Ty))
        TSframeright+=1
        if TSframeright==5:
            TSframeright=0
        myClock.tick(15)

    if TSONGROUND==False:
        if direction=="left":
            screen.blit((sprite[7][2]),(Tx,Ty))
        if direction=="right":
            screen.blit((sprite[7][3]),(Tx,Ty))
        myClock.tick(90)

    if TSmove=="crouch":
        if direction=="left":
            screen.blit((sprite[7][13]),(Tx+15,Ty+20))
        if direction=="right":
            screen.blit((sprite[7][14]),(Tx,Ty+20))
    if TSmove=="taunt" :
        screen.blit((sprite[7][10]),(Tx,Ty-10))
        

#==================================================================================================
TAttackR1Frame=0
TAttackR2Frame=0
TAttackR3Frame=0

TAttackL1Frame=0
TAttackL2Frame=0
TAttackL3Frame=0

def TAttack(TSAttackType, direction):
    global Tx,Ty, TAttackR1Frame,TAttackR2Frame,TAttackR3Frame,TAttackL1Frame,TAttackL2Frame,TAttackL3Frame
    
    if direction=="right":
        if TSAttackType==1:
            screen.blit((sprite[7][5])[TAttackR1Frame],(Tx-20,Ty-10))
            TAttackR1Frame += 1
            if TAttackR1Frame == 7:
                TAttackR1Frame = 0
            myClock.tick(10)

        if TSAttackType==2:
            screen.blit((sprite[7][7])[TAttackR2Frame],(Tx-20,Ty-10))
            TAttackR2Frame += 1
            Tx+=20
            if TAttackR2Frame == 3:
                TAttackR2Frame = 0
            myClock.tick(5)
            
        if TSAttackType==3:
            boxRect=(Tx-30,Ty,((sprite[7][8])[TAttackR3Frame].get_width()),(sprite[7][8])[TAttackR3Frame].get_height())
            draw.rect(screen,(255,0,0),(boxRect),2)
            screen.blit((sprite[7][8])[TAttackR3Frame],(Tx-20,Ty+10))
            TAttackR3Frame += 1
            if TAttackR3Frame== 6:
                TAttackR3Frame = 0
            myClock.tick(5)
                
    if direction=="left":
        if TSAttackType==1:
            screen.blit((sprite[7][4])[TAttackL1Frame],((Tx-(sprite[7][4])[TAttackL1Frame].get_width())+50,Ty-10))
            TAttackL1Frame += 1
            if TAttackL1Frame == 7:
                TAttackL1Frame = 0
            myClock.tick(10)

        if TSAttackType==2:
            screen.blit((sprite[7][6])[TAttackL2Frame],((Tx-(sprite[7][6])[TAttackL2Frame].get_width())+50,Ty-10))
            TAttackL2Frame += 1
            Tx-=20
            if TAttackL2Frame == 3:
                TAttackL2Frame = 0
            myClock.tick(5)

        if TSAttackType==3:
            boxRect=(Tx-30,Ty,(sprite[7][9])[TAttackL3Frame].get_width(),(sprite[7][9])[TAttackL3Frame].get_height())
            draw.rect(screen,(255,0,0),(boxRect),2)
            screen.blit((sprite[7][9])[TAttackL3Frame],((Tx-(sprite[7][9])[TAttackL3Frame].get_width())+50,Ty+10))
            TAttackL3Frame+= 1
            
            if TAttackL3Frame == 6:
                TAttackL3Frame = 0
            myClock.tick(5)
Dx=700
Dy=400
DollDamageR=image.load("pictures\\doll\\trainingdollRight2.png")
DollDamageL=image.load("pictures\\doll\\trainingdollLeft2.png")
DollStandR=image.load("pictures\\doll\\trainingdollRight1.png")
DollStandL=image.load("pictures\\doll\\trainingdollLeft0.png")

Dist=0
Slope=0
def Tdoll():
    global TSAttackType, Dx, Dy, Dist, Slope
    
    if Dx>1000:
        Dx=0
    if Dx<0:
        Dx=1000
    Dist=((Tx-Dx)**2+(Ty-Dy)**2)**.5

    if (Tx-Dx)!=0:
        Slope=((Ty-Dy)/(Tx-Dx))
    if TSAttackType==0 or Dist>100:
        if direction=="right":
            screen.blit(DollStandR,(Dx,Dy))
        if direction=="left":
            screen.blit(DollStandL,(Dx,Dy))

    
#==============================================================================    
#Survival
dist1=0
dist2=0
dist3=0
Tx=500
Ty=400
Tvy=1
direction="right"
SBackground=image.load("Maps\\final destination survival.jpg")
#Control=======================================================================
ControlMenuPic=image.load("Menu pictures\\Control\\Controls.jpg")

BackControlRect=Rect(23,25,170,50)
BackControlpic=image.load("Menu pictures\\Control\\Select Back.jpg")

def Control():
    global Cscreen
    if BackControlRect.collidepoint(mx,my):
        screen.blit(BackControlpic,(23,24)) 
        if mb[0]==1:
            Cscreen="Main Menu"
    

Cscreen="Main Menu"
Tscreen=""
TSONGROUND=True
running=True


while running:
    TSRunR=False
    TSRunL=False
    TSmove=""
    TSAttackType=0
    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False
    keys = key.get_pressed()
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    if Cscreen=="Main Menu":
        screen.blit(MainMenuPic,(0,0))  
        Menu()

    if Cscreen=="Character Melee":
        screen.blit(CharacterSelPic,(0,0))
        CharacterSel()
        if char1!="" and char2!="" and keys[K_RETURN]:
            Cscreen="Map Melee"
    if Cscreen=="Map Melee":
        screen.blit(MapSelPic,(0,0))
        MapSelection()

    if Cscreen=="Training":
        screen.blit(TBackground,(0,0))
        TSGame()
        Tdoll()
        if keys[K_w] or TSONGROUND==False:
            Ty-=18
            TSONGROUND=False
            if TSONGROUND==False:
                Ty+=Tvy
                if Ty==400:
                    Ty=400
                    Tvy=0
                    TSONGROUND=True
                Tvy+=1
            myClock.tick(90)

    if Cscreen=="Survival":
        screen.blit(SBackground,(0,0))
        TSGame()
        if keys[K_w] or TSONGROUND==False:
            Ty-=18
            TSONGROUND=False
            if TSONGROUND==False:
                Ty+=Tvy
                if Ty==400:
                    Ty=400
                    Tvy=0
                    TSONGROUND=True
                Tvy+=1
            myClock.tick(90)
    if Cscreen=="Control":
        screen.blit(ControlMenuPic,(0,0))
        Control()
        
    display.flip()
    print(cool)
quit()
