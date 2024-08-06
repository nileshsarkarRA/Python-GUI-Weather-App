## Simple Weather App using OpenWeatherMap API

## requests will allow to make HTTP requests from OpenWeatherMap APIs
import requests

## API Key for OpenWeatherMaps
api_key = "36fd9ee44c8d2376e8decd312f5ab28a"

## User Input for the City
user_city = input("Please Enter the Name of the City: ")

## Storing the website address in a variable for easiser access
WeatherDataFetch_url = (f"http://api.openweathermap.org/data/2.5/weather?q={user_city}&appid={api_key}")

## allows to make an HTTP request and stores the return values in the variable
response  = requests.get(WeatherDataFetch_url)

## When the API request is successfull (status code : 200) convert everthing to a dictionary
if response.status_code == 200:
    data = response.json() # converts all the data obtained from the server to .json format for easier access
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    temperature_Celsius = temperature - 273.15 # converts the temperature returned in kelvin to celsius
    rounded_temperature = round(temperature_Celsius, 2) # rounds off temperature in celsius to 2 decimal places
    
    # Display the output to user
    print(f"""
The Temperature in {user_city} is :

Temperature : {rounded_temperature} C
Description : {description}    
    """)
## Error handling in case of no response or error
else:
    print("""
Error Fetching Weather Data from Server. Try Again!!
Suggestion : Access to Internet is required to fetch data or check the API Key or too many requests!""")