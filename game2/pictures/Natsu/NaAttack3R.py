# # NaAttack3R.py
# A Sprite is an old term that used to refer to specialized hardware that
# was used to draw characters is a video game sperate from the background
# Now a sprite just refers to a 2D object in a game, usually a character
# A spritesheet is a sheet of all of the frames of animation that a character
# uses in a game to walk or preform actions.
#
# Pygame has a Sprite module that can help with sprites but it is a bit too
# advances for our needs. To achieve simple animation in python we simply
# display the frames of the picture in order.

from pygame import *

init()
size = width, height = 800, 600
screen = display.set_mode(size)
running = True
myClock = time.Clock()
x=10
total=0
flameRect=Rect(total,100,75,50) # Damage Rect area of attack.
frame = 0
pics = []
for i in range(4):
    pics.append(image.load("NaAttack3R" + str(i) + ".png"))
flameframe = 0
flamepics = []
for i in range(8):
    flamepics.append(image.load("NaFireballR" + str(i) + ".png"))

while running:
    for evnt in event.get():                # checks all events that happen
        if evnt.type == QUIT:
            running = False
    x+=30
    screen.fill((150,220,150))
    total=100+x
    flameRect=Rect(total,100,75,50)
    
    screen.blit(pics[frame],(100,100))
    frame += 1
    if frame == 4: frame = 0
    draw.rect(screen,(255,0,0),flameRect,3)
    screen.blit(flamepics[flameframe],(total,100))
    flameframe += 1
    if flameframe == 8:
        flameframe=0
        x=0

    myClock.tick(6)
    display.flip()
    
quit()
