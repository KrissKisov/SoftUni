a = int(input())
b = int(input())
maximum_generated_passwords = int(input())
passwords_count = 0
is_a_and_b_reached = False
for A in range(35, 55 + 1):
    for B in range(64, 96 + 1):
        for x in range(1, a + 1):
            for y in range(1, b + 1):
                passwords_count += 1
                if passwords_count > maximum_generated_passwords:
                    break
                print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")

                B += 1
                if B > 96:
                    B = 64

                A += 1
                if A > 55:
                    A = 35

                if y > b and x > a:
                    break
            is_a_and_b_reached = True
        if is_a_and_b_reached:
            break
    if is_a_and_b_reached:
        break
# a = int(input())
# b = int(input())
# max_count = int(input())
# counter = 0
#
# for A in range(35, 55):
#     for B in range(64, 96):
#         for x in range(1, a + 1):
#             for y in range(1, b + 1):
#                 counter += 1
#
#                 if counter > max_count:
#                     exit()
#                 print(f'{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}', end='|')
#                 if x == a and y == b:
#                     exit()
#                 A += 1
#                 if A > 55:
#                     A = 35
#                 B += 1
#                 if B > 96:
#                     B = 64
