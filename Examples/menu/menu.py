# menu.py

from pygame import *
from datetime import datetime
from math import *

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

def bottom(tb,bb):
    pts = [tb[3],tb[2],bb[2],bb[3]]
    draw.polygon(screen,(111,111,111),pts)
    draw.polygon(screen,OUTLINE,pts,2)
    
def top(tb,bb):
    pts = [bb[0],bb[1],tb[1],tb[0]]
    draw.polygon(screen,(211,211,211),pts)
    draw.polygon(screen,OUTLINE,pts,2)

def right(tb,bb):
    pts = [tb[1],bb[1],bb[2],tb[2]]
    draw.polygon(screen,(171,171,171),pts)
    draw.polygon(screen,OUTLINE,pts,2)

def left(tb,bb):
    pts = [bb[0],tb[0],tb[3],bb[3]]
    draw.polygon(screen,(161,161,161),pts)
    draw.polygon(screen,OUTLINE,pts,2)

def corners(x,y,s):
    return [(x,y), (x+s,y), (x+s,y+s), (x,y+s)]  

def dist(p1,p2):
    return hypot(p1[0]-p2[0],p1[1]-p2[1])

def check(r1,r2):
    return int(dist(r2,(x,y))-dist(r1,(x,y)))

def simple3D():
    global x,y
    TALL = .7
    SIZE = 150

    roofs = [(-100,100),(200,100),(200,400),(400,300)]
    arrows =[(273,0,-5), (274,0,5),(275,5,0),(276,-5,0)]
    running = True
    myClock = time.Clock()
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False

        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()

        keys = key.get_pressed()
        if keys[27]:running = False
        for a, vx, vy in arrows:
            if keys[a]:
                x += vx
                y += vy

        screen.fill((222,222,222))
        roofs.sort(key = cmp_to_key(check))
        for rx,ry in roofs:        
            topBox = corners(rx-x+400,ry-y+300,150)
            botBox = corners((rx-x)*TALL+400,(ry-y)*TALL+300,120)
            if y-4 < ry:
               top(topBox,botBox)
            if y+24 > ry+SIZE:
               bottom(topBox,botBox)
            if x+24 > rx+SIZE:
               right(topBox,botBox)
            if x-4 < rx:
               left(topBox,botBox)
            draw.rect(screen,(231,231,231),(rx-x+400,ry-y+300,150,150))
            draw.rect(screen,OUTLINE,(rx-x+400,ry-y+300,150,150),2)
            

        draw.circle(screen,(0,255,0),(400,300), 20)
        myClock.tick(50)
        display.flip()
    x,y = 0,0
    return "menu"

def instructions():
    running = True
    inst = image.load("instructions.png")
    inst = transform.smoothscale(inst, screen.get_size())
    screen.blit(inst,(0,0))
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        display.flip()
    return "menu"
        
def credit():
    running = True
    cred = image.load("credits.png")
    cred = transform.smoothscale(cred, screen.get_size())
    screen.blit(cred,(0,0))
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        display.flip()
    return "menu"
    

def story():
    running = True
    story = image.load("story.png")
    story = transform.smoothscale(story, screen.get_size())
    screen.blit(story,(0,0))
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        display.flip()
    return "menu"
    


def menu():
    running = True
    myClock = time.Clock()
    buttons = [Rect(200,y*60+200,100,40) for y in range(4)]
    vals = ["simple3D","instructions","credits","story"]
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"

        mpos = mouse.get_pos()
        mb = mouse.get_pressed()
        
        screen.fill((111,150,111))
        for r,v in zip(buttons,vals):
            draw.rect(screen,(222,55,55),r)
            #draw.circle(screen,(222,55,55),(r.x+50,r.y+20),20)
            if r.collidepoint(mpos):
                draw.rect(screen,(0,255,0),r,2)
                if mb[0]==1:
                    return v
            else:
                draw.rect(screen,(255,255,0),r,2)
                
        display.flip()

# This is the important part of the example.
# The idea is we have a variable (page) that keeps
# track of which page we are one. We give control
# of the program to a function until it is done and
# the program returns the new page it should be on.
screen = display.set_mode((800, 600))
running = True
x,y = 0,0
OUTLINE = (150,50,30)
page = "menu"
while page != "exit":
    if page == "menu":
        page = menu()
    if page == "simple3D":
        page = simple3D()    
    if page == "instructions":
        page = instructions()    
    if page == "story":
        page = story()    
    if page == "credits":
        page = credit()    
    
quit()
