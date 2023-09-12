hundreds_limit = int(input())
tenners_limit = int(input())
unities_limit = int(input())
is_prime = False
for hundreds in range(2, hundreds_limit + 1):
    if hundreds % 2 != 0:
        continue
    for tenners in range(1, tenners_limit + 1):
        if tenners > 1:
            for num in range(2, tenners):
                if tenners % num == 0:
                    is_prime = False
                    break
            else:
                is_prime = True
        else:
            continue
        for unities in range(2, unities_limit + 1):
            if unities % 2 != 0:
                continue
            if is_prime:
                print(f"{hundreds} {tenners} {unities}")
# hundreds_limit = int(input())
# tenners_limit = int(input())
# unities_limit = int(input())
# is_prime = False
# for hundreds in range(2, hundreds_limit + 1):
#     for tenners in range(2, tenners_limit + 1):
#         for unities in range(2, unities_limit + 1):
#             if hundreds % 2 != 0 or unities % 2 != 0:
#                 continue
#             for num in range(2, tenners):
#                 if tenners % num == 0:
#                     is_prime = False
#                     break
#             else:
#                 is_prime = True
#             if is_prime:
#                 print(f"{hundreds} {tenners} {unities}")
