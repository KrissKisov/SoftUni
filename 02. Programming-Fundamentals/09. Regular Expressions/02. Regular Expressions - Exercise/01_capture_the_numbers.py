# import re
#
# some_string = input()
# while some_string:
#     regex = r"\d+"
#     match = re.findall(regex, some_string)
#     if match:
#         print(" ".join(match), end=" ")
#     some_string = input()

import re

all_matches = []
some_string = input()
while some_string:
    regex = r"\d+"
    match = re.findall(regex, some_string)
    if match:
        all_matches.append(" ".join(match))
    some_string = input()

print(" ".join(all_matches))
