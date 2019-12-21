# Character selection screen

#___________________________________________________________________________________
from pygame import*
from random import*
from math import*

screen=display.set_mode((1000,800))
init()
myClock=time.Clock()

display.init()   # <--Must have for caption
display.set_caption("Clash of The FairyTail")


music=mixer.music.load("Fairy Tail - Grey Theme Music -.mp3")
mixer.music.play(-1)

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


running=True
count=0
click=False
click1=False
click2=False
#==============================================================================

def confirm(char1,char2):
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
        cha1=3
        screen.blit(gajpic,(300,160,300,500))
    elif char1=="Fr":
        cha1=4
        screen.blit(frpic,(0,50,300,500))
    elif char1=="Lu":
        cha1=5
        screen.blit(lupic,(355,160,300,500))
    elif char1=="We":
        cha1=6
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
        cha2=3
        screen.blit(gajpic,(600,160,300,500))
    elif char2=="Fr":
        cha2=4
        screen.blit(frpic,(280,50,300,500))
    elif char2=="Lu":
        cha2=5
        screen.blit(lupic,(650,160,300,500))
    elif char2=="We":
        cha2=6
        screen.blit(wepic,(600,235,300,500))
#==============================================================================
    
while running:
    for evnt in event.get():                
        if evnt.type == QUIT:
            if char1 !="" and char2 !="":
                import Newpvp
                running = False
            else:
                import mainmenu

            
    keys = key.get_pressed()
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    if mb[0]==1 or mb[2]==1 or mb[0]==1 and mb[2]==1:
        click=True
    
    if NatRect.collidepoint(mx,my):
        draw.rect(screen,blue,NatRect,2)
        if mb[0]==1:
            screen.blit(background,(0,0))
            char1SELECT="Natsu"
            char1="Na"

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
            
    elif optionRect.collidepoint(mx,my):
        draw.rect(screen,blue,optionRect,2)
        if mb[0]==1:
            print("import option menu")
            #import optionmenu
            #optionmenu.init()
            
    elif backRect.collidepoint(mx,my):
        draw.rect(screen,blue,backRect,2)
        if mb[0]==1 or mb[2]==1 and click==True:
            #print("import mainmenu")
            import mainmenu
            break

    if keys[K_KP_ENTER]:
        screen.blit(background2,(0,0))
        background=screen.copy()
    
            
    if keys[K_RETURN]: #press enter key and breaks this loop
        if char1 != "" and char2 != "":  #makes sure that characters are chosen :)
            break
            
    elif click==True:
        confirm(char1,char2)
#==============================================================================
        
    txtp1=font.render((char1SELECT),True,(0,100,255))
    txtp2=font.render((char2SELECT),True,(0,100,255))
    txtintructions1=font.render("Left Click for Player 1",True,(0,100,255))
    txtintructions2=font.render("Right Click for Player 2",True,(0,100,255))
    screen.blit(txtintructions1,intructions1Rect)
    screen.blit(txtintructions2,intructions2Rect)
    screen.blit(txtp1,Player1Rect)
    screen.blit(txtp2,Player2Rect)
    
    print(char1,char2)
    display.flip()

quit()
