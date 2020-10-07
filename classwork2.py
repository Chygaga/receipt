import turtle
joan = turtle.Pen()
def shapeFunction(l):
    i=0
    while i < 4:
        joan.forward(l)
        joan.left(90)
        i +=1

shapeFunction(60)
joan.forward(150)
shapeFunction(100)

turtle.mainloop()

