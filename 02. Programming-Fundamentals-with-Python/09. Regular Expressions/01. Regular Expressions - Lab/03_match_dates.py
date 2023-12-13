# import re
#
# dates = input()
# pattern = r"\b(?P<Day>\d{2})(\.|-|/)(?P<Month>[A-Z][a-z]{2})(\2)(?P<Year>\d{4})\b"
# matched_dates = re.finditer(pattern, dates)
#
# for match in matched_dates:
#     match = match.groupdict()
#     print(f"Day: {match['Day']}, Month: {match['Month']}, Year: {match['Year']}")


import re

dates = input()
pattern = r"\b(\d{2})(\.|-|/)([A-Z][a-z]{2})(\2)(\d{4})\b"
matched_dates = re.findall(pattern, dates)

for match in matched_dates:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[4]}")
