def team_lineup(*info_tuple):
    info_dictionary = {}

    for info in info_tuple:
        player, country = info

        if country not in info_dictionary.keys():
            info_dictionary[country] = []

        info_dictionary[country].append(player)

    info_dictionary = dict(sorted(info_dictionary.items(), key=lambda x: (-len(x[-1]), x[0])))
    result = {}

    for key, values in info_dictionary.items():
        result[key] = [f"  -{value}\n" for value in values]

    return ''.join([f"{k}:\n{''.join(v)}" for k, v in result.items()])


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))

# # Output
# Germany:
#   -Manuel Neuer
#   -Toni Kroos
#   -Thomas Muller
# England:
#   -Harry Kane
#   -Raheem Sterling
# Portugal:
#   -Cristiano Ronaldo
#
# England:
#   -Harry Kane
#   -Raheem Sterling
# Argentina:
#   -Lionel Messi
# Brazil:
#   -Neymar
# France:
#   -Kylian Mbappe
# Portugal:
#   -Cristiano Ronaldo
#
# England:
#   -Harry Kane
#   -Raheem Sterling
#   -Harry Maguire
# Germany:
#   -Manuel Neuer
#   -Toni Kroos
#   -Thomas Muller
# Portugal:
#   -Cristiano Ronaldo
#   -Bruno Fernandes
#   -Bernardo Silva
