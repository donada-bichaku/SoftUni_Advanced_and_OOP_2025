# First we receive the number of rows and columns NxN chess board
# (with only knights on the board that attack one another)
N = int(input())

# Create an empty dict that will hold the information about the
# knight and attacks {(row, col): [(row, col), ..]}
knights = {}
knights_removed = 0

# Define which cells a knight can attack/move to
MOVES = [(-2, 1), (2, 1), (2, -1), (-2, -1), (-1, 2), (1, -2), (1, 2), (-1, -2)]

# Read rows of the matrix one by one and add knights as they are found,
# we do not need to keep the matrix composition as it will not be printed later
for row in range(N):
    line = input().strip()
    for col, char in enumerate(line):
        if char == 'K':
            knights[(row,col)] = set()

# Only for performance, so we don't have to check moves that are out of bounds
# and not in cells in the board, we create a function to check for those
def check_in_bounds(row, col):
    return 0 <= row < N and 0 <= col < N

# we check if the new position the knight moves to is an attack position,
# if not we can ingore it
def check_if_attacks(row, col):
    return (row, col) in knights

# One time only we check the moves for each knight and only add to our dict the ones that are attack moves and in bouds.
# From here on out we only work with those without running more loops for the moves.
def knight_moves(row, col):
    for move in MOVES:
        new_row = row + move[0]
        new_col = col + move[1]

        if not check_in_bounds(new_row, new_col):
            continue

        if not check_if_attacks(new_row, new_col):
            continue

        knights[(row, col)].add((new_row, new_col))


# Get one time the initial moves we care for. See func above.
for knight in knights.keys():
    knight_moves(*knight)

# Core logic to remove the knight with most attacks until all the knights left cannot attack each-other in one move only.
# Print only the number of knights that had to be removed.
while True:

    if all(len(attacks) == 0 for attacks in knights.values()):
        break

    max_attack = max(knights, key=lambda k: len(knights[k]))

    for attack_list in knights.values():
        if max_attack in attack_list:
            attack_list.remove(max_attack)

    knights.pop(max_attack)
    knights_removed += 1

print(knights_removed)




