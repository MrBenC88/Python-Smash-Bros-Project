# FP Basics Eg 4.py
''' 
    This example shows that as soon as we add complexity to a game we
    need to start breaking our code down into procedures. The goal is 
    for the mainline and each of the procedures to be simple. The overall 
    program may be complex, but we don't need to think about the the 
    whole program at any given time, we only need to focus our attention 
    on the mainline or any particular procedure.
'''

from pygame import *
from random import *
import math

class BadShip:
    ''' The BadShip class keeps tack of:
            startX, startY - so they can reset
            x,y - current position
            ang - current angle the guy is facing
            pic - image to display
            speed - currently just set as a constant, but could be easily modified
    '''
    
    def __init__(self, x, y, ang, pic):
        self.startX = x
        self.startY = y
        self.x = x
        self.y = y
        self.ang = ang
        self.pic = pic
        self.speed = 10

    def move(self, target):
        ''' The badguy simply B-Lines towards the goodguy. I use similar triangles to find
            how far in each x and y. I store the angle for later when we draw the guy
        ''' 
        dist = max(1,distance(self.x, self.y, target.x, target.y))
        moveX = (target.x - self.x)*self.speed/dist
        moveY = (target.y - self.y)*self.speed/dist
        self.ang = math.degrees(math.atan2(-moveY, moveX))
        self.x += moveX
        self.y += moveY

    def reset(self):
        ''' Simply goes back to where he started. '''
        self.x, self.y = self.startX, self.startY

    def draw(self, screen):
        ''' Draws self to the screen. '''
        pic = transform.rotate(self.pic, self.ang)
        screen.blit(pic, (self.x-40, self.y-40))

class GoodShip:
    ''' The GoodShip class keeps tack of:
            x,y - current position
            ang - current angle the guy is facing
            pic - image to display
    '''
    def __init__(self, pic):
        self.x = 0
        self.y = 0
        self.ang = 0
        self.pic = pic
        
    def move(self):
        ''' The good guy is pretty quick. He just moves to where the mouse is.
            We keep track of the angle to draw the guy later.
        '''        
        destX, destY = mouse.get_pos()
        if distance(self.x, self.y, destX, destY) > 2:
            self.ang = math.degrees(math.atan2(self.y - destY, destX - self.x))
        self.x, self.y = destX, destY


    
    def hit(self, other):
        ''' Still using simple circle/distance to check for collisions.
        '''        
        if distance(self.x, self.y, other.x, other.y ) < 40:
            return True
        else:
            return False
        
    def draw(self, screen):
        ''' Draws self to the screen. '''
        pic = transform.rotate(self.pic, self.ang)
        screen.blit(pic, (self.x-40, self.y-40))
        

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


def checkHits(badGuys, goodGuy):
    ''' Both good and bad guys are circles, so to check hits we just need to check if the
        distance from center to center is < 20.
        For this simple example when they do collide we re-set the bad guy
    '''
    for guy in badGuys:
        if goodGuy.hit(guy):
            guy.reset()

def drawScene(screen, badGuys, goodGuy):
    ''' We erase the old pictures by drawing a background picture. All of the ships know how
        to draw themselves.
    '''
    screen.blit(backPic, (0,0))
    for guy in badGuys:
        guy.draw(screen)
    goodGuy.draw(screen)
    display.flip()

def moveBadGuys(badGuys, goodGuy):
    ''' Each bad guy just needs to know where the good guy is and he will move towards him/her
    '''
    for guy in badGuys:
        guy.move(goodGuy)

def checkHits(badGuys, goodGuy):
    ''' I check the goodGuy against all of the bad guys to see if he hits any of them.
        Right now the bad guys just die, but obviously we could do a lot more with this.
    '''
    for guy in badGuys:
        if goodGuy.hit(guy):
            guy.reset()


init()
size = width, height = 1024, 768
screen = display.set_mode(size)
badPic = image.load("badship.png")
goodPic = image.load("goodship.png")
backPic = image.load("space.jpg").convert() # blits faster after convert(). Only convert the one because I
                                            # had problems with transparency.
goodGuy = GoodShip(goodPic)

# Add 5 guys to random starting spots
badGuys = []
for i in range(5):
    badGuys.append(BadShip(randint(0,width),randint(0,height),0,badPic))
    
myClock = time.Clock()
mouse.set_visible(False)

# The try ... except block prevents a painfull crash from pygame. Currently if it doesn't work I get
# no feedback as to what went wrong.
try:
    while running():
        goodGuy.move()

        moveBadGuys(badGuys, goodGuy)
        checkHits(badGuys, goodGuy)
        drawScene(screen, badGuys, goodGuy)
        myClock.tick(60)
except: pass
    
quit()
