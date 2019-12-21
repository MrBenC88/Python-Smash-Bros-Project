# # WeAttack3R.py
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
waterWRect=Rect(total,100,75,50) # Damage Rect area of attack.
frame = 0
pics = []
for i in range(7):
    pics.append(image.load("WeAttack3R" + str(i) + ".png"))
waterWframe = 0
waterWpics = []
for i in range(3):
    waterWpics.append(image.load("WaterBulletR" + str(i) + ".png"))

while running:
    for evnt in event.get():                # checks all events that happen
        if evnt.type == QUIT:
            running = False
    x+=100
    screen.fill((150,220,150))
    total=100+x
    waterWRect=Rect(total,100,75,50)
    screen.blit(pics[frame],(100,100))
    frame += 1
    if frame == 7: frame = 0
    draw.rect(screen,(255,0,0),waterWRect,3)
    screen.blit(waterWpics[waterWframe],(total,100))
    waterWframe += 1
    if waterWframe == 3:
        waterWframe=0
        x=0

    myClock.tick(6)
    display.flip()
    
quit()
