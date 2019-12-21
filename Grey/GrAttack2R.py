# GrAttack2R.py
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
x=150
arrow=image.load("GrArrowR.png")


frame = 0
frame2=0
pics = []
for i in range(3):
    pics.append(image.load("GrAttack2R" + str(i) + ".png"))



while running:
    for evnt in event.get():                # checks all events that happen
        if evnt.type == QUIT:
            running = False
    screen.fill((150,220,150))
    x+=50
    arrowrect=Rect(x,100,30,30)
    screen.blit(arrow,arrowrect)
    draw.rect(screen,(255,0,0),arrowrect,2)
    
    
    if x>798 :
        x=150
    
    screen.blit(pics[frame],(100,100))
    frame += 1
    

    if frame == 3:
        while True:
            #screen.fill((150,220,150))
            
            frame=0
            break
        
    display.flip()
    myClock.tick(10)
    
quit()


