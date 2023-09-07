# На площадката пред жилищен блок трябва да се поставят плочки.
# Площадката е с форма на квадрат със страна N метра.
# Плочките са широки „W“ метра и дълги „L“ метра.
# На площадката има една пейка с ширина M метра и дължина O метра.
# Под нея не е нужно да се слагат плочки. Всяка плочка се поставя за 0.2 минути.
#
# Напишете програма, която чете от конзолата размерите на площадката,
# плочките и пейката и пресмята колко плочки са необходими да се покрие площадката
# и пресмята времето за поставяне на всички плочки.
#
# Входни данни
# От конзолата се четат 5 числа:
#
# N – дължината на страна от площадката в интервала [1 … 100].
# W – широчината на една плочка в интервала [0.1 … 10.00].
# L – дължината на една плочка в интервала [0.1 … 10.00].
# М – широчината на пейката в интервала [0 … 10].
# О – дължината на пейката в интервала [0 … 10].
# Изходни данни
# Да се отпечатат на конзолата две числа:
#
# броя плочки, необходим за ремонта
# времето за поставяне
# Всяко число да бъде на нов ред и закръглено до втория знак след десетичната запетая.

n_play_ground_length = float(input())
w_tile_width = float(input())
l_tile_length = float(input())
m_bench_width = float(input())
o_bench_length = float(input())
time_per_tile = 0.2
tile_area = w_tile_width * l_tile_length
play_ground_area = n_play_ground_length * n_play_ground_length
bench_area = m_bench_width * o_bench_length
tiles_needed = (play_ground_area - bench_area) / tile_area
total_time = tiles_needed * 0.2

print(f"{tiles_needed:.2f}")
print(f"{total_time:.2f}")