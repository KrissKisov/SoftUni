from collections import deque


textiles = deque([int(x) for x in input().split()])
medications = [int(x) for x in input().split()]

created_items = {}
healing_item = {
    "Patch": 30,
    "Bandage": 40,
    "MedKit": 100,
}

while textiles and medications:
    textile = textiles.popleft()
    medicament = medications.pop()
    result = textile + medicament

    if result > healing_item["MedKit"]:

        if "MedKit" not in created_items.keys():
            created_items["MedKit"] = 0

        created_items["MedKit"] += 1
        medications[-1] += result - healing_item["MedKit"]
        continue

    for item in healing_item:

        if result == healing_item[item]:

            if item not in created_items.keys():
                created_items[item] = 0

            created_items[item] += 1
            break

    else:
        medications.append(medicament + 10)

if not medications and not textiles:
    print("Textiles and medicaments are both empty.")
elif not medications:
    print("Medicaments are empty.")
elif not textiles:
    print("Textiles are empty.")

if len(created_items) != 0:
    created_items = dict(sorted(created_items.items(), key=lambda x: (-x[-1], x[0])))
    [print(''.join(f"{k} - {v}")) for k, v in created_items.items()]

if medications:
    print(f"Medicaments left: {', '.join([str(x) for x in medications[::-1]])}")

if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
