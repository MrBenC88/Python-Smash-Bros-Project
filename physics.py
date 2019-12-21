#physics.py

### Basic Physics
##   Displacement:
##       Distance in a direction.
##       x,y pixel location.
##       
##    Velocity:
##        Speed in a direction.
##        Change in displacement overtime. delta d/ delta t.
##
##    
##
running=True
from pygame import*
screen=display.set_mode((1000,800))

##init()
##mixer.music.load("Fairy Tail Natsu's Theme Extended   YouTube-[www_flvto_com].mp3")
##mixer.music.play()

x=100
y=200
vx=5
vy=2 

init()
myClock=time.Clock()

while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
    x+=vx
    vy+=.1
    y+=vy
    screen.fill((0,0,0))
    draw.circle(screen,(0,255,0),(x,int(y)),10)
    
    if x<0 or x>1000:
        vx*=-1
    if y<0 or y>800:
        vy*=-1


    display.flip()

quit()
