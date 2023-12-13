# open_tabs_count = int(input())
# salary = float(input())
#
# facebook_fine = 150
# instagram_fine = 100
# reddit_fine = 50
# for num in range(open_tabs_count):
#     website = input()
#     if website == "Facebook":
#         salary -= facebook_fine
#         if salary <= 0:
#             print(f"You have lost your salary.")
#             break
#     elif website == "Instagram":
#         salary -= instagram_fine
#         if salary <= 0:
#             print(f"You have lost your salary.")
#             break
#     elif website == "Reddit":
#         salary -= reddit_fine
#         if salary <= 0:
#             print(f"You have lost your salary.")
#             break
#
# print(int(salary))

open_tabs_count = int(input())
salary = float(input())

facebook_fine = 150
instagram_fine = 100
reddit_fine = 50
for num in range(open_tabs_count):
    website = input()
    if website == "Facebook":
        salary -= facebook_fine
    elif website == "Instagram":
        salary -= instagram_fine
    elif website == "Reddit":
        salary -= reddit_fine
    if salary <= 0:
        print(f"You have lost your salary.")
        break
else:
    print(int(salary))
