# happiness = list(map(int, input().split()))
# factor = int(input())
# improved_happiness = [num * factor for num in happiness]
# average_happiness = sum(improved_happiness) / len(improved_happiness)
# average_count = 0
# total_count = len(improved_happiness)
# for person_happiness in improved_happiness:
#     if person_happiness >= average_happiness:
#         average_count += 1
# if average_count >= total_count / 2:
#     print(f"Score: {average_count}/{total_count}. Employees are happy!")
# else:
#     print(f"Score: {average_count}/{total_count}. Employees are not happy!")

happiness = list(map(int, input().split()))
factor = int(input())
improved_happiness = [num * factor for num in happiness]
average_happiness = sum(improved_happiness) / len(improved_happiness)
total_count = len(improved_happiness)
average_count = sum(person_happiness >= average_happiness for person_happiness in improved_happiness)

if average_count >= total_count / 2:
    print(f"Score: {average_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {average_count}/{total_count}. Employees are not happy!")
