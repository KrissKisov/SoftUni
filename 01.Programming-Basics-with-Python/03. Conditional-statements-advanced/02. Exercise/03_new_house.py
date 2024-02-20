type_of_flower = input()
flower_count = int(input())
budget = int(input())

rose_price = 5
dahlia_price = 3.8
tulip_price = 2.8
narcissus_price = 3
gladiolus_price = 2.5

final_price = 0
if type_of_flower == "Roses":
    if flower_count > 80:
        final_price = flower_count * rose_price * 0.9
    else:
        final_price = flower_count * rose_price
elif type_of_flower == "Dahlias":
    if flower_count > 90:
        final_price = flower_count * dahlia_price * 0.85
    else:
        final_price = flower_count * dahlia_price
elif type_of_flower == "Tulips":
    if flower_count > 80:
        final_price = flower_count * tulip_price * 0.85
    else:
        final_price = flower_count * tulip_price
elif type_of_flower == "Narcissus":
    if flower_count < 120:
        final_price = flower_count * narcissus_price * 1.15
    else:
        final_price = flower_count * narcissus_price
elif type_of_flower == "Gladiolus":
    if flower_count < 80:
        final_price = flower_count * gladiolus_price * 1.2
    else:
        final_price = flower_count * gladiolus_price

if budget >= final_price:
    print(f"Hey, you have a great garden with {flower_count} {type_of_flower} "
          f"and {budget - final_price :.2f} leva left.")
else:
    print(f"Not enough money, you need {final_price - budget :.2f} leva more.")
