# FP Basics Eg 3.py
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
import math

def distance(x1,y1,x2,y2):
	return ((x1-x2)**2 + (y1-y2)**2)**0.5 

def running():
    ''' check the event queue for an quit as well as the keyboard
        for the escape key. return false if either are seen true
        if we make it to the end.
    ''' 
    for evnt in event.get():
        if evnt.type == QUIT:
            return False
        
    return True

def badMove(guy, x,y):
	''' The Bad Guy will now B-Line towards the player. Draw a similar
		triangle to get the x,y components of the move and use trig to 
		get the angle. The angle is needed to rotate the picture.
		returns (x,y,ang)
	'''

	dist = max(1,distance(guy[0], guy[1], x, y))
	moveX = (x- guy[0])*BADSPEED/dist
	moveY = (y- guy[1])*BADSPEED/dist
	ang = math.atan2(-moveY, moveX)
	return moveX, moveY, math.degrees(ang)
	
	
def moveBadGuys(badGuys, goodX, goodY):
    ''' The AI for the badGuys is real simple. If the goodGuy is left/right
        they move left/right. Same with up/down.
        badGuys - A list of bad guy positions ([x,y] lists)
        goodX, goodY - good guy position
    '''
    for guy in badGuys:
        mx, my, ang = badMove(guy, goodX, goodY)
        guy[0] += mx
        guy[1]+=my
        guy[2] = ang

def checkHits(badGuys, goodX, goodY):
    ''' Both good and bad guys are circles, so to check hits we just need to check if the
        distance from center to center is < 20.
        For this simple example when they do collide we re-set the bad guy
    '''
    for i, guy in enumerate(badGuys):
        if ((goodX-guy[0])**2 + (goodY-guy[1])**2)**0.5 < 20:
            guy[0], guy[1] = i*200,0

def drawScene(screen, badGuys, goodX, goodY, goodAng):
    ''' 
    '''
    screen.fill((0,0,0))
    for guy in badGuys:
        pic = transform.rotate(badPic, guy[2])
        screen.blit(pic, guy[:2])

    screen.blit(transform.rotate(goodPic, goodAng), (goodX, goodY))
    display.flip()

    
init()
size = width, height = 1024, 768
screen = display.set_mode(size)
badX, badY = 0,0
red = 255, 0, 0
green = 0, 255, 0
BADSPEED = 10
badGuys = [[0,0,0], [200,0,0], [400,0,0], [600, 0,0],[800, 0,0],[1000, 0,0]]    # 6 x,y pairs 
badPic = image.load("badship.png")
goodPic = image.load("goodship.png")
myClock = time.Clock()
mouse.set_visible(False)
goodX, goodY = 0,0

while running():
    oldX, oldY = goodX, goodY    
    goodX, goodY = mouse.get_pos()      # input from the user & move good guy
    goodAng = math.degrees(math.atan2(oldY-goodY, goodX-oldX))

    moveBadGuys(badGuys, goodX, goodY)
    checkHits(badGuys, goodX, goodY)
    drawScene(screen, badGuys, goodX, goodY, goodAng)
    myClock.tick(60)                    # delay

quit()
