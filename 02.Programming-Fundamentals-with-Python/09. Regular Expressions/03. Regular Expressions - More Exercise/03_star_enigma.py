import re

number_of_messages = int(input())
attacked_planets = []
destroyed_planets = []
for message in range(number_of_messages):
    encrypted_message = input()
    decrypting_key = len(re.findall('(?i)[star]', encrypted_message))

    decrypted_message = ""
    for symbol in encrypted_message:
        decrypted_message += chr(ord(symbol) - decrypting_key)

    pattern = r"@([A-Z][a-z]+)[^\@\-\!\:\>]*:(\d+)[^\@\-\!\:\>]*!(A|D)![^\@\-\!\:\>]*->(\d+)"
    match = re.search(pattern, decrypted_message)
    if match:
        if match.group(3) == "A":
            attacked_planets.append(match.group(1))
        elif match.group(3) == "D":
            destroyed_planets.append(match.group(1))
attacked_planets = sorted(attacked_planets)
destroyed_planets = sorted(destroyed_planets)
print(f"Attacked planets: {len(attacked_planets)}")
for planet in attacked_planets:
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in destroyed_planets:
    print(f"-> {planet}")
