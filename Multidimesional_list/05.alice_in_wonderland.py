
N = int(input())
field = []
alice_pos, rabit_hole = [], []
tea_bags = 0


MOVES = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(N):
    field.append(input().split())

    if "A" in field[row]:
        alice_pos = [row, field[row].index("A")]
        field[row][alice_pos[1]] = "*"

def check_in_bounds(r, c):
    return 0 <= r < N and 0 <= c < N

while True:
    command = input()
    new_r, new_c = alice_pos[0] + MOVES[command][0], alice_pos[1] + MOVES[command][1]

    if not check_in_bounds(new_r, new_c):
        print("Alice didn't make it to the tea party.")
        break

    if field[new_r][new_c] == "R":
        field[new_r][new_c] = "*"
        print("Alice didn't make it to the tea party.")
        break

    if field[new_r][new_c] not in ("*", "."):
        tea_bags += int(field[new_r][new_c])

    field[new_r][new_c] = "*"
    alice_pos = [new_r, new_c]

    if tea_bags >= 10:
        print("She did it! She went to the party.")
        break

print("\n".join(" ".join(el for el in row) for row in field))












