processors_number = int(input())
number_workers = int(input())
working_days = int(input())

employee_hours_per_day = 8
time_per_processor = 3
total_work_hours = working_days * number_workers * employee_hours_per_day
total_processors = total_work_hours // time_per_processor
processor_price = 110.10

if total_processors >= processors_number:
    profit = (total_processors - processors_number) * processor_price
    print(f"Profit: -> {profit :.2f} BGN")
else:
    losses = (processors_number - total_processors) * processor_price
    print(f"Losses: -> {losses :.2f} BGN")
