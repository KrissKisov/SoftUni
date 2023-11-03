countries = input().split(', ')
capitals = input().split(', ')
country_capital = {countries[i]: capitals[i] for i in range(len(countries))}
for country, capital in country_capital.items():
    print(f'{country} -> {capital}')
