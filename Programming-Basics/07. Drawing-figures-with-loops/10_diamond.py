# # solution 1
# n = int(input())
#
# outer_hyphen = (n - 1) // 2
# inner_hyphen = n - 2 * outer_hyphen - 2
# if inner_hyphen < 0:
#     for upper_row in range(1, (n + 1) // 2 + 1):
#         if upper_row == 1:
#             print(outer_hyphen * "-" + "*" + outer_hyphen * "-")
#         elif upper_row <= (n // 2) + 1:
#             outer_hyphen -= 1
#             inner_hyphen += 2
#             print(outer_hyphen * "-" + "*" + inner_hyphen * "-" + "*" + outer_hyphen * "-")
#
#     for lower_row in range(((n + 1) // 2) + 1, n + 1):
#         if lower_row < n:
#             outer_hyphen += 1
#             inner_hyphen -= 2
#             print(outer_hyphen * "-" + "*" + inner_hyphen * "-" + "*" + outer_hyphen * "-")
#         elif lower_row == n:
#             outer_hyphen += 1
#             inner_hyphen -= 2
#             print(outer_hyphen * "-" + "*" + outer_hyphen * "-")
#
# else:
#     for upper_row in range(1, n // 2 + 1):
#         if upper_row == 1:
#             print(outer_hyphen * "-" + "**" + outer_hyphen * "-")
#         elif upper_row <= (n // 2) + 1:
#             outer_hyphen -= 1
#             inner_hyphen += 2
#             print(outer_hyphen * "-" + "*" + inner_hyphen * "-" + "*" + outer_hyphen * "-")
#
#     for lower_row in range(((n + 1) // 2) + 1, n):
#         if lower_row < n:
#             outer_hyphen += 1
#             inner_hyphen -= 2
#             print(outer_hyphen * "-" + "*" + inner_hyphen * "-" + "*" + outer_hyphen * "-")
#         elif lower_row == n:
#             outer_hyphen += 1
#             inner_hyphen -= 2
#             print(outer_hyphen * "-" + "**" + outer_hyphen * "-")
#
# # solution 2
# n = int(input())
#
# outer_hyphens = (n - 1) // 2
# inner_hyphens = n - outer_hyphens * 2 - 2
# for top_rows in range(1, (n + 1) // 2 + 1):
#     if inner_hyphens < 0:
#
#         if top_rows == 1:
#             # outer_hyphens -= 1
#             # inner_hyphens += 2
#             print(outer_hyphens * "-" + "*" + outer_hyphens * "-")
#         else:
#             outer_hyphens -= 1
#             inner_hyphens += 2
#             print(outer_hyphens * "-" + "*" + inner_hyphens * "-" + "*" + outer_hyphens * "-")
#     else:
#
#         if top_rows == 1:
#             # outer_hyphens -= 1
#             # inner_hyphens += 2
#             print(outer_hyphens * "-" + "**" + outer_hyphens * "-")
#         else:
#             outer_hyphens -= 1
#             inner_hyphens += 2
#             print(outer_hyphens * "-" + "*" + inner_hyphens * "-" + "*" + outer_hyphens * "-")
#
# for bottom_rows in range((n + 1) // 2 + 1, n + 1):
#     if inner_hyphens > 0:
#
#         if bottom_rows == n:
#             outer_hyphens += 1
#             inner_hyphens -= 2
#             print(outer_hyphens * "-" + "*" + outer_hyphens * "-")
#         else:
#             outer_hyphens += 1
#             inner_hyphens -= 2
#             print(outer_hyphens * "-" + "*" + inner_hyphens * "-" + "*" + outer_hyphens * "-")

# solution 3
n = int(input())

outer_hyphen = (n - 1) // 2
inner_hyphen = n - 2 * outer_hyphen - 2
if inner_hyphen < 0:

    for row in range(1, n + 1):

        if row == 1:
            print(outer_hyphen * "-" + "*" + outer_hyphen * "-")

        elif row == n:
            outer_hyphen += 1
            inner_hyphen -= 2
            print(outer_hyphen * "-" + "*" + outer_hyphen * "-")

        elif row <= (n + 1) // 2:
            outer_hyphen -= 1
            inner_hyphen += 2
            print(outer_hyphen * "-" + "*" + inner_hyphen * "-" + "*" + outer_hyphen * "-")

        else:
            outer_hyphen += 1
            inner_hyphen -= 2
            print(outer_hyphen * "-" + "*" + inner_hyphen * "-" + "*" + outer_hyphen * "-")

else:

    for row in range(1, n):

        if row == 1:
            print(outer_hyphen * "-" + "**" + outer_hyphen * "-")

        elif row <= (n + 1) // 2:
            outer_hyphen -= 1
            inner_hyphen += 2
            print(outer_hyphen * "-" + "*" + inner_hyphen * "-" + "*" + outer_hyphen * "-")

        else:
            outer_hyphen += 1
            inner_hyphen -= 2
            print(outer_hyphen * "-" + "*" + inner_hyphen * "-" + "*" + outer_hyphen * "-")
