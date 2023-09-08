exam_start_hour = int(input())  # от 0 до 23;
exam_start_minute = int(input())  # от 0 до 59;
arrival_hour = int(input())  # от 0 до 23;
arrival_minute = int(input())  # от 0 до 59;

time_of_exam = exam_start_hour * 60 + exam_start_minute
time_of_arrival = arrival_hour * 60 + arrival_minute
status = ""  # "Late" "On time" "Early"
difference = 0
if time_of_arrival < (time_of_exam - 30):
    status = "Early"
    difference = time_of_exam - time_of_arrival
    if difference < 60:
        print(status)
        print(f"{difference} minutes before the start")
    else:
        if difference % 60 < 10:
            print(status)
            print(f"{difference // 60}:0{difference % 60} hours before the start")
        else:
            print(status)
            print(f"{difference // 60}:{difference % 60} hours before the start")
elif time_of_arrival > time_of_exam:
    status = "Late"
    difference = time_of_arrival - time_of_exam
    if difference < 60:
        print(status)
        print(f"{difference} minutes after the start")
    else:
        if difference % 60 < 10:
            print(status)
            print(f"{difference // 60}:0{difference % 60} hours after the start")
        else:
            print(status)
            print(f"{difference // 60}:{difference % 60} hours after the start")
else:
    status = "On time"
    difference = time_of_exam - time_of_arrival
    if difference == 0:
        print(status)
    else:
        print(status)
        print(f"{difference} minutes before the start")
