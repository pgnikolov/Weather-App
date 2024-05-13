# Weather App 
# Get Current & 5-Day Forecast with OpenWeatherMap API

This is a weather application that retrieves current weather conditions and a 5-day forecast for any city in the world. It utilizes the OpenWeatherMap API to fetch the data.

### Features

- Enter any city in the world and get the current weather conditions
- The app uses the datetime library to determine the timezone of the location entered by the user
- The app uses the Requests library to make an API call to OpenWeatherMap to get the current weather conditions and the five-days forecast
- The app uses json library API response in in the form of json
- The app gives you the opportunity to modify the list with favourite cities.

### Requirements
- Python 3.x
- Requests library
- json
- datetime

### Installation

1. Clone this repository
```shell
git clone https://github.com/your-username/weather-app.git
```
2. Install required libraries:
```shell
pip install requests
pip install json
pip install datetime
```
### Usage

1. Obtain an API key from OpenWeatherMap (https://openweathermap.org/).
2. Replace api_key in rgb(*current_weather.py*) and *forecast_weather.py* with your actual API key.
3. Run the script:
```shell
python weather_app.py
```
4. The application will display a menu with options:

![choice](https://github.com/pgnikolov/Weather-App/assets/151896883/df7d8252-dbcc-4c68-82cb-2e1f8d19691c)

5. Select the desired option by entering the corresponding number.

6. Output of real time weather conditions:

![current](https://github.com/pgnikolov/Weather-App/assets/151896883/ef0e2a21-3e45-4649-906b-07f470e5df0c)

7. Output of five-day forecast:

![5days_forecast](https://github.com/pgnikolov/Weather-App/assets/151896883/31c6f285-e872-47b9-83a1-d8c714ff04a3)


