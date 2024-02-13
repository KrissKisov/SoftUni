def forecast(*args):
    weather_location = {"Sunny": [], "Cloudy": [], "Rainy": []}

    for location, weather in args:

        weather_location[weather].append(location)
        weather_location[weather].sort()

    output = ""
    for weather, locations in weather_location.items():

        for location in locations:
            output += f"{location} - {weather}\n"

    return output


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
