from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk, width=500, height=400)
tk.title("Drawing")
canvas.pack()
ball = canvas.create_oval(20,20,70,70, fill= "blue")
for i in range (400):
    canvas.move(ball, 1, 2)
    tk.update()




canvas.mainloop()