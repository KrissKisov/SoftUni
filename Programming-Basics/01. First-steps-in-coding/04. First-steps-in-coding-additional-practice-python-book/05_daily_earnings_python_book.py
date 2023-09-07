''' Иван е програмист в американска компания и работи от вкъщи средно N дни в месеца,
като изкарва средно по M долара на ден.
В края на годината Иван получава бонус, който е равен на 2.5 месечни заплати.
От спечеленото през годината му се удържат 25% данъци.
Напишете програма, която да пресмята колко е чистата средна печалба на Иван на ден в лева,
тъй като той харчи изкараното в България.
Приема се, че в годината има точно 365 дни.
Курсът на долара спрямо лева ще се подава на функцията. '''

'''Входни данни
От конзолата се четат 3 числа:

На първия ред – работни дни в месеца. Цяло число в интервала [5 … 30].
На втория ред – изкарани пари на ден. Реално число в интервала [10.00 … 2000.00].
На третия ред – курсът на долара спрямо лева /1 долар = X лева/. Реално число в интервала [0.99 … 1.99].

Изходни данни
На конзолата да се отпечата едно число – средната печалба на ден в лева. 
Резултатът да се форматира до втората цифра след десетичния знак.'''

worked_days_per_mount = int(input())
earned_money_per_day = float(input())
currency_rate_usd_to_bgn = float(input())
monthly_earnings = worked_days_per_mount * earned_money_per_day
yearly_earnings = monthly_earnings * 12
yearly_bonus = monthly_earnings * 2.5
total_yearly_earnings = yearly_earnings + yearly_bonus
tax_deduction = total_yearly_earnings * 0.25
total_earnings_after_tax_in_usd = total_yearly_earnings - tax_deduction
total_earnings_after_tax_in_bgn = total_earnings_after_tax_in_usd * currency_rate_usd_to_bgn
average_daily_earnings_in_bgn_after_tax = total_earnings_after_tax_in_bgn / 365

print(f"{average_daily_earnings_in_bgn_after_tax:.2f}")