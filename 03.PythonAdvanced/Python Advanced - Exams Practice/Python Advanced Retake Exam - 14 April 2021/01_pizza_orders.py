from collections import deque


pizza_orders = deque(int(x) for x in input().split(", "))
employees_capacities = [int(x) for x in input().split(", ")]

made_pizza_orders = 0

while pizza_orders and employees_capacities:
    current_order = pizza_orders.popleft()

    if current_order <= 0 or current_order > 10:
        continue

    current_employee_capacity = employees_capacities.pop()

    if current_order <= current_employee_capacity:
        made_pizza_orders += current_order

    else:
        current_order -= current_employee_capacity
        pizza_orders.appendleft(current_order)
        made_pizza_orders += current_employee_capacity

if not pizza_orders:
    print(f"All orders are successfully completed!\n"
          f"Total pizzas made: {made_pizza_orders}\n"
          f"Employees: {', '.join(str(x) for x in employees_capacities)}")
else:
    print(f"Not all orders are completed.\n"
          f"Orders left: {', '.join(str(x) for x in pizza_orders)}")
