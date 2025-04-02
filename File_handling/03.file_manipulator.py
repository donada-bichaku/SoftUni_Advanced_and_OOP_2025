import os

ABSOLUTE_PATH = os.path.join("..")


def create_file(name):
    with open(os.path.join(ABSOLUTE_PATH, name), 'w'): pass


def add_content(name, content):
    with open(os.path.join(ABSOLUTE_PATH, name), 'a') as file:
        file.write(f"{content}\n")


def replace_content(name, old, new):
    try:
        with open(os.path.join(ABSOLUTE_PATH, name), 'r+') as file:
            cont = file.read()
            cont = cont.replace(old, new)

            file.seek(0)

            file.write(cont)
            file.truncate()
    except FileNotFoundError:
        print("As error occurred.")


def delete_file(name):
    try:
        os.remove(os.path.join(ABSOLUTE_PATH, name))
    except FileNotFoundError:
        print("File doesn't exist")


commands = {
    "Add": add_content,
    "Remove": delete_file,
    "Replace": replace_content,
    "Create": create_file,
}

text = input()
while text != "End:":
    command, *instructions = text.split("-")
    if command in commands.keys():
        commands[command](*instructions)

    text = input()

