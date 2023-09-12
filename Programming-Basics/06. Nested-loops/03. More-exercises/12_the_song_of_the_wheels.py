special_value = int(input())
pass_count = 0
password = ""
is_password_found = False
for a in range(1, 10):
    for b in range(a + 1, 10):
        for c in range(1, 10):
            for d in range(1, c):
                if special_value == a * b + c * d:
                    print(f"{a}{b}{c}{d}", end=" ")
                    pass_count += 1

                    if pass_count == 4:
                        is_password_found = True
                        password = str(a) + str(b) + str(c) + str(d)
print()
if is_password_found:
    print(f"Password: {password}")
else:
    print("No!")
