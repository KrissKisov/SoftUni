from collections import deque


bowls_of_ramen = [int(x) for x in input().split(", ")]
customers_queue = deque([int(x) for x in input().split(", ")])

while bowls_of_ramen and customers_queue:

    current_bowl = bowls_of_ramen.pop()
    current_customer = customers_queue.popleft()

    if current_bowl == current_customer:
        continue

    elif current_bowl > current_customer:
        current_bowl -= current_customer
        bowls_of_ramen.append(current_bowl)

    elif current_bowl < current_customer:
        current_customer -= current_bowl
        customers_queue.appendleft(current_customer)

if not customers_queue:
    print("Great job! You served all the customers.")

    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_of_ramen)}")

else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers_queue)}")
