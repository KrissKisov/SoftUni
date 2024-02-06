import os

path = os.path.join("files_folder", "numbers.txt")

file = open(path)
total_sum = 0
file_info = file.readlines()
file.close()

for line in file_info:
    total_sum += int(line.strip())

print(total_sum)
