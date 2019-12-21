#gametestfun.py
# THIS is just a demo alpha version of our project

# PATCH
    #start match function not working--

    ###### IMPORTANT--gravity needs TO BE FIXED Line--388-436 !!!!! 
   


#___________________________________________________________________________________
from pygame import*
from random import*
from math import*

screen=display.set_mode((1000,800))
init()
myClock=time.Clock()

display.init()   # <--Must have for caption
display.set_caption("Clash of The FairyTail")

init()   #must have for font
arialFontstart = font.SysFont("Times New Roman", 60)
arialFont2 = font.SysFont("Times New Roman", 70)
damagep1=0
damagep2=0
damagerect1=Rect(300,700,100,100)
damagerect2=Rect(600,700,100,100)
replayrect=Rect(400,500,200,100)
Quitrect=Rect(400,400,200,100)
txtPosStartRect=Rect(500,300,30,30)
colour=((0,0,0))
colour2=((0,0,0))
red=((255,0,0))
blue=((0,0,255))
damag1=False
damag2=False
hit=False
Quit=False


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
        
    

def offscreen(x,y,playernum):
    '''checks if player is offscreen'''
    global damagep1,damagep2
    if playernum==1:
        if x>=1000 or x<=0 or y<=0 or y>=1000:
            x=300
            y=400
            damagep1=1000
    elif playernum==2:
        if x>=1000 or x<=0 or y<=0 or y>=1000:
            x=700
            y=400
            damagep2=1000
            

##def hitside():
##    '''hits the player damaged and blows them away in opposite direction'''
##    global damag1, damag2, x1, y1,x2,y2, vy1,vy2
##    if damag1==True and damag2==False:
##        if x1 <x2 :
##            x2+=damagep2//4+9
##            y2-=damagep2//4+2
##            damag1=False
##            ONGROUND=False
##            y2-=vy2    
##            if y2 >= 400 and ONGROUND==False:
##                y2 = 400
##                vy2= 0
##                ONGROUND=True
##            vy2+=1            
##        elif x1>x2 :
##            x2-=damagep2//4+9
##            y2-=damagep2//4+2
##            damag1=False
##            ONGROUND=False
##            y2-=vy2   
##            if y2 >= 400 and ONGROUND==False:
##                y2 = 400
##                vy2= 0
##                ONGROUND=True
##            vy2+=1            
##            
##    elif damag2==True and damag1==False:
##        if x2 <x1 :
##            x1+=damagep1//4+9
##            y1-=damagep1//4+2
##            damag2=False
##            ONGROUND=False
##            y1-=vy1    
##            if y1 >= 400 and ONGROUND==False:
##                y1 = 400
##                vy1= 0
##                ONGROUND=True
##            vy1+=1
##        elif x2>x1:
##            x1-=damagep1//4+9
##            y1-=damagep1//4+2
##            damag2=False
##            ONGROUND=False
##            y1-=vy1    
##            if y1 >= 400 and ONGROUND==False:
##                y1 = 400
##                vy1= 0
##                ONGROUND=True
##            vy1+=1            
    
    
def damagedisplay():
    '''dislays damage percentage that both players have gained'''
    global txtPos,txtPos1, colour, colour2
    txtPos=arialFont2.render((str(damagep1)+"%"),True,(colour))
    txtPos2=arialFont2.render((str(damagep2)+"%"),True,(colour2))
    screen.blit(txtPos2,damagerect2)
    screen.blit(txtPos,damagerect1)
    


def punch(character,spritefile,playernumber):
    '''punch animation'''
    screen.blit(character+spritefile,+".png",(x+playernumber,y+playernumber))

def crouch(x,y,direct,charactersymbol):
    '''crouch animation'''
    
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
    '''load moves'''
    filepics=[]
    for p in range(frange):
        filepics.append(image.load((foldername)+str(p)+".png"))
    return filepics

def walk(direction):
    '''player1 move function'''
    global x1,y1,frame
    keys=key.get_pressed()
    if keys[K_d]:
        direction = "right"
        x1+=10 

    if keys[K_a]:
        direction = "left"
        x1-=10

def walk2(direction2):
    '''player2 move function'''
    global x2,y2,frame
    keys=key.get_pressed()
    if keys[K_RIGHT]:
        direction2 = "right"
        x2+=10


    if keys[K_LEFT]:
        direction2 = "left"
        x2-=10


startmatch()

init()
mixer.music.load("SSBM Themes Hyrule Temple-[www_flvto_com].mp3")
mixer.music.play()

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
damage3=0

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
againgame=False

while running:
    dis1=((x1-x2)**2+(y1-y2)**2)**.5
    dis2=((x1-x2)**2+(y1-y2)**2)**.5
    dis3=((x1-x2)**2+(y1-y2)**2)**.5
    
    ONGROUND=True
    for evnt in event.get():                
        if evnt.type == QUIT:
            import mainmenu
            running = False
##        if evnt.type==KEYDOWN:
##            gravity()
    keys = key.get_pressed()
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    

    
    screen.fill((255,255,255))
    damagedisplay()
    colour=((0,0,0))
    colour2=((0,0,0))

    
    if player=="Captian Falcon":
        if  keys[K_d] or keys[K_a]:
            walk(direction)
        if keys[K_w] :
            ONGROUND=False
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

    if keys[K_p] and dis1<=80:
        damage1=1
        myClock.tick(15)
        
    if keys[K_KP1] and dis2<=80:
        damage2=1
        myClock.tick(15)
    
    if keys[K_KP9] and dis3<=80:
        damage3=1
        txtPospJ=arialFont2.render(("JB ADMIN PUNCH"),True,(red))
        screen.blit(txtPospJ,(0,200,100,100))
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
        damag1=True
        circle2=draw.circle(screen,(200,0,0),(x2,int(y2)),10)
        damage1=0
        damagep2+=2+damagep2//10
        colour2=((255,0,0))
        damagedisplay()
        hit=True
      
    if damage2==1:
        damag2=True
        circle=draw.circle(screen,(200,0,0),(x1,int(y1)),10)
        damage2=0
        damagep1+=2+damagep1//10
        colour=((255,0,0))
        damagedisplay()
        hit=True

    if damage3==1:

        damag2=True
        circle=draw.circle(screen,(200,0,0),(x1,int(y1)),10)
        damage3=0
        damagep1+=90+damagep1//10
        colour=((0,0,255))
        damagedisplay()
        hit=True
        
    
        
    if damagep1>=1000:
        screen.fill((0,0,0))
        txtPosp2=arialFont2.render(("You lose Player 1! GAME OVER!"),True,(red))
        screen.blit(txtPosp2,(0,200,100,100))
        txtPosReplay=arialFont2.render(("Replay"),True,(blue))
        screen.blit(txtPosReplay,(replayrect))
        txtPosQuit=arialFont2.render((" Quit"),True,(blue))
        screen.blit(txtPosQuit,(Quitrect))
        if Quitrect.collidepoint(mx,my):
            draw.rect(screen,(red),(Quitrect),3)
            if mb[0]==1:
                import mainmenu
        elif replayrect.collidepoint(mx,my):
            draw.rect(screen,(red),(replayrect),3)
            if mb[0]==1:
                damagep1=0
                damagep2=0
                screen.fill((255,255,255))
                againgame=True
                
    elif damagep2>=1000:
        screen.fill((0,0,0))
        txtPosp2=arialFont2.render(("You lose Player 2! GAME OVER!"),True,(red))
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
                damagep1=0
                damagep2=0
                screen.fill((255,255,255))
                againgame=True
                
    if againgame==True:
        x1=300
        y1=400
        x2=700
        y2=400
        againgame=False
        startmatch()
                
    offscreen(x1,y1,1)
    offscreen(x2,y2,2)
    if hit==True:
        if damag1==True and damag2==False:
            if x1 <x2 :
                x2+=damagep2//4+9
                y2-=damagep2//4+2
                damag1=False
                ONGROUND=False
                y2-=vy2    
                if y2 >= 400 and ONGROUND==False:
                    y2 = 400
                    vy2= 0
                    ONGROUND=True
                vy2+=1            
            elif x1>x2 :
                x2-=damagep2//4+9
                y2-=damagep2//4+2
                damag1=False
                ONGROUND=False
                y2-=vy2   
                if y2 >= 400 and ONGROUND==False:
                    y2 = 400
                    vy2= 0
                    ONGROUND=True
                vy2+=1            
        
        elif damag2==True and damag1==False:
            if x2 <x1 :
                x1+=damagep1//4+9
                y1-=damagep1//4+2
                damag2=False
                ONGROUND=False
                y1-=vy1    
                if y1 >= 400 and ONGROUND==False:
                    y1 = 400
                    vy1= 0
                    ONGROUND=True
                vy1+=1
            elif x2>x1:
                x1-=damagep1//4+9
                y1-=damagep1//4+2
                damag2=False
                ONGROUND=False
                y1-=vy1    
                if y1 >= 400 and ONGROUND==False:
                    y1 = 400
                    vy1= 0
                    ONGROUND=True
                vy1+=1  
        hit=False
        
    if Quit==True:
        import mainmenu

    
    print(damagep1,damagep2,y1)
    display.flip()
    myClock.tick(60)
    

quit()
