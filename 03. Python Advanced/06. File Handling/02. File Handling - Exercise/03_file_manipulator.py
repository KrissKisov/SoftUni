import os


folder_path = "files_folder"


command = input().split("-")

while "End" not in command:

    file_name = command[1]
    file_path = os.path.join(folder_path, file_name)

    if "Create" in command:

        with open(file_path, "w"):
            pass

    elif "Add" in command:

        with open(file_path, "a") as file:
            file.write(f"{command[2]}\n")

    elif "Replace" in command:

        try:
            with open(file_path, "r+") as file:
                file_content = file.read()
                file_content = file_content.replace(command[2], command[3])

                file.seek(0)
                file.write(file_content)
                file.truncate()

        except FileNotFoundError:
            print("An error occurred")

    elif "Delete" in command:
        try:
            os.remove(file_path)

        except FileNotFoundError:
            print("An error occurred")

    command = input().split("-")