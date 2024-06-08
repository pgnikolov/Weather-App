# Weather Forecast 🌦️

<img src="https://github.com/pgnikolov/Weather-App/assets/151896883/c54946a9-86ed-4bf4-97fa-741522f608e9" width="750" height="400"/>

## Get Current & 5-Day Forecast with  <img src="https://openweathermap.org/themes/openweathermap/assets/img/logo_white_cropped.png" width="92" height="40"/>  API

This is a weather application that retrieves current weather conditions and a 5-day forecast for any city in the world. It utilizes the OpenWeatherMap API to fetch the data.

### Features 🧰

- Enter any city in the world and get the current weather conditions
- The app uses the datetime library to determine the timezone of the location entered by the user
- The app uses the Requests library to make an API call to OpenWeatherMap to get the current weather conditions and the five-days forecast
- The app uses json library API response in in the form of json
- The app gives you the opportunity to modify the list with favourite cities.

### Requirements 🗄️
- Python 3.x
- Requests library
- json
- datetime

### Installation ⚙️

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

1. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/).
2. Replace api_key in *current_weather.py* and *forecast_weather.py* with your actual API key.
3. Run the script:
```shell
python weather_app.py
```
4. The application will display a menu with options:
```
1. View Favourite Cities
2. Add Favourite City
3. Remove Favorite City
4. Check Weather
5. Check 5-Day Forecast
6. Exit
```
5. Select the desired option by entering the corresponding number.

* If your choice is "View Favourite Cities".
```
Enter the number of your choice: 
1
Your Favorite Cities:
1. Sofia
2. New York
3. London
4. Manchester
5. Paris
6. Burgas
```
* If your choice is "Add Favourite City" you will need to write the name of city you want to add.
```
Enter city name to add as favorite: Madrid
City 'Madrid' added to favorites.
```
* The option "Remove Favourite City" will ask you to write the number of the city in list.
```
1. Sofia
2. New York
3. London
4. Manchester
5. Paris
6. Burgas
7. Madrid
Enter the number of the city you want to remove: 7
City 'Madrid' removed from favorites.
```
* In options "Check Weather" and "Check 5-Day Forecast" you can choose whether to check the forecast for a city from the list of favorites by typing "fav" or to enter the name of another.
```
Enter city name (or 'fav' for favorites): fav
Select a favorite city by number:
1. Sofia
2. New York
3. London
4. Manchester
5. Paris
6. Burgas
```
* "Check Weather" gives the real time weather conditions.
```
Current Weather at New york: 
Clear sky 
Current Temperature: 21.07°C 
Temperature feels like: 20.88°C 
Max Temperature: 23.6°C 
Min Temperature: 18.09°C 
Today the sunrise is at 11:39:32 
Today the sunset is at 02:05:23 
Humidity: 63% 
Pressure: 1017hPa 
Visibility: 10.00Km. 
Wind: 
	Speed: 4.97Km/h 
	Direction: 180° SE
```
* Output of five-day forecast gives basic conditions and average temperature.
```
- 2024-05-14:
  Descriptions: scattered clouds, light rain
  Average Temp: 20.5°C

- 2024-05-15:
  Descriptions: overcast clouds, moderate rain, light rain
  Average Temp: 16.1°C

- 2024-05-16:
  Descriptions: moderate rain, light rain
  Average Temp: 14.8°C

- 2024-05-17:
  Descriptions: overcast clouds, scattered clouds, broken clouds
  Average Temp: 17.1°C

- 2024-05-18:
  Descriptions: overcast clouds, broken clouds
  Average Temp: 17.2°C

- 2024-05-19:
  Descriptions: overcast clouds
  Average Temp: 14.3°C
```

### Contributing 🤝
Contributions are welcome! Please fork the repository and submit a pull request.

### License 📝
This project is licensed under the MIT License. See the LICENSE file for details.

### Contact 📫
For any questions or feedback, please contact [![Gmail](https://img.shields.io/badge/-Gmail-c14438?style=flat&logo=Gmail&logoColor=white)](mailto:pgnikolov@gmail.com)
