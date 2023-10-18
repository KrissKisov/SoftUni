population = [int(num) for num in input().split(", ")]
minimum_wealth = int(input())
distributed_wealth = []

if sum(population) / len(population) >= minimum_wealth:
    for number in population:
        if number < minimum_wealth:
            number_index = population.index(number)
            difference = minimum_wealth - number
            max_wealth = max(population)
            max_wealth_index = population.index(max_wealth)
            if max_wealth - difference >= minimum_wealth:
                population[max_wealth_index] -= difference
                population[number_index] += difference
    print(population)

else:
    print("No equal distribution possible")
