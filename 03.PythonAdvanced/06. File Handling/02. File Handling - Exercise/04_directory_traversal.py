import os


def save_extensions(dir_name):
    for each_file in os.listdir(dir_name):
        current_file_path = os.path.join(dir_name, each_file)

        if os.path.isfile(current_file_path):  # gets all files in 'Homework-File_Handling' folder
            current_extension = each_file.split(".")[-1]
            file_extensions[current_extension] = file_extensions.get(current_extension, []) + [each_file]

        elif current_file_path == os.path.join(dir_name, "directory_traversal"):
            # gets all files from 'directory_traversal' folder but none from 'example_folder' and 'files_folder'
            save_extensions(current_file_path)


directory = os.path.abspath(input("Please enter a '.': "))
file_extensions = {}

save_extensions(directory)

for key, value in file_extensions.items():
    file_extensions[key] = sorted(value)

file_extensions = dict(sorted(file_extensions.items(), key=lambda x: x[0]))

output_file = os.path.join(directory, "report.txt")

with open(output_file, "w") as file:

    for key, value in file_extensions.items():
        file.write(f".{key}""\n")

        for el in value:
            file.write(f"- - - {el}""\n")
