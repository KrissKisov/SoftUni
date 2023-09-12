country = input()  # "Russia", "Bulgaria" или "Italy"
category = input()  # "ribbon", "hoop" или "rope"

difficulty_score = 0
performance_score = 0

if category == "ribbon":

    if country == "Russia":
        difficulty_score = 9.100
        performance_score = 9.400

    elif country == "Bulgaria":
        difficulty_score = 9.600
        performance_score = 9.400

    else:  # category == "Italy"
        difficulty_score = 9.200
        performance_score = 9.500

elif category == "hoop":

    if country == "Russia":
        difficulty_score = 9.300
        performance_score = 9.800

    elif country == "Bulgaria":
        difficulty_score = 9.550
        performance_score = 9.750

    else:  # category == "Italy"
        difficulty_score = 9.450
        performance_score = 9.350

else:  # category == "rope"

    if country == "Russia":
        difficulty_score = 9.600
        performance_score = 9.000

    elif country == "Bulgaria":
        difficulty_score = 9.500
        performance_score = 9.400

    else:  # category == "Italy"
        difficulty_score = 9.700
        performance_score = 9.150

total_score = difficulty_score + performance_score
percent_to_max_score = (20 - total_score) / 20 * 100

print(f"The team of {country} get {total_score :.3f} on {category}.")
print(f"{percent_to_max_score :.2f}%")
