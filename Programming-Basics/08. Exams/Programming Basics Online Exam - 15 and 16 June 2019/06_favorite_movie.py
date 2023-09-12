# command = input()
movie_count = 0
points = 0
best_movie = ""
while True:
    command = input()
    if command == "STOP":
        break

    current_movie = command
    movie_count += 1
    current_points = 0
    for letter in current_movie:
        current_points += ord(letter)

        if letter.isupper():
            current_points -= len(current_movie)
        elif letter.islower():
            current_points -= len(current_movie) * 2

    if current_points >= points:
        points = current_points
        best_movie = current_movie

    if movie_count == 7:
        print("The limit is reached.")
        break

    # command = input()

print(f"The best movie for you is {best_movie} with {points} ASCII sum.")
