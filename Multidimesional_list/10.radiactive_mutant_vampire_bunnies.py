def check_valid_index(row, col, isplayer=False):
    global wins
    if 0 <= row < rows and 0 <= col < cols:
        return True
    if isplayer:
        wins = True


def print_matrix(row_to_print, col_to_print):
    for r in range(row_to_print):
        for c in range(col_to_print):
            if [r, c] in bunnies:
                print("B", end="")
            else:
                print(".", end="")
        print()


rows, cols = [int(el) for el in input().split()]
matrix = []
player = []
bunnies = []

wins = False

directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

for row in range(rows):
    matrix.append([el for el in input()])
    if "P" in matrix[row]:
        player = [row, matrix[row].index("P")]
    for col, el in enumerate(matrix[row]):
        if el == "B":
            bunnies.append([row, col])

commands = input()

for command in commands:
    player_row, player_col = player[0] + directions[command][0], player[1] + directions[command][1]
    if check_valid_index(player_row, player_col, True):
        player[0], player[1] = player_row, player_col

    for bun in bunnies.copy():
        for value in directions.values():
            new_row, new_col = bun[0]+value[0], bun[1]+value[1]
            if check_valid_index(new_row, new_col) and [new_row, new_col] not in bunnies:
                bunnies.append([new_row, new_col])

    if wins:
        print_matrix(rows, cols)
        print(f"won: {player[0]} {player[1]}")
        exit()

    if player in bunnies:
        print_matrix(rows, cols)
        print(f"dead: {player[0]} {player[1]}")
        exit()
