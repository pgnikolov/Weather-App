def add_favourite_city(city_name):
    with open('favourite_cities.txt', 'a') as f:
        f.write(city_name + "\n")


def get_favourite_cities():
    with open('favourite_cities.txt', 'r') as f:
        return f.readlines()


def remove_favourite_city(city_name):
    favourite_cities = get_favourite_cities()
    # create new list with all cities which are different from the one we want to remove
    filtered_cities = [city.strip() for city in favourite_cities if city.strip().lower() != city_name.lower()]
    with open("favourite_cities.txt", "w") as f:
        # from new list we put the cities back to the fav list order
        for city in filtered_cities:
            f.write(city + "\n")
