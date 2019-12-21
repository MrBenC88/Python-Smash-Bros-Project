# # NaRunR.py
# A Sprite is an old term that used to refer to specialized hardware that
# was used to draw characters is a video game sperate from the background
# Now a sprite just refers to a 2D object in a game, usually a character
# A spritesheet is a sheet of all of the natrunframes of animation that a character
# uses in a game to walk or preform actions.
#
# Pygame has a Sprite module that can help with sprites but it is a bit too
# advances for our needs. To achieve simple animation in python we simply
# display the natrunframes of the picture in order.

from pygame import *

init()
size = width, height = 800, 600
screen = display.set_mode(size)
running = True
myClock = time.Clock()

natrunframe = 0
natrunpics = []
for i in range(6):
    natrunpics.append(image.load("NaRunR" + str(i) + ".png"))

while running:
    for evnt in event.get():                # checks all events that happen
        if evnt.type == QUIT:
            running = False

    screen.fill((150,220,150))
    screen.blit(natrunpics[natrunframe],(100,100))
    natrunframe += 1
    if natrunframe == 6: natrunframe = 0
    display.flip()
    myClock.tick(5)
    
quit()
