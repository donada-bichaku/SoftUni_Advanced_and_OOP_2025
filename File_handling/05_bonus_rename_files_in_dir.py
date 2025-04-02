import os

directory = input("Enter a directory path: ")
string_to_replace = input("String to replace: ")
string_to_replace_with = input("String to replace with: ")

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)

    if os.path.isfile(file):
        name, ext = os.path.splitext(filename)
        new_name = f"{name.replace(string_to_replace, string_to_replace_with)}" + f"{ext}"
        new_file = os.path.join(directory, new_name)

        os.rename(file, new_file)


