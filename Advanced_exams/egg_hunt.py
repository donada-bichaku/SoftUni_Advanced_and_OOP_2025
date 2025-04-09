
N = int(input())
bunny_eggs = 5
target = 10
bunny_init_r, bunny_init_c = 0, 0

MOVES = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    }

field = []

for row in range(N):
    line = [el for el in input()]
    field.append(line)
    if "B" in field[row]:
        bunny_init_r, bunny_init_c = row, field[row].index("B")
        field[bunny_init_r][bunny_init_c] = "."


def step_egg(r, c, eggs):
    field[r][c] = "."
    eggs += 1
    return eggs

def step_trap(r, c, eggs):
    field[r][c] = "."
    eggs -= 1
    return eggs

def step_magic(r, c, eggs):
    field[r][c] = "."
    eggs *= 2
    return eggs

def check_in_bounds(r, c):
    return 0 <= r < N and 0 <= c < N

bunny_r, bunny_c = bunny_init_r, bunny_init_c

while True:
    command = input()
    if command == "stop":
        break
    new_r, new_c = bunny_r + MOVES[command][0], bunny_c + MOVES[command][1]

    if not check_in_bounds(new_r, new_c):
        bunny_r, bunny_c = bunny_init_r, bunny_init_c
    else:
        bunny_r, bunny_c = new_r, new_c

    if field[bunny_r][bunny_c] == "E":
        bunny_eggs = step_egg(bunny_r, bunny_c, bunny_eggs)
        if bunny_eggs >= 10:
            break
    elif field[bunny_r][bunny_c] == "T":
        bunny_eggs = step_trap(bunny_r, bunny_c, bunny_eggs)
        if bunny_eggs <= 0:
            break
    elif field[bunny_r][bunny_c] == "F":
        bunny_eggs = step_magic(bunny_r, bunny_c, bunny_eggs)
        if bunny_eggs >= 10:
            break

if bunny_eggs >= 10:
    print(f"Easter Bunny wins! Collected eggs: {bunny_eggs}.")
elif bunny_eggs == 0:
    print("Game over! Easter Bunny has no eggs left.")
elif 0 < bunny_eggs < 10:
    print(f"Easter Bunny stopped hunting with {bunny_eggs} eggs.")

field[bunny_r][bunny_c] = "B"

for row in field:
    print(''.join(row))