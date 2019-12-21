# FP Basics Eg 1.py
''' Main Game Loop
    ~~~~~~~~~~~~~~~~~~~~

    while playing:
        get input from user
        move good guy
        move bad guys
        move other stuff
        check interactions
        draw scene
        delay
'''

from pygame import *

init()
size = width, height = 1024, 768
screen = display.set_mode(size)
badX, badY = 0,0
red = 255, 0, 0
green = 0, 255, 0

running = True
myClock = time.Clock()

while running:
    for evnt in event.get():            # checks all events that happen
        if evnt.type == QUIT:
            running = False

    goodX, goodY = mouse.get_pos()      # input from the user & move good guy

    if goodX > badX +5:                 # move bad guy - this is my AI
        badX+=5                    
    elif goodX < badX-5:   
        badX-=5        
    if goodY > badY +5:
        badY+=5
    elif goodY < badY-5:
        badY-=5

    if ((goodX-badX)**2 + (goodY-badY)**2)**0.5 < 20:   # check interactions
        badX, badY = 0,0
      
    screen.fill((0,0,0))                # drawScene
    draw.circle(screen, red, (badX, badY), 20)
    draw.circle(screen, (0,255,0), (goodX, goodY), 20)
    display.flip()
    
    myClock.tick(60)                    # delay

quit()
