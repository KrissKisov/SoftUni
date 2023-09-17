# n = int(input())
#
# if n > 1:
#     for i in range(2, n // 2):
#         if n % i == 0:
#             print("False")
#             break
#     else:5
#         print("True")

num = int(input())  # num = 5; -> prime = [2; 3; 5]

for n in range(1, num + 1):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n)
