town = input()
sales = float(input())

commission_percent = 0
if town == "Sofia":
    if sales < 0:
        print("error")
    elif 0 <= sales <= 500:
        commission_percent = 0.05
        final_commission = sales * commission_percent
        print(f"{final_commission:.2f}")
    elif sales <= 1000:
        commission_percent = 0.07
        final_commission = sales * commission_percent
        print(f"{final_commission:.2f}")
    elif sales <= 10000:
        commission_percent = 0.08
        final_commission = sales * commission_percent
        print(f"{final_commission:.2f}")
    elif sales > 10000:
        commission_percent = 0.12
        final_commission = sales * commission_percent
        print(f"{final_commission:.2f}")
    elif sales < 0:
        print("error")
elif town == "Varna":
    if sales < 0:
        print("error")
    elif 0 <= sales <= 500:
        commission_percent = 0.045
        final_commission = sales * commission_percent
        print(f"{final_commission:.2f}")
    elif sales <= 1000:
        commission_percent = 0.075
        final_commission = sales * commission_percent
        print(f"{final_commission:.2f}")
    elif sales <= 10000:
        commission_percent = 0.10
        final_commission = sales * commission_percent
        print(f"{final_commission:.2f}")
    elif sales > 10000:
        commission_percent = 0.13
        final_commission = sales * commission_percent
        print(f"{final_commission:.2f}")
    elif sales < 0:
        print("error")
elif town == "Plovdiv":
    if sales < 0:
        print("error")
    elif 0 <= sales <= 500:
        commission_percent = 0.055
        final_commission = sales * commission_percent
        print(f"{final_commission:.2f}")
    elif sales <= 1000:
        commission_percent = 0.08
        final_commission = sales * commission_percent
        print(f"{final_commission:.2f}")
    elif sales <= 10000:
        commission_percent = 0.12
        final_commission = sales * commission_percent
        print(f"{final_commission:.2f}")
    elif sales > 10000:
        commission_percent = 0.145
        final_commission = sales * commission_percent
        print(f"{final_commission:.2f}")
else:
    print("error")