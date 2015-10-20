# A way to add animation to tkinter

# Combining classes AnimationCanvas and AnimatedObject into one module

# Rhys Price Jones 7 April 2015

# AnimationCanvas extends tk.Canvas.  
# It allows you to add as many AnimatedObjects as you like with addItem()
# remove them with removeItem()
# start() and stop() are provided to start and stop the animation easily.
# The animate() method causes all the AnimatedObjects to start moving

import Tkinter as tk

SPEED = 40   # Smaller for faster, 40 means 1 frame per 40ms == 25 fps

class AnimationCanvas(tk.Canvas):
    items = []
    
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.going = False
        
    def addItem(self, item):
        self.items.append(item)            
 
    def removeItem(self, item):
        self.items.remove(item)  
                       
    def start(self):
        self.going = True
        self.after(0, self.animate())
        
    def animate(self):
        for item in self.items:
            item.move()
        if self.going:
            self.after(SPEED, self.animate)       # next update after SPEED milliseconds
             
    def stop(self):
        self.going = False   
    
# Class AnimatedObject is anything that can be added to a tkinter Canvas
# If it has a move() method, then  it can be added to an AnimationCanvas and animated


class AnimatedObject:       
                        
    def move(self):
        raise NotImplementedError('*move* method needs to be implemented in class inheriting from AnimatedObject.')
