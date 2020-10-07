import tkinter as tk
from tkinter import font
import requests
import os
import urllib.request

root = tk.Tk()

HEIGHT = 500
WIDTH = 600

#def test_function(entry):
    #print("this is the entry:", entry)

#api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={API key}
#5da5c4563f110a859d814096e8346c28

def format_response(weather):
    #print(weather)
    try:
        name = (weather['name'])
        desc = (weather['weather'][0]['description'])
        temp = (weather['main']['temp'])

        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name,desc,temp)
    except:
        final_str = 'There was a problem retrieving that information'
    return final_str
 
def get_weather(city):
    weather_key = '5da5c4563f110a859d814096e8346c28' 
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)

def get_icon(icon):
    url = 'https://openweathermap.org/img/w/'
    weather_response = requests.get(url)
    weather_json = weather_response.json()
    icon_name = weather_json['weather:'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = tk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img

    #print(weather['name'])
    #print(weather['weather'][0]['description'])
    #print(weather['main']['temp'])


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='./landscape7.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relheight=1, relwidth=1)


frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75, anchor='n')

entry = tk.Entry(frame, font=('Franklin Gothic Demi', 14))
entry.place(relheight=1, relwidth=0.65)

button = tk.Button(frame, text= "Get Weather", font=('Franklin Gothic Demi', 14), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relheight=0.6, relwidth=0.75, anchor='n')

bg_color = 'white'
label = tk.Label(lower_frame, font=('Franklin Gothic Demi', 16), anchor='nw', justify='left', bd=4 )
label.place(relheight=1, relwidth=1)

weather_icon = tk.Canvas(label, bg=bg_color, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

# icon image
#icon_image=tk.PhotoImage(file='landscape9.png')
#icon_canvas=tk.Canvas(bg='white', bd=0, highlightthickness=0)

#con_canvas.place(relx=0.80, rely=0.30, relheight=0.2, relwidth=0.1, anchor='ne')

#icon_canvas.create_image(2,2,image=icon_image, anchor='n')
#print(tk.font.families())



root.mainloop()
