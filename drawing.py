from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk, width=500, height=400)
tk.title("Drawing")
canvas.pack()

canvas.create_line(0,0, 500, 400)
canvas.create_rectangle(100, 100, 200, 250, fill="red")
canvas.create_oval(30,30,70,70, fill= "blue")
canvas.create_polygon(350,20,250,300,500,300, fill="green")

for i in range(100):
    x1 = random.randrange(500)
    y1 = random.randrange(400)
    x2 = random.randrange(500)
    y2 = random.randrange(400)
    canvas.create_oval(x1,y1,x2,y2)



canvas.mainloop()