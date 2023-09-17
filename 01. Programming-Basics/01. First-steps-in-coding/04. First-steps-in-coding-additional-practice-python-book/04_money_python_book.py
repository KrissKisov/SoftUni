# 1 биткойн = 1168 лева.
# 1 китайски юан = 0.15 долара.
# 1 долар = 1.76 лева.
# 1 евро = 1.95 лева.
BITCOIN = 1168
USD = 1.76
CNY_CHINESE_YUAN = 0.15 * USD
EURO = 1.95

bitcoin = int(input())
cny_chinese_yuan = float(input())
commission_rate = float(input()) / 100

euros_from_bitcoins = (bitcoin * BITCOIN) / EURO
euros_from_cny =(cny_chinese_yuan * CNY_CHINESE_YUAN) / EURO

amount_in_euros = (euros_from_bitcoins + euros_from_cny) - (euros_from_bitcoins + euros_from_cny) * commission_rate
print(f"{amount_in_euros:.2f}")