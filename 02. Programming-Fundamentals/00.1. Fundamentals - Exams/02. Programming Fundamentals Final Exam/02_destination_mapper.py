import re

destinations = []
places = input()
pattern = r"([=\/])([A-Z]+[A-Za-z*]{2,})(\1)"
result = re.finditer(pattern, places)
for match in result:
    destinations.append(match.group(2))
travel_points = len("".join(destinations))
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
