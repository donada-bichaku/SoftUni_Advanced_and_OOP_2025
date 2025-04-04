# You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated by a single space:
# •	Your position is marked with the symbol "A"
# •	Targets marked with the symbol "x"
# •	All of the empty positions will be marked with "."
# After the field state, you will be given an integer representing the number of commands you will receive. The possible commands are:
# •	"move {right/left/up/down} {steps}" – you should move in the given direction with the given steps.
# You can only move if the field you want to step on is marked with ".".
# •	"shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving).
# Beware that there might be targets that stand in the way of other targets, and you cannot reach them - you can shoot only the nearest target.
# When you have shot a target, the field becomes an empty position (".").
# Validate the positions since they can be outside the field.
# Keep track of all the shot targets:
# •	If at any point there are no targets left, end the program and print: "Training completed! All {count_targets} targets hit.".
# •	If, after you perform all the commands, there are some targets left print: "Training not completed! {count_left_targets} targets left.".
# Finally, print the index positions of the targets that you hit, as shown in the examples.

N = 5

targets_hit = []
shooter_pos = []
field = []
total_targets = 0

MOVES = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(N):
    field.append(input().split())
    if "A" in field[row]:
        shooter_pos = [row, field[row].index("A")]
    if "x" in field[row]:
        total_targets += field[row].count("x")

num_commands = int(input())

def check_in_bounds(r, c):
    return 0 <= r < N and 0 <= c < N

for _ in range(num_commands):
    command, *instructions = input().split()

    if command == "move":
        direction, steps = instructions[0], int(instructions[1])
        dr, dc = MOVES[direction]
        new_r = shooter_pos[0] + dr * steps
        new_c = shooter_pos[1] + dc * steps
        if not check_in_bounds(new_r, new_c) or field[new_r][new_c] != ".":
            continue
        shooter_pos = [new_r, new_c]

    else:
        dr, dc = MOVES[instructions[0]]
        bullet_r, bullet_c = shooter_pos
        while True:
            bullet_r += dr
            bullet_c += dc

            if not check_in_bounds(bullet_r, bullet_c):
                break
            if field[bullet_r][bullet_c] == "x":
                targets_hit.append([bullet_r, bullet_c])
                field[bullet_r][bullet_c] = "."
                break

        if len(targets_hit) == total_targets:
            print(f"Training completed! All {total_targets} targets hit.")
            break
else:
    print(f"Training not completed! {total_targets-len(targets_hit)} targets left.")

print("\n".join(str(el) for el in targets_hit))
