import tkinter as tk
from tkinter import font
import requests
from PIL import Image, ImageTk

HEIGHT = 500
WIDTH = 600

def clean_response(raw):
	try:
		name = raw['name']
		desc = raw['weather'][0]['description']
		temp = raw['main']['temp']
		final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' %(name, desc, temp)
		
	except: 
		final_str = "There was a problem retrieving that information!"

	return final_str


def get_weather():
	city = entry.get()
	API_KEY = 'c6ee0eb05ed3c05ae676faf46253305c'
	url = "https://api.openweathermap.org/data/2.5/weather"
	params = {'APPID': API_KEY, 'q': city, 'units': "metric"}
	response = requests.get(url, params=params)
	response = response.json()
	#To write the cleaned response into the label box.
	label['text'] = clean_response(response)

	#To display an image beside the displayed response.
	icon_name = response['weather'][0]['icon']
	open_image(icon_name)

def open_image(icon):
	size = int(lower_frame.winfo_height()*0.25)
	img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
	weather_icon.delete("all")
	weather_icon.create_image(0,0, anchor='nw', image=img)
	weather_icon.image = img

root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="landscape.png")
background_label = tk.Label(canvas, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(canvas, bg = "#80c1ff", bd=5)
frame.place(relx=0.5, rely= 0.1, relwidth=0.75, relheight=0.1, anchor = 'n')


entry = tk.Entry(frame, font=('Times New Roman', 16))
entry.place(relwidth=0.65, relheight=1)


button = tk.Button(frame, text="Get Weather!",font=('Times New Roman', 16) ,command = get_weather)
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(canvas, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Times New Roman', 16), anchor='nw', justify = 'left', bd = 4)
label.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(label)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

#print(tk.font.families())

root.mainloop()

