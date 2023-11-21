import re

list_of_participants = input().split(", ")
command = input()
results = {}
while command != "end of race":
    pattern = r"[^\W\_]"
    match = re.findall(pattern, command)
    current_match = "".join(match)
    name = ""
    distance = 0
    for element in current_match:
        if element.isalpha():
            name += element
        elif element.isdigit():
            distance += int(element)
    if name in list_of_participants:
        if name not in results.keys():
            results[name] = 0
        results[name] += distance
    command = input()

# creating list wit keys from results dictionary, sorted by dictionary's values in descending order and limited to 3.
sorted_results = [key for key, value in sorted(results.items(), key=lambda x: x[1], reverse=True)[:3]]
print(f"1st place: {sorted_results[0]}\n2nd place: {sorted_results[1]}\n3rd place: {sorted_results[2]}")
