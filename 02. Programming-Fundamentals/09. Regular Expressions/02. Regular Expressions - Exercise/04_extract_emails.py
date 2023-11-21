import re

some_string = input()
pattern = (r"((?<=)^|\s)(\b[A-Za-z0-9]+[\.\-\_]?[A-Za-z0-9]*"
           r"@(([A-Za-z]+\-?([A-Za-z]*[A-Za-z]+)?\-?[A-Za-z]*)\.[A-Za-z]+(\-?)(\.[A-Za-z]*)?)\b)")

emails = re.finditer(pattern, some_string)
for each_email in emails:
    print(each_email.group(2))
