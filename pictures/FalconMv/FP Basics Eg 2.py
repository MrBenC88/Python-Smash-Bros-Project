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
    
    This example shows that as soon as we add complexity to a game we
    need to start breaking our code down into procedures. The goal is 
    for the mainline and each of the procedures to be simple. The overall 
    program may be complex, but we don't need to think about the the 
    whole program at any given time, we only need to focus our attention 
    on the mainline or any particular procedure.
'''

from pygame import *

def running():
    ''' check the event queue for an quit as well as the keyboard
        for the escape key. return false if either are seen true
        if we make it to the end.
    ''' 
    for evnt in event.get():
        if evnt.type == QUIT:
            return False
        
    keys = key.get_pressed()
    if keys[27]:
        return False
    return True

def moveBadGuys(badGuys, goodX, goodY):
    ''' The AI for the badGuys is real simple. If the goodGuy is left/right
        they move left/right. Same with up/down.
        badGuys - A list of bad guy positions ([x,y] lists)
        goodX, goodY - good guy position
    '''
    for guy in badGuys:
        if goodX > guy[0] +5:
            guy[0]+=5                    
        elif goodX < guy[0]-5:   
            guy[0]-=5        
        if goodY > guy[1] +5:
            guy[1]+=5
        elif goodY < guy[1]-5:
            guy[1]-=5


def checkHits(badGuys, goodX, goodY):
    ''' Both good and bad guys are circles, so to check hits we just need to check if the
        distance from center to center is < 20.
        For this simple example when they do collide we re-set the bad guy
    '''
    for i, guy in enumerate(badGuys):
        if ((goodX-guy[0])**2 + (goodY-guy[1])**2)**0.5 < 20:
            guy[0], guy[1] = i*200,0

def drawScene(screen, badGuys, goodX, goodY):
    ''' The scene is very simple. Each bad guy is a red circle, and the good guy is
        a green circle.
    '''
    screen.fill((0,0,0))
    for guy in badGuys:
        draw.circle(screen, red, guy, 20)

    draw.circle(screen, (0,255,0), (goodX, goodY), 20)
    display.flip()

    
init()
size = width, height = 1024, 768
screen = display.set_mode(size)
badX, badY = 0,0
red = 255, 0, 0
green = 0, 255, 0
badGuys = [[0,0], [200,0], [400,0], [600, 0],[800, 0],[1000, 0]]    # 6 x,y pairs 
myClock = time.Clock()

while running():
    goodX, goodY = mouse.get_pos()      # input from the user & move good guy

    moveBadGuys(badGuys, goodX, goodY)
    checkHits(badGuys, goodX, goodY)
    drawScene(screen, badGuys, goodX, goodY)
    myClock.tick(60)                    # delay

quit()
