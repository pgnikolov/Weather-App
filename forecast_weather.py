import requests
import json


def get_forecast_5days(city_name):
    # api for current weater
    forecast_url = (f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&'
                    f'appid={api_key}')

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

