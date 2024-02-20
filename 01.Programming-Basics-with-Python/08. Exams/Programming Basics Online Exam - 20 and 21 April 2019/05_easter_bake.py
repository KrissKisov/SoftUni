from math import ceil


num_easter_breads = int(input())
used_sugar_gr = 0
used_flour_gr = 0
max_sugar_per_bread = 0
max_flour_per_bread = 0

for _ in range(num_easter_breads):
    sugar = int(input())
    flour = int(input())
    used_sugar_gr += sugar
    used_flour_gr += flour

    if max_sugar_per_bread < sugar:
        max_sugar_per_bread = sugar

    if max_flour_per_bread < flour:
        max_flour_per_bread = flour

sugar_packs = ceil(used_sugar_gr / 950)
flour_packs = ceil(used_flour_gr / 750)

print(f"Sugar: {sugar_packs}")
print(f"Flour: {flour_packs}")
print(f"Max used flour is {max_flour_per_bread} grams, "
      f"max used sugar is {max_sugar_per_bread} grams.")
