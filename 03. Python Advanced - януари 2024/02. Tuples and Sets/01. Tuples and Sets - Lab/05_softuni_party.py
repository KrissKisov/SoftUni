# 1

number_of_guests = int(input())
guests_reservations = set()

for _ in range(number_of_guests):
    guests_reservations.add(input())

command = input()
while command != "END":
    guests_reservations.discard(command)

    command = input()

print(len(guests_reservations))
guests_reservations = sorted(guests_reservations)
for guest in guests_reservations:
    print(guest)

# # 2
#
# number_of_guests = int(input())
# guests_reservations = set()
#
# for _ in range(number_of_guests):
#     guests_reservations.add(input())
#
# command = input()
# while command != "END":
#     guests_reservations.discard(command)
#
#     command = input()
#
# integers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
# regular_guests = set()
# vip_guests = set()
# for guest in guests_reservations:
#     if guest.startswith(integers):
#         vip_guests.add(guest)
#     else:
#         regular_guests.add(guest)
#
# vip = tuple(sorted(vip_guests))
# regular = tuple(sorted(regular_guests))
#
# print(len(vip) + len(regular))
# for guest in vip:
#     print(guest)
# for guest in regular:
#     print(guest)
