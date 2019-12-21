# spriteEg2.py
# the first example has the animation display too quickly
# we can slow it down by slowing our frame rate but that
# will slow down the whole game. A better choice is to not
# advance our frame counter each time around the main loop

from pygame import *

init()
size = width, height = 800, 600
screen = display.set_mode(size)
running = True
myClock = time.Clock()

frameDelay = 6                              # only advance the frame
frame = 0                                   # every 6 loops
pics = []
for i in range(9):
    pics.append(image.load("ryu\\ryu" + str(i) + ".png"))

while running:
    for evnt in event.get():                # checks all events that happen
        if evnt.type == QUIT:
            running = False

    screen.fill((150,220,150))
    screen.blit(pics[frame],(100,100))
    
    frameDelay -= 1                         # count down to zero
    if frameDelay == 0:                     # then advance frame like normal
        frameDelay = 6
        frame += 1
        if frame == 9: frame = 0
        
    display.flip()
    myClock.tick(50)
    
quit()
