import requests
import datetime
import json


def add_favourite_city(city_name):
    with open('favourite_cities.txt', 'a') as f:
        f.write(city_name + "\n")


def get_favourite_cities():
    with open('favourite_cities.txt', 'r') as f:
        return f.readlines()


def remove_favourite_city(city_name):
    favourite_cities = get_favourite_cities()
    city_index = int(city_name) - 1
    if 0 <= city_index < len(favourite_cities):
        city_to_remove = favourite_cities.pop(city_index).strip()
        with open("favourite_cities.txt", "w") as f:
            f.writelines(city for city in favourite_cities)
        print(f"City '{city_to_remove}' removed from favorites.")
    else:
        print("Invalid choice.")


def get_forecast_5days(city_name):
    # api for current weater
    forecast_url = (f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&'
                    f'appid={api_key}=metric')

    r = requests.get(forecast_url)
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


def get_current_weather(city_name):
    # api for current weater
    weather_url = (f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&'
                   f'appid={api_key}&units=metric')

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


def print_forecast(city_name):
    forecast_data = get_forecast_5days(city_name)
    # new diictionary to store daily forecasts
    daily_forecasts = {}
    for day in forecast_data["list"]:
        # get the date info from datetime string
        date = day["dt_txt"].split()[0]
        if date not in daily_forecasts:
            # add the forecast for every day in the created dict.
            daily_forecasts[date] = {"descriptions": [], "temps": []}
        description = day["weather"][0]["description"]
        temp = day["main"]["temp"]
        # add all info for the date ( API gives 5 days every 3 hours forecast)
        daily_forecasts[date]["descriptions"].append(description)
        daily_forecasts[date]["temps"].append(temp)

    # get the avrg. temps with key, value for loop for every day
    for date, forecast in daily_forecasts.items():
        # temp round to the c losest num
        average_temp = round(sum(forecast["temps"]) / len(forecast["temps"]), 1)
        # descriptions we can have same discription 2-3 or motre times,
        # so we put them to set, to avoid duplicates
        descriptions = ", ".join(set(forecast["descriptions"]))
        print(f"\n- {date}:")
        print(f"  Descriptions: {descriptions}")
        print(f"  Average Temp: {average_temp}°C")


def weather_app():
    while True:
        print("\n1. View Favourite Cities")
        print("2. Add Favourite City")
        print("3. Remove Favorite City")
        print("4. Check Weather")
        print("5. Check 5-Day Forecast")
        print("6. Exit\n")

        user_choice = input("Enter the number of your choice: \n")

        if user_choice == "1":
            favourite_cities = get_favourite_cities()
            if not favourite_cities:
                print("No favourite cities found.")
            else:
                print("Your Favorite Cities:")
                for i, city in enumerate(favourite_cities):
                    print(f"{i + 1}. {city.strip()}")

        elif user_choice == "2":
            city = input("Enter city name to add as favorite: ")
            add_favourite_city(city)
            print(f"City '{city}' added to favorites.")

        elif user_choice == "3":
            favourite_cities = get_favourite_cities()
            if not favourite_cities:
                print("No favorite cities to remove.")
            else:
                print("Select a favorite city to remove by number:")
                for i, city in enumerate(favourite_cities):
                    print(f"{i + 1}. {city.strip()}")
                city_to_remove = input("Enter the number of the city you want to remove: ")
                remove_favourite_city(city_to_remove)

        # user can choose from cities in fav list or other he can write
        elif user_choice == "4" or user_choice == "5":
            city = input("Enter city name (or 'fav' for favorites): ")
            if city.lower() == "fav":
                favourite_cities = get_favourite_cities()
                if not favourite_cities:
                    print("No favorite cities found yet.")
                else:
                    print("Select a favorite city by number:")
                    for i, city in enumerate(favourite_cities):
                        print(f"{i + 1}. {city.strip()}")
                    choice = input("Enter choice: ")
                    if 1 <= int(choice) <= len(favourite_cities):
                        city = favourite_cities[int(choice) - 1].strip()
                        if user_choice == "4":
                            print_weather(city)
                        elif user_choice == "5":
                            print_forecast(city)
                    else:
                        print("Invalid choice.")
            else:
                if user_choice == "4":
                    print_weather(city)
                elif user_choice == "5":
                    print_forecast(city)
        # EXIT OPTION
        elif user_choice == "6":
            print("Exit by user request")
            break

        else:
            print("Invalid option. Please try again.")


weather_app()
