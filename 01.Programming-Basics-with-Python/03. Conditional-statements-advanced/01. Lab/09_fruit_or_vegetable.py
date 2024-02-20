product_name = input()

product_type = "unknown"
if product_name == "banana"\
        or product_name == "apple"\
        or product_name == "kiwi"\
        or product_name == "cherry"\
        or product_name == "lemon"\
        or product_name == "grapes":
    product_type = "fruit"
elif product_name == "tomato"\
        or product_name == "cucumber"\
        or product_name == "pepper"\
        or product_name == "carrot":
    product_type = "vegetable"

print(product_type)
