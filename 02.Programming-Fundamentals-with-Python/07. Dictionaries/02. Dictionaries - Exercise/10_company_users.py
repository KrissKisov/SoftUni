companies = {}
command = input()
while command != "End":
    company_name, employee_id = command.split(" -> ")
    if company_name not in companies.keys():
        companies[company_name] = []

    if employee_id not in companies[company_name]:
        companies[company_name].append(employee_id)

    command = input()

for company in companies.keys():
    print(f"{company}")
    for employee in companies[company]:
        print(f"-- {employee}")
