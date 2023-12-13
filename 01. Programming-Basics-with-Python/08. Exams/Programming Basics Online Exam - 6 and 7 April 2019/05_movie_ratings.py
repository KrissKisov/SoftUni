import sys


number_of_movies = int(input())
highest_rating = -sys.maxsize
lowest_rating = sys.maxsize
film_highest_rating = ""
film_lowest_rating = ""
all_ratings = 0

for film in range(number_of_movies):
    movie_name = input()
    rating = float(input())
    if rating > highest_rating:
        highest_rating = rating
        film_highest_rating = movie_name
    elif rating < lowest_rating:
        lowest_rating = rating
        film_lowest_rating = movie_name
    all_ratings += rating

average_rating = all_ratings / number_of_movies
print(f"{film_highest_rating} is with highest rating: {highest_rating :.1f}")
print(f"{film_lowest_rating} is with lowest rating: {lowest_rating :.1f}")
print(f"Average rating: {average_rating :.1f}")
