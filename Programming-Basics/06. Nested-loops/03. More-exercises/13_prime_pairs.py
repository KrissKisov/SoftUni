# first version(faster)
first_pair_beginning = int(input())
second_pair_beginning = int(input())
first_difference = int(input())
second_difference = int(input())
first_pair_ending = first_pair_beginning + first_difference
second_pair_ending = second_pair_beginning + second_difference
is_first_prime = False
is_second_prime = False
for first_pair in range(first_pair_beginning, first_pair_ending + 1):
    for second_pair in range(second_pair_beginning, second_pair_ending + 1):

        for first in range(2, first_pair):
            if first_pair % first == 0:
                is_first_prime = False
                break
            else:
                is_first_prime = True

        for second in range(2, second_pair):
            if second_pair % second == 0:
                is_second_prime = False
                break
            else:
                is_second_prime = True

        if is_first_prime and is_second_prime:
            print(f"{first_pair}{second_pair}")

# # second version(slower)
# first_pair_beginning = int(input())
# second_pair_beginning = int(input())
# first_difference = int(input())
# second_difference = int(input())
# first_pair_ending = first_pair_beginning + first_difference
# second_pair_ending = second_pair_beginning + second_difference
# is_first_prime = False
# is_second_prime = False
# for first_pair in range(first_pair_beginning, first_pair_ending + 1):
#
#     for first in range(2, first_pair):
#         if first_pair % first == 0:
#             is_first_prime = False
#             break
#         else:
#             is_first_prime = True
#
#     for second_pair in range(second_pair_beginning, second_pair_ending + 1):
#
#         for second in range(2, second_pair):
#             if second_pair % second == 0:
#                 is_second_prime = False
#                 break
#             else:
#                 is_second_prime = True
#
#         if is_first_prime and is_second_prime:
#             print(f"{first_pair}{second_pair}")
