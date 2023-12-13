def fair_distribution(wealth_list: list, minimum: int) -> bool:
    if sum(wealth_list) / len(wealth_list) >= minimum:
        for number in wealth_list:
            if number < minimum:
                number_index = wealth_list.index(number)
                difference = minimum - number
                max_wealth = max(wealth_list)
                max_wealth_index = wealth_list.index(max_wealth)
                if max_wealth - difference >= minimum:
                    wealth_list[max_wealth_index] -= difference
                    wealth_list[number_index] += difference
        return True
    return False


population = [int(num) for num in input().split(", ")]
minimum_wealth = int(input())

if fair_distribution(population, minimum_wealth):
    print(population)
else:
    print("No equal distribution possible")
