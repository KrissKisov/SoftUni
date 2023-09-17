rent_hall = int(input())
statuette_prize = rent_hall - (rent_hall * 0.3)
catering = statuette_prize - (statuette_prize * 0.15)
sound = catering * 0.5

expenses = rent_hall + statuette_prize + catering + sound

print(f"{expenses:.2f}")