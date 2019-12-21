
from pygame import *
arrows =[(273,0,-5), (274,0,5),(275,5,0),(276,-5,0)]


class Guy:
    def __init__(self, x, y, baseName):
        self.x = x
        self.y = y
        self.pics = {}
        picFile = open(baseName+"/"+baseName+".txt")
        n = int(picFile.readline())
        for i in range(n):
            key = int(picFile.readline())
            st, end = map(int,picFile.readline().split(","))
            self.pics[key] = []
            for n in range(st,end+1):
                self.pics[key].append(image.load(baseName+"/"+baseName+str(n)+".bmp"))

        self.frame = 0
        self.frameDelay = 3
        self.direction = 274

    def move(self, k):
        if k == self.direction:
            self.frameDelay -= 1
            if self.frameDelay == 0:
                self.frameDelay = 3
                self.frame = (self.frame + 1) % len(self.pics[k])
            self.x += arrows[k-273][1]
            self.y += arrows[k-273][2] 
        elif k in self.pics:
            self.frameDelay = 3
            self.direction = k
            self.frame = 1
            self.x += arrows[k-273][1]
            self.y += arrows[k-273][2] 
        else:
            self.frame = 0


    def draw(self, screen):
        screen.blit(self.pics[self.direction][self.frame],(self.x,self.y))

init()
size = width, height = 800, 600
midx = width/2
midy = height/2
screen = display.set_mode(size)
mx, my = 0,0



def drawScene(screen,guy):
    screen.fill((255,255,255))
    guy.draw(screen)            
    display.flip()

running = True
myClock = time.Clock()
guts = Guy(midx,midy, "guts_walk")

while running:
    for evnt in event.get():                # checks all events that happen
        if evnt.type == QUIT:
            running = False

    keys = list(key.get_pressed())
    if True in keys:
        k = keys.index(True)
    else:
        k = 0
    guts.move(k)          
    drawScene(screen,guts)
    myClock.tick(20)                        
    
quit()
