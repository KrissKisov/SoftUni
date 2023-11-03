schedule = input().split(', ')

while True:
    command = input()
    if command == 'course start':
        break

    current_command = command.split(':')
    action = current_command[0]
    lesson = current_command[1]
    exercise = f'{lesson}-Exercise'

    if action == 'Add':
        if lesson not in schedule:
            schedule.append(lesson)

    elif action == 'Insert':
        index = int(current_command[2])
        if lesson not in schedule:
            schedule.insert(index, lesson)

    elif action == 'Remove':
        if lesson in schedule:
            if exercise in schedule:
                schedule.remove(exercise)
            schedule.remove(lesson)

    elif action == 'Swap':
        swap_lesson = current_command[2]
        swap_exercise = f'{swap_lesson}-Exercise'
        if lesson in schedule and swap_lesson in schedule:
            lesson_index = schedule.index(lesson)
            swap_lesson_index = schedule.index(swap_lesson)
            schedule[lesson_index], schedule[swap_lesson_index] = schedule[swap_lesson_index], schedule[lesson_index]

            if exercise in schedule:
                lesson_index = schedule.index(lesson)
                exercise_index = schedule.index(exercise)
                schedule.insert(lesson_index + 1, schedule.pop(exercise_index))

            if swap_exercise in schedule:
                swap_lesson_index = schedule.index(swap_lesson)
                swap_exercise_index = schedule.index(swap_exercise)
                schedule.insert(swap_lesson_index + 1, schedule.pop(swap_exercise_index))

    elif action == 'Exercise':
        if lesson in schedule and exercise not in schedule:
            lesson_index = schedule.index(lesson)
            schedule.insert(lesson_index + 1, exercise)

        elif lesson not in schedule:
            schedule.append(lesson)
            schedule.append(exercise)

for num in range(len(schedule)):
    print(f'{num + 1}.{schedule[num]}')
