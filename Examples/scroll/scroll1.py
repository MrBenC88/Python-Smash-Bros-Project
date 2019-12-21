# scroll1
# simple example of a scrolling background. This one uses just one picture that
# is drawn to a negative position.
from pygame import *
from random import randint

X=0
Y=1
VY=2

init()
size = width, height = 500, 500
screen = display.set_mode(size)
backPic = image.load("back.JPG")
guyPic = image.load("guy.png")


def drawScene(screen,guy):
    """ draws the current state of the game """
    screen.blit(backPic, (-guy[X],0))
    screen.blit(guyPic, (250,450-guy[Y]))
        
    display.flip()

'''
    The guy's x position is where he is in the "world" we then draw the map
    at a negative position to compensate.
'''
def moveGuy(guy):
    keys = key.get_pressed()
    
    if keys[K_LEFT] and guy[X] > 250:
        guy[X] -= 10
    if keys[K_RIGHT] and guy[X] < 3500:
        guy[X] += 10
    if keys[K_SPACE] and guy[Y]==0:
        guy[VY] = 10

    guy[Y]+=guy[VY]     # add current speed to Y
    if guy[Y] <= 0:
        guy[Y] = 0
        guy[VY] = 0
    guy[VY]-=.7     # add current speed to Y
    
    


running = True          # allows for early exit if you find the aliens too scary
myClock = time.Clock()  # although I don't need a constant frame rate here
guy = [250,0,0]

while running:
    for evnt in event.get():                # checks all events that happen
        if evnt.type == QUIT:
            running = False

    moveGuy(guy)        
        
    drawScene(screen, guy)
    myClock.tick(60)

quit()
