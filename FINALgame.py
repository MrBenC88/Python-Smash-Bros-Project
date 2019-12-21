from pygame import*
from math import*
from random import*
from loadimage import*
##from spritelist import*
init()
screen=display.set_mode((1000,800))
myClock=time.Clock()
NatsuList=[6,4,11,22,4]
Greylist=[6,4,12,3,26]
ErzaList=[7,6,10,5,6]
WendyList=[6,5,13,9,7]
Gajeellist=[6,5,17,9,8]
FreedList=[6,5,24,20,17]
LucyList=[6,0,16,5,5]

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
            import NEWpvp
                
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

font1 = font.SysFont("Times New Roman", 20)
font2 = font.SysFont("Times New Roman", 100)
arialFontscore = font.SysFont("Times New Roman", 45)

NatRect=Rect(49,121,140,121)
GreyRect=Rect(49,294,140,121)
ErRect=Rect(49,459,140,121)
GajRect=Rect(824,121,140,121)
FreRect=Rect(824,294,140,121)
LuRect=Rect(824,459,140,121)
WenRect=Rect(431,605,140,121)

##Player 1 Select and Player 2 Select
Player1Rect=Rect(310,676,145,33)
Player2Rect=Rect(650,676,145,33)

CharacterbackRect=Rect(801,11,173,44)

CharacterSelPic=image.load("Selection pictures\\CharacterSelect.png")
CharacterBackSelPic=image.load("Selection pictures\\CharacterSelect back.png")
BackSelectRect=Rect(800,12,176,46)



MapBackSelPic=image.load("selection pictures\Map selection back.png")
Map1Pic=image.load("selection pictures\Map selection map 1.png")
Map2Pic=image.load("selection pictures\Map selection map 2.png")
MapSelPic=image.load("selection pictures\Map selection copy.png")
Map1Rect=Rect(55,70,357,285)
Map2Rect=Rect(55,438,357,285)
MapbackRect=Rect(779,27,183,70)    

def MapSelection():
    global Cscreen, GameMap

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
EndGamePic=image.load("End Game\\EndGame.png")
EndGameReplayPic=image.load("End Game\\EndGame Play game.png")
EndReplayRect=Rect(290,530,435,110)
EndBackRect=Rect(390,665,240,100)

GameMap2Pic=image.load("Maps\\final destination map 2.png")
GameMap1Pic=image.load("Maps\\final destination map 1.png")

Ch1x=300
Ch1y=400
Ch2x=700
Ch2y=400
Ch1direction="right"
Ch2firection="left"

def MeleeMovement():
    global Ch1x,Ch1y,Ch2x,Ch2y,Ch1direction, Ch2direction,Ch1RunR,Ch1RunL, Ch1ONGROUND,Ch1AttackType, Cscreen, GameMap
    if GameMap=="Map 2":
        screen.blit(GameMap2Pic,(0,0))
    if GameMap=="Map 1":
        screen.blit(GameMap1Pic,(0,0))
    
    if BackRect.collidepoint(mx,my):
        screen.blit(TSBackgroundBack,(712,25))
        if mb[0]==1:
            Ch1x=300
            Ch1y=400
            Ch2x=700
            Ch2y=400
            GameMap=""
            Cscreen="Main Menu"
        
    if keys[K_a] or keys[K_d] and TSmove!="taunt":
        if keys[K_a] and Ch1RunR==False:
            Ch1direction="left"
            Ch1RunL=True

        if keys[K_d] and Ch1RunL==False:
            Ch1direction="right"
            Ch1RunR=True
    if keys[K_w]:
        Ch1move="jump"

    if keys[K_s] and Ch1RunL==False and Ch1RunL==False and Ch1ONGROUND==True:
        Ch1move="crouch"

    if keys[K_SPACE]and Ch1RunL==False and Ch1RunL==False and Ch1ONGROUND==True:
        Ch1move="taunt"
        
    if (keys[K_g] or keys[K_h] or keys[K_j]) and Ch1ONGROUND==True:
        if keys[K_g]:
            Ch1AttackType=1
        if keys[K_h]:
            Ch1AttackType=2
        if keys[K_j]:
            Ch1AttackType=3

        Attack(Ch1AttackType, Ch1direction)
    if Ch1AttackType==0:
        Ch1movement()
        Ch1Picture(Ch1direction, Ch1ONGROUND, Ch1move)     


    if keys[K_LEFT] or keys[K_RIGHT] and TSmove!="taunt":
        if keys[K_LEFT] and Ch2RunR==False:
            Ch2direction="left"
            Ch2RunL=True

        if keys[K_RIGHT] and Ch2RunL==False:
            Ch2direction="right"
            Ch2RunR=True
    if keys[K_UP]:
        Ch2move="jump"

    if keys[K_DOWN] and Ch2RunL==False and Ch2RunL==False and Ch2ONGROUND==True:
        Ch2move="crouch"

    if keys[K_KP_ENTER]and Ch2RunL==False and Ch2RunL==False and Ch2ONGROUND==True:
        Ch2move="taunt"
        
    if (keys[K_KP1] or keys[K_KP2] or keys[K_KP3]) and Ch2ONGROUND==True:
        if keys[K_KP1]:
            Ch2AttackType=1
        if keys[K_KP2]:
            Ch2AttackType=2
        if keys[K_KP3]:
            Ch2AttackType=3
def EndGame():
    global char1, char2, Cscreen, GameMap

    GameMap=""
    screen.blit(EndGamePic,(0,0))
    txtWinner=font2.render((char1),True,(0,0,0))
    screen.blit(txtWinner,(400,375,500,500))
    
    if EndBackRect.collidepoint(mx,my):
        screen.blit(TSBackgroundBack,(396,664))
        if mb[0]==1:
            char1=""
            char2=""
            Cscreen="Main Menu"

    if EndReplayRect.collidepoint(mx,my):
        screen.blit(EndGameReplayPic,(293,532))
        
    
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
TSdirection="right"
TBackground=image.load("Maps\\final destination training.jpg")
TSBackgroundBack=image.load("Maps\\final destination back.jpg")
BackRect=Rect(713,25,240,100)

def TSGame():
    global dist1,dist2,dist3,Tx,Ty,Tvy,TSdirection,LifeCounter, TSRunR, TSRunL, TSmove, Cscreen, TSAttackType, TSONGROUND
    if BackRect.collidepoint(mx,my):
        screen.blit(TSBackgroundBack,(712,25))
        if mb[0]==1:
            Tx=500
            Ty=400
            LifeCounter=250
            Cscreen="Main Menu"
        
    if keys[K_a] or keys[K_d] and TSmove!="taunt":
        if keys[K_a] and TSRunR==False:
            TSdirection="left"
            TSRunL=True

        if keys[K_d] and TSRunL==False:
            TSdirection="right"
            TSRunR=True
    if keys[K_w]:
        TSmove="jump"

    if keys[K_s] and TSRunL==False and TSRunR==False and TSONGROUND==True:
        TSmove="crouch"

    if keys[K_SPACE]and TSRunL==False and TSRunR==False and TSONGROUND==True:
        TSmove="taunt"
        
    if (keys[K_g] or keys[K_h] or keys[K_j]) and TSONGROUND==True:
        if keys[K_g]:
            TSAttackType=1
        if keys[K_h]:
            TSAttackType=2
        if keys[K_j]:
            TSAttackType=3
        TAttack(TSAttackType, TSdirection)
    if TSAttackType==0:
        TSmovement()
        TSPicture(TSdirection, TSONGROUND, TSmove)                   

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

def TSPicture(TSdirection, TSONGROUND, TSmove):
    global TSframeLeft, TSframeright, TSRunR, TSRunL, TSAttackType, SBoxRect
    

    if TSRunR==False and TSRunL==False and TSONGROUND==True and TSmove=="" and TSAttackType==0:
        if TSdirection=="left":
            SBoxRect=Rect(Tx,Ty,(sprite[7][11]).get_width(),(sprite[7][11]).get_height())
            screen.blit((sprite[7][11]),(Tx,Ty))
        if TSdirection=="right":
            SBoxRect=Rect(Tx,Ty,(sprite[7][12]).get_width(),(sprite[7][12].get_height()))
            screen.blit((sprite[7][12]),(Tx,Ty))


    if keys[K_a] and TSRunR==False and TSONGROUND==True:
        SBoxRect=(Tx+20,Ty,(((sprite[7][0])[TSframeLeft].get_width())+10),(sprite[7][0])[TSframeLeft].get_height())
        screen.blit((sprite[7][0])[TSframeLeft],(Tx+20,Ty))
        TSframeLeft+=1
        if TSframeLeft==5:
            TSframeLeft=0
   

    if keys[K_d]and TSRunL==False and TSONGROUND==True:
        SBoxRect=(Tx,Ty,(((sprite[7][1])[TSframeright].get_width())+10),(sprite[7][1])[TSframeright].get_height())
        screen.blit((sprite[7][1])[TSframeright],(Tx,Ty))
        TSframeright+=1
        if TSframeright==5:
            TSframeright=0


    if TSONGROUND==False:
        if TSdirection=="left":
            SBoxRect=Rect(Tx,Ty,(sprite[7][2]).get_width(),(sprite[7][2].get_height()))
            screen.blit((sprite[7][2]),(Tx,Ty))
        if TSdirection=="right":
            SBoxRect=Rect(Tx,Ty,(sprite[7][3]).get_width(),(sprite[7][3].get_height()))
            screen.blit((sprite[7][3]),(Tx,Ty))
        myClock.tick(90)

    if TSmove=="crouch":
        if TSdirection=="left":
            SBoxRect=Rect(Tx+15,Ty+20,(sprite[7][13]).get_width(),(sprite[7][13].get_height()))
       
            screen.blit((sprite[7][13]),(Tx+15,Ty+20))
        if TSdirection=="right":
            SBoxRect=Rect(Tx,Ty+20,(sprite[7][14]).get_width(),(sprite[7][14].get_height()))
   
            screen.blit((sprite[7][14]),(Tx,Ty+20))

    if TSmove=="taunt" :
        SBoxRect=Rect(Tx,Ty-15,(sprite[7][10]).get_width(),(sprite[7][10].get_height()))
        screen.blit((sprite[7][10]),(Tx,Ty-15))

    if TSONGROUND==False:
        myClock.tick(90)
    else:
        myClock.tick(15) 

#==================================================================================================
TAttackR1Frame=0
TAttackR2Frame=0
TAttackR3Frame=0

TAttackL1Frame=0
TAttackL2Frame=0
TAttackL3Frame=0

def TAttack(TSAttackType, TSdirection):
    global Tx,Ty, TAttackR1Frame,TAttackR2Frame,TAttackR3Frame,TAttackL1Frame,TAttackL2Frame,TAttackL3Frame, SAttackboxRect
    
    if TSdirection=="right":
        if TSAttackType==1:
            SAttackboxRect=(Tx-30,Ty,(((sprite[7][5])[TAttackR1Frame].get_width())+10),(sprite[7][5])[TAttackR1Frame].get_height())
            screen.blit((sprite[7][5])[TAttackR1Frame],(Tx-20,Ty-10))
            TAttackR1Frame += 1
            if TAttackR1Frame == 7:
                TAttackR1Frame = 0
            myClock.tick(10)

        if TSAttackType==2:
            SAttackboxRect=(Tx-30,Ty,(((sprite[7][7])[TAttackR2Frame].get_width())+10),(sprite[7][7])[TAttackR2Frame].get_height())
            screen.blit((sprite[7][7])[TAttackR2Frame],(Tx-20,Ty-10))
            TAttackR2Frame += 1
            Tx+=20
            if TAttackR2Frame == 3:
                TAttackR2Frame = 0
            myClock.tick(5)
            
        if TSAttackType==3:
            SAttackboxRect=(Tx-30,Ty,(((sprite[7][8])[TAttackR3Frame].get_width())+10),(sprite[7][8])[TAttackR3Frame].get_height())
            screen.blit((sprite[7][8])[TAttackR3Frame],(Tx-20,Ty+10))
            TAttackR3Frame += 1
            if TAttackR3Frame== 6:
                TAttackR3Frame = 0
            myClock.tick(5)
                
    if TSdirection=="left":
        if TSAttackType==1:
            SAttackboxRect=(Tx-30,Ty,(sprite[7][4])[TAttackL1Frame].get_width(),(sprite[7][4])[TAttackL1Frame].get_height())
            screen.blit((sprite[7][4])[TAttackL1Frame],((Tx-(sprite[7][4])[TAttackL1Frame].get_width())+50,Ty-10))
            TAttackL1Frame += 1
            if TAttackL1Frame == 7:
                TAttackL1Frame = 0
            myClock.tick(10)

        if TSAttackType==2:
            SAttackboxRect=(Tx-30,Ty,(sprite[7][6])[TAttackL2Frame].get_width(),(sprite[7][6])[TAttackL2Frame].get_height())
            screen.blit((sprite[7][6])[TAttackL2Frame],((Tx-(sprite[7][6])[TAttackL2Frame].get_width())+50,Ty-10))
            TAttackL2Frame += 1
            Tx-=20
            if TAttackL2Frame == 3:
                TAttackL2Frame = 0
            myClock.tick(5)

        if TSAttackType==3:
            SAttackboxRect=(Tx-30,Ty,(sprite[7][9])[TAttackL3Frame].get_width(),(sprite[7][9])[TAttackL3Frame].get_height())
            screen.blit((sprite[7][9])[TAttackL3Frame],((Tx-(sprite[7][9])[TAttackL3Frame].get_width())+50,Ty+10))
            TAttackL3Frame+= 1
            
            if TAttackL3Frame == 6:
                TAttackL3Frame = 0
            myClock.tick(5)
Dx=700
Dy=400
DollDamageR=image.load("doll\\trainingdollRight2.png")
DollDamageL=image.load("doll\\trainingdollLeft2.png")
DollStandR=image.load("doll\\trainingdollRight1.png")
DollStandL=image.load("doll\\trainingdollLeft0.png")

Dist=0
Slope=0
def Jump():
    global TSONGROUND,Ty,Tvy
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
        myClock.tick(50)   
#==============================================================================
def Tdoll():
    global TSAttackType, Dx, Dy, Dist, Slope, SAttackboxRect,TrainHit

    if Dx>1000:
        Dx=500
    if Dx<0:
        Dx=500
    DollRect=Rect(Dx,Dy,(DollStandR).get_width(),(DollStandR.get_height()))

    if DollRect.colliderect(SAttackboxRect):
        TrainHit=True
        if TSdirection=="right":
            Dx+=10
            screen.blit(DollDamageR,(Dx,Dy))
        if TSdirection=="left":
            Dx-=10
            screen.blit(DollDamageL,(Dx,Dy))        

    if TrainHit==False:
        if TSdirection=="right":
            screen.blit(DollStandR,(Dx,Dy))
        if TSdirection=="left":
            screen.blit(DollStandL,(Dx,Dy))

#==============================================================================
FireballPic=image.load("200px-Fireball.png")
ABx=200
ABy=200
BBx=400
BBy=200
CBx=600
CBy=200
DBx=800
DBy=200
Avx=15
Avy=14
Bvx=14
Bvy=15
Cvx=15
Cvy=14
Dvx=14
Dvy=15
SCount=0
STotal=500
Fire1Rect=Rect(0,0,0,0)
Fire2Rect=Rect(0,0,0,0)
Fire3Rect=Rect(0,0,0,0)
Fire4Rect=Rect(0,0,0,0)
slope1=0
slope2=0
slope3=0
slope4=0

LifeCounter=250

def MainEnemies():
    global ABx,ABy,BBx,BBy,CBx,CBy,DBx,DBy,Avx,Cscreen,Avy,Bvx,Bvy,Cvx,Cvy,Dvx,Dvy,STime,STotal,SCount,LifeCounter,FireballPic,Tx,Ty,Fire1Rect,Fire2Rect,Fire3Rect,Fire4Rect,slope1,slope2,slope3,slope4,SBoxRect
    if (ABx-Tx)!=0:
        slope1=((ABy-Ty)/(ABx-Tx))

    if (BBx-Tx)!=0:
        slope2=((BBy-Ty)/(BBx-Tx))
    if (CBx-Tx)!=0:
        slope3=((CBy-Ty)/(CBx-Tx))
    if (DBx-Tx)!=0:
        slope4=((DBy-Ty)/(DBx-Tx))
    ABx+=Avx
    ABy+=Avy
    BBx-=Bvx
    BBy-=Bvy
    CBx+=Cvx
    CBy+=Cvy
    DBx-=Dvx
    DBy-=Dvy

    screen.blit(FireballPic,(ABx-12,ABy-12))
    Fire1Rect=Rect(ABx,ABy,25,25)
    screen.blit(FireballPic,(BBx-12,BBy-12))
    Fire2Rect=Rect(BBx,BBy,25,25)
    screen.blit(FireballPic,(CBx-12,CBy-12))
    Fire3Rect=Rect(CBx,CBy,25,25)
    screen.blit(FireballPic,(DBx-12,DBy-12))
    Fire4Rect=Rect(DBx,DBy,25,25)
    
    if ABx<0 or ABx>1000:
        Avx*=-1
    if ABy<170 or ABy>450:
        Avy*=-1
    if BBx<0 or BBx>1000:
        Bvx*=-1
    if BBy<170 or BBy>450:
        Bvy*=-1
    if CBx<0 or CBx>1000:
        Cvx*=-1
    if CBy<170 or CBy>450:
        Cvy*=-1
    if DBx<0 or DBx>1000:
        Dvx*=-1
    if DBy<170 or DBy>450:
        Dvy*=-1

    if Fire1Rect.colliderect(SBoxRect):
        LifeCounter-=10
        if slope1>0 or slope1==0:
            Tx+=10
        else:
            Tx-=10

    if Fire2Rect.colliderect(SBoxRect):
        LifeCounter-=10
        if slope2>0 or slope2==0:
            Tx+=10
        else:
            Tx-=10
    if Fire3Rect.colliderect(SBoxRect):
        LifeCounter-=10
        if slope3>0 or slope3==0:
            Tx+=10
        else:
            Tx-=10
        
    if Fire4Rect.colliderect(SBoxRect):
        LifeCounter-=10
        if slope4>0 or slope4==0:
            Tx+=10
        else:
            Tx-=10
    LifeCounterText=arialFontscore.render((str(LifeCounter))+"%",True,(100,200,255))
    screen.blit( LifeCounterText,(200,675,500,500))
    if LifeCounter==0:
        LifeCounter=250
        Cscreen="Main Menu"

Cx=randint(100,900)
Cy=randint(310,400)
CoinPic=image.load("Blue_Falcon.png")
pointCount=0
def Coin():
    global Cx, Cy, pointCount
    CoinRect=Rect(Cx,Cy,30,30)
    screen.blit(CoinPic,(Cx,Cy))
    if CoinRect.colliderect(SBoxRect):
        pointCount+=10
        Cx=randint(100,900)
        Cy=randint(320,400)
    PointCounterText=arialFontscore.render((str(pointCount)),True,(100,200,255))
    screen.blit( PointCounterText,(800,675,500,500))        
            
#==============================================================================    
#Survival
dist1=0
dist2=0
dist3=0
Tx=500
Ty=400
Tvy=1
TSdirection="right"
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

    SBoxRect=Rect(0,0,0,0)
    SAttackboxRect=Rect(0,0,0,0)
    TrainHit=False
    TSRunR=False
    TSRunL=False
    TSmove=""
    TSAttackType=0

    Ch1RunR=False
    Ch1RunL=False
    Ch1move=""
    Ch1AttackType=0

    Ch2RunR=False
    Ch2RunL=False
    Ch2move=""
    Ch2AttackType=0
    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False
    keys = key.get_pressed()
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    if Cscreen=="Main Menu":
        screen.blit(MainMenuPic,(0,0))  
        Menu()



    if Cscreen=="Map Melee":
        screen.blit(MapSelPic,(0,0))
        MapSelection()
        if GameMap!="":
            Cscreen="Melee"
    if Cscreen=="Melee":
        MeleeMovement()

    if Cscreen=="End Melee":
        EndGame()
    if Cscreen=="Character Melee":
        import NEWpvp        
#================================================================================
    if Cscreen=="Training":
        screen.blit(TBackground,(0,0))
        TSGame()
        Tdoll()
        Jump()


    if Cscreen=="Survival":

        screen.blit(SBackground,(0,0))
        TSGame()
        MainEnemies()
        Jump()
        Coin()

    if Cscreen=="Control":
        screen.blit(ControlMenuPic,(0,0))
        Control()
        
    display.flip()

quit()
