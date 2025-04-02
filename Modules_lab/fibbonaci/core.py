from Modules_lab.fibbonaci.main import create_sequence, locate_sequence

command = input()
sequence = []

while command != "Stop":
    if "Create"  in command:
        _, _, number = command.split()
        number = int(number)
        sequence = create_sequence(number)
        print(sequence)
    else:
        _, number = command.split()
        number = int(number)
        result = locate_sequence(number, sequence)
        print(result)



    command = input()