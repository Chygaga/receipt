from tkinter import *
import random
import time
tk = Tk()
canvas = Canvas(tk, width=500, height=400)
tk.title("Drawing")
canvas.pack()
ball = canvas.create_oval(20,20,70,70, fill= "blue")
xspeed = 6
yspeed = 4

while True:
    canvas.move(ball, xspeed, yspeed)
    pos = canvas.coords(ball)
    if pos[3] >= 400 or pos[1] <= 0:
        yspeed = -yspeed
    if pos[2] >= 500 or pos[0] <= 0:
        xspeed = -xspeed
    tk.update()
    time.sleep(0.03)




canvas.mainloop()