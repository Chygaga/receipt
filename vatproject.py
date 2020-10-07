import tkinter as tk
from tkinter import font
import requests


root = tk.Tk()

HEIGHT = 500
WIDTH = 600

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75, anchor='n')

entry = tk.Entry(frame, font=('Franklin Gothic Demi', 14))
entry.place(relheight=1, relwidth=0.65)

button = tk.Button(frame, text= "Print", font=('Franklin Gothic Demi', 14))
button.place(relx=0.7, relheight=1, relwidth=0.3)
#command=lambda: get_weather(entry.get())

lower_frame = tk.Frame(root, bg='#70c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relheight=0.6, relwidth=0.75, anchor='n')



root.mainloop()