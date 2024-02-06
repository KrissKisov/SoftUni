# import os.path
#
# path = os.path.join("files_folder", "my_first_file.txt")
#
# file = open(path, "w")
# file.write("I just created my first file!")
# file.close()


# import os
#
#
# with open("files_folder/my_first_file.txt", "a") as file:  # Not a good practice for defining path
#     file.write("I just created my first file!")


import os


path = os.path.join("files_folder", "my_first_file.txt")

with open(path, "a") as file:
    file.write("I just created my first file!")
