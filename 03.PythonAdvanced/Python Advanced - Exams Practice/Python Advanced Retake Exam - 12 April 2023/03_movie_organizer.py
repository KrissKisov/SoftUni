def movie_organizer(*args):
    movies_dict = {}

    for movie, genre in args:

        if genre not in movies_dict.keys():
            movies_dict[genre] = []

        movies_dict[genre].append(movie)

    for key, values in movies_dict.items():
        movies_dict[key] = sorted(values)
    sorted_movies = dict(sorted(movies_dict.items(), key=lambda x: (-len(x[-1]), x[0])))

    result = ""
    for key, values in sorted_movies.items():
        result += f"{key} - {len(values)}\n"
        for value in values:
            result += f"* {''.join(value)}\n"

    return result


print(movie_organizer(
    ("The Matrix", "Sci-fi")))

print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
