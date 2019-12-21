"""  Final Project Basics
    ~~~~~~~~~~~~~~~~~~~~
    Most grade 11 final projects involve a real-time game (a game where things
    are constantly moving on the screen.) For the most part this involves
    simulating some game world on the computer.  The most important thing
    to understand for this is the "main game loop."  During the main part 
    of your game the program will constantly be looping around at a fixed rate.
    The main game loop should look something like:
    
    while playing:
		get input from user
		move good guy
		move bad guys
		move other stuff
		check interactions
		draw scene
		delay
    
    By seperating the logically different actions in the main game loop we
    reduce the amount of unwanted interactions.  In this loop, THE ONLY PLACE
    THINGS ARE DRAWN IS IN "DRAW SCENE". The most common mistake 
    in final projects is to try to follow a simple action to it's logical 
    completion. e.g. when a shot is fired DO NOT, in the input procedure, try
    to follow the shot until it hits something. Instead the shot just becomes a 
    new object in the world to be tracked.
    
    Each time around the main game loop takes a set amount of time (e.g. 20 ms)
    each procedure in the loop should track what happens in that amount of time
    (e.g. move the good guy 5 pixels.) By having a bunch of things move a small 
    amount makes them look like they are moving simultaneously.
"""


