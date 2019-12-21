#adventure.py
from pygame import*
from random import*

alive=True
againgame=False
damage=0
size=10
atkrange=50
atk=3
vy1=2
x=100
y=200
vx=5
vy=2 

damaEN=False
dama=False
score=0
xc=500
yc=400
scoreRect=Rect(850,10,100,100)
init()
myClock=time.Clock()
init()   #must have for font
arialFontstart = font.SysFont("Times New Roman", 60)
arialFontscore = font.SysFont("Times New Roman", 35)
arialFont2 = font.SysFont("Times New Roman", 70)
healthp1=5000
keys = key.get_pressed()

healthrect=Rect(300,700,100,100)
enhealthrect=Rect(700,700,100,100)
replayrect=Rect(400,500,200,100)
Quitrect=Rect(400,400,200,100)
txtPosStartRect=Rect(500,300,30,30)
colour=((0,0,0))
colour2=((0,0,0))
red=((255,0,0))
blue=((0,0,255))
Quit=False
ONGROUND=True
player="P1"
move=""
enemyhealth=10000


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
        
def healthdisplay():
    '''dislays health percentage that player have gained'''
    global txtPos2, colour2
    txtPos2=arialFont2.render((str(healthp1)+"%"),True,(colour))
    screen.blit(txtPos2,healthrect)
    txtPosEN=arialFont2.render((str(enemyhealth)+"%"),True,(colour))
    screen.blit(txtPosEN,enhealthrect)
    
def scoredisplay():
    txtPosScore=arialFontscore.render((str(score)),True,(blue))
    screen.blit(txtPosScore,scoreRect)
    
def offscreen(x,y):
    '''checks if player is offscreen'''
    global healthp1,xc,yc

    if xc>=1000 or xc<=0 or yc<=0 or yc>=1000:
        xc=500
        yc=400
        healthp1-=1000

def walk():
    '''player1 move function'''
    global xc,yc,frame
    keys=key.get_pressed()
    if keys[K_RIGHT]:
        direction = "right"
        xc+=10 

    if keys[K_LEFT]:
        direction = "left"
        xc-=10
        

        
from pygame import*

screen=display.set_mode((1000,800))
running=True
startmatch()
while running:
    dis1=((xc-x)**2+(yc-y)**2)**.5
    screen.fill((255,255,255))
    
    for evnt in event.get():                
        if evnt.type == QUIT:
            import mainmenu
            running = False
    keys = key.get_pressed()
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    num=1
    
##    x+=vx
##    vy+=.1
##    y+=vy
    draw.circle(screen,(blue),(x,int(y)),size)
    draw.circle(screen,(0,255,0),(xc,int(yc)),10)

    if xc > x +5:                 # move bad guy - this is my AI
        x+=5                    
    elif xc < x-5:   
        x-=5        
    if yc > y +5:
        y+=5
    elif yc < y-5:
        y-=5
        
    if alive==True:
        score+=10
##    if x<0 or x>1000:
##        vx*=-1
##    if y<0 or y>800:
##        vy*=-1    

    if dis1<=1+atkrange:
        damage=2
        damaEN=True
        
##    if ((xc-x)**2 + (yc-y)**2)**0.5 < atkrange:   # check interactions
##        damage=2
##        damaEN=True
        
    if damaEN==True and damage==2:
        
        draw.circle(screen,(255,0,0),(xc,int(yc)),10)
        healthp1-=atk
        myClock.tick(30)
        
        
        damage=0
        damaEN=False
    
    if keys[K_RIGHT] or keys[K_LEFT]:
        walk()
        if keys[K_UP] :
            ONGROUND=False
            move="jump"
    if keys[K_UP] :
        ONGROUND=False
        move="jump"
    if move=="jump":
        yc-=20
        ONGROUND=False
        if ONGROUND==False: # if sprite is of the ground
            yc+=vy1    
            if yc >= 400:
                yc = 400
                vy1= 0
                ONGROUND=True
                move=""
            vy1+=1
    
    if keys[K_KP1] and dis1<=100:
        damage=1
        dama=True
    if damage==1 and dama==True:
        draw.circle(screen,(255,0,0),(x,int(y)),size)
        myClock.tick(30)
        enemyhealth-=5
        damage=0
        dama=False
    if score==2000:
        size+=5
        atk+=3
        atkrange+=2
        
    elif score==6000:
        size+=7
        atk+=10
        atkrange+=5

    elif score==11000:
        size+=10
        atk+=20
        atkrange+=7
    elif score==20000:
        enemyhealth+=10000
        size+=5
        
    elif enemyhealth<500:
        enemyhealth+=50
        
        
    if y==800:
        y=300

    if healthp1<=0:
        alive=False
        screen.fill((0,0,0))
        txtPosp2=arialFont2.render(("Game Over! Your score is "+str(score)),True,(red))
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
                score=0
                healthp1=5000
                enemyheath=10000
                size=10
                atkrange=20
                atk=1
                vy1=2
                x=100
                y=200
                vx=5
                vy=2 
                screen.fill((255,255,255))
                againgame=True
              
    if againgame==True:
        xc=300
        yc=400
        x=500
        y=0
        
        againgame=False
        startmatch()

    if Quit==True:
        import mainmenu
        
    healthdisplay()
    scoredisplay()
    offscreen(xc,yc)
    colour=((0,0,0))
    colour2=((0,0,0))
    myClock.tick(30)
    display.flip()
quit()
            
