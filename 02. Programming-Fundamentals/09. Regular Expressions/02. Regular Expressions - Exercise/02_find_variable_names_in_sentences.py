import re

some_string = input()
regex = r"\b_{1}([A-Za-z0-9]+)\b"
result = re.findall(regex, some_string)
print(",".join(result))
