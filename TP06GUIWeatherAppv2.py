## Weather app by Team Achievers 
# Built using OpenWeatherMap API

from tkinter import *
import tkinter as ttk
import requests
import json
from datetime import datetime

##Initialize Window

root =ttk.Tk()
root.geometry("500x500") 
root.resizable(5,5) 
root.config(bg="#26242f")
root.title("Weather App by Team Achievers")



## fetch and display weather info


def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


city_value = StringVar()

def showWeather():
    #API keys from the OpenWeatherMap dashboard
    api_key = ""  #sample API

# Get city name from user from the input field (later in the code)
    city_name=city_value.get()

    # API url
    weather_url = (f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")

    # Get the response from fetched url
    response = requests.get(weather_url)

    # changing response from json to python readable 
    weather_info = response.json()
    tfield.delete("1.0", "end")   #to clear the text field for every new output
 
#as per API documentation, if the code is 200, it means that weather data was successfully fetched
 
 
    if weather_info['code'] == 200:
        kelvin = 273.15 # value of kelvin
 
#Storing the fetched values of weather of a city
 
        temp = int(weather_info['main']['temp'] - kelvin)                                     #converting default kelvin value to Celcius
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
 
#assigning Values to our weather varaible, to display as output
         
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} \nSunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
 
 
 
    tfield.insert(INSERT, weather)   #to insert or send value in our Text Field to display output
 
 
city_head = Label(root, text='\nCheck the Real Time Weather of City!\nEnter City Name', font='Arial 12 bold',bg="#26242f",fg="lightblue")
city_head.pack(pady=10)

inp_city = ttk.Entry(root, textvariable=city_value, width=24, font='Arial 14 bold',bg="#26242f",fg="white")
inp_city.pack()

Button(root, command=showWeather, text="Show Real Time Weather", font="Arial 10", bg='#26242f', fg='white', activebackground="lightgreen", padx=5, pady=5).pack(pady=20)

# To show output
weather_now = ttk.Label(root, text=f"The Real Time Weather of the City!", font='Arial 12 bold', fg="lightgreen", bg="#26242f")
weather_now.pack(pady=10)

tfield = Text(root, width=50, height=12,bg="#26242f", fg= "white")
tfield.pack()

root.mainloop()