one_lev_coins = int(input())
two_levs_coins = int(input())
five_levs_note = int(input())
amount = int(input())
for one_lev in range(one_lev_coins + 1):
    for two_levs in range(two_levs_coins + 1):
        for five_levs in range(five_levs_note + 1):
            if one_lev * 1 + two_levs * 2 + five_levs * 5 == amount:
                print(f"{one_lev} * 1 lv. + {two_levs} * 2 lv. + {five_levs} * 5 lv. = {amount} lv.")
