#intro.py

running=True
from pygame import*
screen=display.set_mode((1000,800))
pic=False
intro=False
bombframe = 0
bombpics = []
for i in range(0,12):
    bombpics.append(image.load("Extra\\bomb" + str(i) + ".png"))
    
summonframe = 0
summonpics = []
for i in range(4):
    summonpics.append(image.load("Lucy//LuAttack2L" + str(i) + ".png"))


runframeR = 0
runpicsR = []
for i in range(5):
    runpicsR.append(image.load("Lucy\\LucyRunpicsL0" + str(i) + ".png"))

winframe = 0
winpics = []
for i in range(0,8):
    winpics.append(image.load("Lucy\\lucywin" + str(i) + ".png"))

introframe=0
intropics=[]
for i in range(2):
    intropics.append(image.load("intropic"+str(i)+".jpg"))
    
##init()
##mixer.music.load("Fairy Tail Natsu's Theme Extended   YouTube-[www_flvto_com].mp3")
##mixer.music.play()

x=1000
y=600

lustand=image.load("Lucy//LuAttack2L4.png")
intropic=image.load("intropic0.jpg")
intropic2=image.load("intropic1.jpg")
teampic=image.load("teamFT.png")
invisible=image.load("Lucy\\invisible.png")

screen.blit(intropic,(0,0))
init()
myClock=time.Clock()

while running:
    screen.blit(intropic,(0,0))
    for evt in event.get():
        if evt.type == QUIT:
            running = False
    if intro==True:
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        if mb[0]==1:
            import mainmenu

    if x!=700 and x!=500 and x!=550:
        screen.blit(runpicsR[runframeR],(x,y))
        runframeR += 1
        if runframeR == 5: runframeR = 0
        x-=10

    if x==700:
        screen.blit(summonpics[summonframe],(x,y))
        summonframe += 1
        if summonframe == 4: summonframe = 0
        myClock.tick()
##    elif x==700:
##        x-=10
        if x!=550:
            screen.blit(runpicsR[runframeR],(x,y))
            runframeR += 1
            if runframeR == 5: runframeR = 0
            x-=10
            
    if x==550:
        screen.blit(lustand,(x,y))
        screen.blit(bombpics[bombframe],(x-100,y-100))
        bombframe += 1
        myClock.tick(5)
        if bombframe == 12: bombframe = 0
        if bombframe == 0:
            pic=True
            myClock.tick(6)
            if x>500:
                x-=2
##            if x==500:
##                screen.blit(winpics[winframe],(x,y))
##                winframe += 1
##                if winframe == 8: winframe = 0
##                myClock.tick(5)                
    if pic==True:
        screen.blit(intropic2,(0,0))
        screen.blit(teampic,(130,60))
        screen.blit(winpics[winframe],(x,y))
        winframe += 1
        if winframe == 8: winframe = 0
        myClock.tick(5)
        intro=True
    if intro==True:
        screen.blit(intropics[introframe],(0,0))
        introframe += 1
        if introframe == 2: introframe = 0
        
        
        
        myClock.tick()
    display.flip()

quit()

