# Your task is to collect as many eggs as possible.
# On the first line, you will be given a number representing the size of the field. In the following few lines, you will be given a field with:
# •	One bunny - randomly placed in it and marked with the symbol "B"
# •	Number of eggs placed at different positions of the field and traps marked with "X"
# Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs.
# The directions that should be considered as possible are up, down, left, and right.
# If you reach a trap while checking some of the directions, you should not consider the fields after the trap in this direction.
# The bunny can move within the field and cannot go outside its boundaries. Do not consider negative indices as valid ones.
# Note: In some directions, the collected eggs can happen to be zero or a negative number.

N = int(input())
field = []
init_bunny_r, init_bunny_c = None, None
max_egg_count = float('-inf')
moves_for_max_eggs = []
max_direction = ""

for row in range(N):
    field.append(input().split())

    if "B" in field[row]:
        init_bunny_r, init_bunny_c = [row, field[row].index("B")]

MOVES = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


def check_in_bounds(r, c):
    return 0 <= r < N and  0 <= c < N

def check_if_better_direction(max_eggs, max_moves, max_dir, eggs, list_moves, dir):
    if eggs > max_eggs:
        return eggs, list_moves, dir
    return max_eggs, max_moves, max_dir

for direction, values in MOVES.items():
    bunny_r, bunny_c = init_bunny_r, init_bunny_c
    r, c = values[0], values[1]
    egg_count = 0
    moves = []
    while True:
        new_r, new_c = bunny_r + r, bunny_c + c

        if not check_in_bounds(new_r, new_c) or field[new_r][new_c] == "X":
            if egg_count > max_egg_count and moves:
                max_egg_count = egg_count
                moves_for_max_eggs = moves
                max_direction = direction
            break

        egg_count += int(field[new_r][new_c])
        moves.append([new_r, new_c])
        bunny_r, bunny_c = new_r, new_c

print(max_direction)
print("\n".join(str(el) for el in moves_for_max_eggs))
print(max_egg_count)


