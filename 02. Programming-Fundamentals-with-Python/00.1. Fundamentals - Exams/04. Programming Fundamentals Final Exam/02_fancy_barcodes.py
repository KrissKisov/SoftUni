import re

number_of_barcodes = int(input())
for _ in range(number_of_barcodes):
    some_string = input()
    pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
    barcode = re.findall(pattern, some_string)
    if barcode:
        group_pattern = r"\d"
        product_group = re.findall(group_pattern, "".join(barcode))

        if product_group:
            print(f"Product group: {''.join(product_group)}")

        else:
            product_group = "00"
            print(f"Product group: {product_group}")

    else:
        print("Invalid barcode")
