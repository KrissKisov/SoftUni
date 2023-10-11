# def calculate_total_price(order: str, quantity: int) -> float:
#     total_price = 0
#     if order == "coffee":
#         total_price = quantity * 1.50
#     elif order == "water":
#         total_price = quantity * 1.00
#     elif order == "coke":
#         total_price = quantity * 1.40
#     elif order == "snacks":
#         total_price = quantity * 2.00
#
#     return total_price
#
#
# product_ordered = input()
# product_quantity = int(input())
# print(f"{calculate_total_price(product_ordered, product_quantity) :.2f}")

def calculate_total_price(order: str, quantity: int) -> float:
    total_price = 0
    if order == "coffee":
        total_price = f"{quantity * 1.50 :.2f}"
    elif order == "water":
        total_price = f"{quantity * 1.00 :.2f}"
    elif order == "coke":
        total_price = f"{quantity * 1.40 :.2f}"
    elif order == "snacks":
        total_price = f"{quantity * 2.00 :.2f}"

    return total_price


product_ordered = input()
product_quantity = int(input())
print(calculate_total_price(product_ordered, product_quantity))
