rows = int(input())
commands = input().split()

matrix = []
miner_position = [] # [row, col]
end = []

# total_coal = sum([line.count("c") for line in matrix])
total_coal, coal_collected = 0, 0

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for row in range(rows):
    matrix.append(input().split())

    if "s" in matrix[row]:
        miner_position = [row, matrix[row].index("s")]
        matrix[miner_position[0]][miner_position[1]] = "*"
    if "c" in matrix[row]:
        total_coal += matrix[row].count("c")

for command in commands:
    r, c = miner_position[0] + directions[command][0], miner_position[1] + directions[command][1]
    if not (0 <= r < rows and 0 <= c < rows):
        continue

    miner_position = [r, c]

    if matrix[r][c] == "c":
        coal_collected += 1
        matrix[r][c] = "*"
        if coal_collected == total_coal:
            print(f"You collected all coal! ({r}, {c})")
            exit()
    elif matrix[r][c] == "e":
        print(f"Game over! ({r}, {c})")
        exit()

print(f"{total_coal-coal_collected} pieces of coal left. ({r}, {c})")



