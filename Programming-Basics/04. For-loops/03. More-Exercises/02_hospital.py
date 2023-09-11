total_days = int(input())

doctors = 7
examined_patients = 0
unexamined_patients = 0
for day in range(1, total_days + 1):
    patients = int(input())
    if doctors >= patients:
        examined_patients += patients
    else:
        examined_patients += doctors
        unexamined_patients += patients - doctors
    day += 1
    if unexamined_patients > examined_patients and day % 3 == 0:
        doctors += 1

print(f"Treated patients: {examined_patients}.")
print(f"Untreated patients: {unexamined_patients}.")
