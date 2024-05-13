import requests
import json
import datetime


def get_current_weather(city_name):
    # api for current weater
    weather_url = (f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&'
                   f'appid=548a48090e1be38d7e828325f094465b&units=metric')

    r = requests.get(weather_url)
    # error list at https://openweathermap.org/api/one-call-3#popularerrors

    if r.status_code == 404:
        print("City not found")
        return
    if r.status_code == 200:
        return json.loads(r.content)
    if r.status_code == 429:
        print("Error 429 - Too Many Requests.")
        return
    if r.status_code == 401:
        print("Please check your API and key")
        return


# WIND DIRECTION FUCTION
def get_wind_direction(data):
    cardinal = ""
    # wind directions https://dev.qweather.com/en/docs/resource/wind-info/
    if 0 <= data["wind"]["deg"] < 33.75:
        cardinal = "N"
    elif 33.75 <= data["wind"]["deg"] < 78.75:
        cardinal = "NE"
    elif 78.75 <= data["wind"]["deg"] < 123.75:
        cardinal = "E"
    elif 123.75 <= data["wind"]["deg"] < 213.75:
        cardinal = "SE"
    elif 213.75 <= data["wind"]["deg"] < 258.75:
        cardinal = "SW"
    elif 258.75 <= data["wind"]["deg"] < 303.75:
        cardinal = "W"
    elif 303.75 <= data["wind"]["deg"] < 348.75:
        cardinal = "NW"
    elif 348.75 <= data["wind"]["deg"] < 360:
        cardinal = "N"
    return cardinal


# OUTPUT CURRENT WEATHER FUNCTION
def print_weather(city_name):
    data = get_current_weather(city_name)
    if data:
        sunrise_time = datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime("%H:%M:%S")
        sunset_time = datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime("%H:%M:%S")
        cardinal = get_wind_direction(data)
        print(f'Current Weather at {city_name.capitalize()}: \n'
              f'{data["weather"][0]["description"].capitalize()} \n'
              f'Current Temperature: {data["main"]["temp"]}°C \n'
              f'Temperature feels like: {data["main"]["feels_like"]}°C \n'
              f'Max Temperature: {data["main"]["temp_max"]}°C \n'
              f'Min Temperature: {data["main"]["temp_min"]}°C \n'
              # surise and sunset only hours no date
              f'Today the sunrise is at {sunrise_time} \n'
              f'Today the sunset is at {sunset_time} \n'
              f'Humidity: {data["main"]["humidity"]}% \n'
              f'Pressure: {data["main"]["pressure"]}hPa \n'
              # visib. ot metri v km
              f'Visibility: {data["visibility"] / 1000:.2f}Km. \n'
              f'Wind: \n'
              # wind speed ot m/s v km/h - \t - 4 spaces
              f'\tSpeed: {data["wind"]["speed"] * 1.60934:.2f}Km/h \n'
              f'\tDirection: {data["wind"]["deg"]}° {cardinal}')
    else:
        return
