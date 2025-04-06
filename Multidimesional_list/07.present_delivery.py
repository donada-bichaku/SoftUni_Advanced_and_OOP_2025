# get number of presents and size of neighborhood NxN
presents = int(input())
size = int(input())

neighborhood = []
santa_row = santa_col = 0
nice_kids = 0

# get Santa's starting position and nice kids count while also receiving line by line matrix/neighborhood.
# nice kids houses = "V", bad kids = "X", santa = "S", cookies = "C"
for row in range(size):
    line = input().split()
    neighborhood.append(line)
    for col in range(size):
        if line[col] == "S":
            santa_row, santa_col = row, col
        elif line[col] == "V":
            nice_kids += 1

happy_kids = 0


def get_next_position(direction, row, col):
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    return row + directions[direction][0], col + directions[direction][1]


def in_bounds(row, col, size):
    return 0 <= row < size and 0 <= col < size



while presents > 0:
    command = input()
    if command == "Christmas morning":
        break

    next_row, next_col = get_next_position(command, santa_row, santa_col)

    if not in_bounds(next_row, next_col, size):
        continue

    neighborhood[santa_row][santa_col] = "-"
    cell = neighborhood[next_row][next_col]

    if cell == "V":
        presents -= 1
        happy_kids += 1
    elif cell == "C":
        # Santa gives presents to all kids around him
        for d in ["up", "down", "left", "right"]:
            r, c = get_next_position(d, next_row, next_col)
            if in_bounds(r, c, size):
                target = neighborhood[r][c]
                if target in {"V", "X"}:
                    presents -= 1
                    if target == "V":
                        happy_kids += 1
                    neighborhood[r][c] = "-"
                    if presents == 0:
                        break

    neighborhood[next_row][next_col] = "S"
    santa_row, santa_col = next_row, next_col

    if presents == 0:
        break

# check if Santa ran out of presents with nice kids still waiting
if presents == 0 and happy_kids < nice_kids:
    print("Santa ran out of presents!")


for row in neighborhood:
    print(" ".join(row))

if happy_kids == nice_kids:
    print(f"Good job, Santa! {happy_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - happy_kids} nice kid/s.")



