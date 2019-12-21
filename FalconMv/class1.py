#class1.py

class Person:
    def __init__(self,looks,favCol,name):
        self.looks=looks
        self.favCol=favCol
        self.name=name

    def admireSelf(self):
        if self.looks =="handsome" or \
           self.looks=="pretty" :
            print("What an inspiring sight!")
            
        else:
            print("You look",self.looks,"but it's what is in the inside that counts")

    def colour(self,c):
        if c==self.favCol:
            print("I love",c,"I am colouring everything",c)
            
        else:
            print(c,"is garbage. I'll use",self.favCol)
            
alex = Person("down-right stud","grey","Probably not Alex")
victor= Person("pretty","pink","Victoria")

alex.admireSelf()
alex.colour("grey")

victor.admireSelf()
victor.colour("Red")


