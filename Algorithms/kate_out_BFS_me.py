from collections import deque
from copy import deepcopy


def is_exit(r, c, rows, cols):
    return r == 0 or r == rows - 1 or c == 0 or c == cols - 1


def bfs(maze, start_row, start_col):

    longest_exit = -1

    initial_state = [start_row, start_col, 0, {(start_row, start_col)}]
    queue = deque([initial_state])

    while queue:
        curr_r, curr_c, moves, visited = queue.popleft()

        if is_exit(curr_r, curr_c, ROWS, COLS): # not checking if moves > 0
            longest_exit = max(longest_exit, moves)

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r, new_c = curr_r + dr, curr_c + dc
            if 0 <= new_r < ROWS and 0 <= new_c < COLS and maze[new_r][new_c] != "#" and (new_r, new_c) not in visited:
                new_visited = visited.union({(new_r, new_c)})
                # new_visited.append((new_r, new_c))
                queue.append([new_r, new_c, moves+1, new_visited])

    return longest_exit


n = int(input().strip())
maze = []
start_row = start_col = None

for i in range(n):
    # Read each maze row as a list of characters.
    row = list(input().rstrip('\n'))
    maze.append(row)
    if 'k' in row:
        start_row = i
        start_col = row.index('k')

ROWS, COLS = len(maze), len(maze[0])

max_num_moves = bfs(maze, start_row, start_col)

if max_num_moves == -1:
    print("kate is stuck")
else:
    print(f"kate got out in {max_num_moves}")

