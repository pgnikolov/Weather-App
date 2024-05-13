from favourite_city import *
from current_weather import *
from forecast_weather import *


def weather_app():
    # load the list with saved fav cities
    favourite_cities = get_favourite_cities()

    while True:
        # user options
        print("1. View Favourite Cities")
        print("2. Add Favourite City")
        print("3. Remove Favorite City")
        print("4. Check Weather")
        print("5. Check 5-Day Forecast")
        print("6. Exit\n")

        user_choice = input("Enter the number of your choice: \n")

        if user_choice == "1":
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
            if not favourite_cities:
                print("No favorite cities to remove.")
            else:
                print("Select a favorite city to remove by number:")
                # print the cities with index + 1 infront
                for i, city in enumerate(favourite_cities):
                    print(f"{i + 1}. {city.strip()}")
                choice = input("Enter the number of the city you want to remove: ")
                try:
                    # city index is list number - 1
                    city_to_remove = favourite_cities[int(choice) - 1].strip()
                    remove_favourite_city(city_to_remove)
                    print(f"City '{city_to_remove}' removed from favorites.")
                    # handle in case of user input mistake
                except (ValueError, IndexError):
                    print("Invalid choice.")
                    continue

        elif user_choice == "4" or user_choice == "5":
            # user can choose from cities in fav list or other he can write
            city = input("Enter city name (or 'fav' for favorites): ")
            if city.lower() == "fav":
                if not favourite_cities:
                    print("No favorite cities found yet.")
                else:
                    print("Select a favorite city by number:")
                    # the same procedure as removing
                    for i, city in enumerate(favourite_cities):
                        print(f"{i + 1}. {city.strip()}")
                    choice = input("Enter choice: ")
                    # for option 4
                    if user_choice == "4":
                        try:
                            city = favourite_cities[int(choice) - 1].strip()
                        except (ValueError, IndexError):
                            print("Invalid choice.")
                            continue
                        print_weather(city)
                    # for optionn 5
                    if user_choice == "5":
                        try:
                            city = favourite_cities[int(choice) - 1].strip()
                        except (ValueError, IndexError):
                            print("Invalid choice.")
                        print_forecast(city)
        # EXIT OPTION
        elif user_choice == "6":
            print("Exit by user request")
            break

        else:
            print("Invalid option. Please try again.")


weather_app()
