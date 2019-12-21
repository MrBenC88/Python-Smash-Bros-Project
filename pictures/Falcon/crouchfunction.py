#crouchfunction.py

def crouch1(x,y,direct,charactersymbol):
    Rightpic=image.load(charactersymbol+"CrouchR.png" )
    Leftpic=image.load(charactersymbol+"CrouchL.png" )
    if keys[K_s] :
        if direct=="Right":
            screen.blit(Rightpic,(x,y))
        elif direct=="Left":
            screen.blit(Leftpic,(x,y))
    elif keys[K_DOWN] :
        if direct=="Right":
            screen.blit(Rightpic,(x,y))
        elif direct=="Left":

  
##    if keys[K_DOWN]:
##        if ONGROUND==True and RunR==False and RunL==False:
##            if R==1:
##               crouch1(x,y,"Right","capt")
##            if L==1:
##                crouch1(x,y,"Left","capt")
##Example when to use it and how to
