dimensions = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(dimensions)]
bombs = [[int(x) for x in el.split(",")] for el in input().split()]

around = {
    "start": [-1, -1],
    "end": [1, 1],
}

for bomb in bombs:
    damage = matrix[bomb[0]][bomb[1]]
    if damage < 0:
        continue

    row1 = bomb[0]+around["start"][0] if bomb[0]+around["start"][0] >= 0 else 0
    row2 = bomb[0]+around["end"][0] if bomb[0]+around["end"][0] < dimensions else dimensions - 1
    col1 = bomb[1]+around["start"][1] if bomb[1]+around["start"][1] >= 0 else 0
    col2 = bomb[1]+around["end"][1] if bomb[1]+around["end"][1] < dimensions else dimensions - 1

    for r in range(row1, row2+1):
        for c in range(col1, col2+1):
            matrix[r][c] -= damage if matrix[r][c] > 0 else 0

alive_cells = [num for line in matrix for num in line if num > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*row) for row in matrix]
