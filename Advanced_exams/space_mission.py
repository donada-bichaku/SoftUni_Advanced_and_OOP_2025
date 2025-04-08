N = int(input())
ship_resources = 100

MOVES = {
    "up": (-1 ,0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

field =[]
ship_r, ship_c = 0, 0

for row in range(N):
    field.append(input().split())
    if "S" in field[row]:
        ship_r, ship_c = row, field[row].index("S")

def check_in_bounds(row, col):
    return 0 <= row < N and 0 <= col < N

def meteor(row, col, fuel):
    fuel -= 5
    field[row][col] = "."
    return fuel

def space_station(fuel):
    fuel += 10
    if fuel > 100:
        fuel = 100
    return fuel

field[ship_r][ship_c] = "."

while True:
    command = input()
    new_r, new_c = ship_r + MOVES[command][0], ship_c + MOVES[command][1]
    if not check_in_bounds(new_r, new_c):
        print("Mission failed! The spaceship was lost in space.")
        break

    ship_r, ship_c = new_r, new_c
    ship_resources -= 5  # cost of moving

    cell = field[ship_r][ship_c]

    if cell == "M":
        ship_resources = meteor(ship_r, ship_c, ship_resources)
    elif cell == "R":
        ship_resources = space_station(ship_resources)
    elif cell == "P":
        print(f"Mission accomplished! The spaceship reached Planet B with {ship_resources} resources left.")
        break

    if ship_resources < 5 and cell not in ("P", "R"):
        print("Mission failed! The spaceship was stranded in space.")
        break


if field[ship_r][ship_c] not in ("R", "P"):
    field[ship_r][ship_c] = "S"
for row in field:
    print(" ".join(row))
