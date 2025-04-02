import os
from os import write

ABSOLUTE_PATH = os.path.join("..")
file_path = os.path.join(ABSOLUTE_PATH, "") # fill if you need the file not in the main directory
file_name = "file_to_be_deleted" # fill in the name of the file you want to delete, here we create it first and then delete it
file_abs_path = os.path.join(file_path, file_name)


os.remove(file_abs_path)





