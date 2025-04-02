import os

ABSOLUTE_PATH = os.path.join("..")

filename = "my_first_file.txt"
file_abs_path = os.path.join(ABSOLUTE_PATH, filename)

with open(file_abs_path, 'a') as new_file:
    new_file.write("I just created my first file!!")