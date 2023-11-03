data_list = []
while True:
    info = input()
    if info == 'stop':
        break
    data_list.append(info)

resources = {}
for i in range(0, len(data_list), 2):
    current_resource = data_list[i]
    quantity = int(data_list[i + 1])
    if current_resource not in resources:
        resources[current_resource] = quantity
    else:
        resources[current_resource] += quantity

for i in resources.keys():
    print(f'{i} -> {resources[i]}')
