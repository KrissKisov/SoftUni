# greening_area_in_sq_meter = float(input())
# price_per_sq_meter = 7.61
# total_price = greening_area_in_sq_meter * price_per_sq_meter
# discount = total_price * 18 / 100
# final_price = total_price - discount
# print(f"The final boat_price is: {final_price} lv.")
# print(f"The discount is: {discount} lv.")
price_for_greening = float(input("Enter square meters: ")) * 7.61
discount = price_for_greening * 0.18
final_price = price_for_greening - discount
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")
