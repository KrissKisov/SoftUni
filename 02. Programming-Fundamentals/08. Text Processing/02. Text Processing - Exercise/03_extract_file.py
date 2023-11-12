file_path = input().split("\\")
file_and_extension = file_path[-1]
file_name, extension = file_and_extension.split(".")
print(f"File name: {file_name}")
print(f"File extension: {extension}")
