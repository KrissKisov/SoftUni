import re

links = []
pattern = r"(?i)www\.[A-Za-z0-9\-]+\.[a-z]+[.a-z+]*"
some_string = input()
while some_string:
    match = re.findall(pattern, some_string)
    if match:
        links.extend(match)

    some_string = input()

for link in links:
    print(link)
