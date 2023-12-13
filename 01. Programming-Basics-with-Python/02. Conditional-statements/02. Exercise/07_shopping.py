budget = float(input())
video_card_count = int(input())
processor_count = int(input())
ram_memory_count = int(input())

video_card_price = 250
processor_price = (video_card_count * video_card_price) * 35 / 100
ram_memory_price = (video_card_count * video_card_price) * 10 / 100

amount_needed = (video_card_count * video_card_price) \
                + (processor_count * processor_price) \
                + (ram_memory_count * ram_memory_price)

if video_card_count > processor_count:
    amount_needed -= amount_needed * 15 / 100

if budget >= amount_needed:
    print(f"You have {budget - amount_needed:.2f} leva left!")
else:
    print(f"Not enough money! You need {amount_needed - budget:.2f} leva more!")
