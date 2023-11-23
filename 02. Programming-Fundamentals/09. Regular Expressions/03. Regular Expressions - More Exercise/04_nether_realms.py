import re


def health(demon_name):
    pattern = r"[^0-9\+\-\*\/\.]"
    total_health = 0
    match = re.findall(pattern, demon_name)
    for character in match:
        total_health += ord(character)
    return total_health


def base_damage(demon_name):
    pattern = r"\-?(?!00)\d+\.?\d*"
    damage = 0
    match = re.findall(pattern, demon_name)
    if match:
        damage = sum([float(x) for x in match])
    for char in demon_name:
        if char == "*":
            damage *= 2
        elif char == "/":
            damage /= 2
    return f"{damage :.2f}"


demons = [x.strip() for x in input().split(",")]
demons = sorted(demons)
for demon in demons:
    demon_health = health(demon)
    demon_damage = base_damage(demon)
    print(f"{demon} - {demon_health} health, {demon_damage} damage")
