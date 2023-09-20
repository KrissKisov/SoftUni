animals = input()
animals_list = animals.split(", ")  # convert string to list without coma and single space
animals_list.append("farmer")  # adding the farmer to the list at the end
animals_list.reverse()  # reverse list, so farmer is first on index - 0

for animal in range(len(animals_list)):
    wolf = animals_list.index("wolf")  # find index of the "wolf"
    if wolf == 1:  # if wolf is just after the farmer in the list
        print("Please go away and stop eating my sheep")
        break
    else:  # {wolf - 1} -> the last sheep before the wolf in the list
        print(f"Oi! Sheep number {wolf - 1}! You are about to be eaten by a wolf!")
        break
