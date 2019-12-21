# # GaAttack3L.py
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
metalRect=Rect(total,100,75,50) # Damage Rect area of attack.
frame = 0
pics = []
for i in range(8):
    pics.append(image.load("GaAttack3L" + str(i) + ".png"))
metalframe = 0
metalpics = []
for i in range(7):
    metalpics.append(image.load("MetalAtkL" + str(i) + ".png"))

while running:
    for evnt in event.get():                # checks all events that happen
        if evnt.type == QUIT:
            running = False
    x-=20
    screen.fill((150,220,150))
    total=700+x
    metalRect=Rect(total,100,75,50)
    
    screen.blit(pics[frame],(700,100))
    if frame<=6:
        frame+=1
        if frame == 7:
            draw.rect(screen,(255,0,0),metalRect,3)
            screen.blit(metalpics[metalframe],(total,100))
            if metalframe<6:
                metalframe+=1
            if metalframe==7:
                frame=0
                total=0

    myClock.tick(6)
    display.flip()
    
quit()
