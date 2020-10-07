from tkinter import *
import random
import time
tk = Tk()
canvas = Canvas(tk, width=500, height=400)
tk.title("Drawing")
canvas.pack()

class Ball:
    def __init__(self, color, size):
        self.shape = canvas.create_oval(20,20,size,size, fill= color)
        self.xspeed = random.randrange(1,8)
        self.yspeed = random.randrange(1,8)
    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= 400 or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= 500 or pos[0] <= 0:
            self.xspeed = -self.xspeed

newball = Ball("red", 50)
newball2 = Ball("blue", 70)
newball3 = Ball("green", 90)

while True:
    newball.move()
    newball2.move()
    newball3.move()
    tk.update()
    time.sleep(0.03)




canvas.mainloop()