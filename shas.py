import turtle
joan = turtle.Pen()
i=0
while i < 4:
    joan.forward(100)
    joan.left(90)
    i +=1
joan.forward(250)
i=0
while i < 3:
    joan.left(120)
    joan.forward(150)
    i +=1
joan.right(90)
i=0
while i < 3:
    joan.forward(120)
    joan.right(90)
    i +=1

turtle.mainloop()