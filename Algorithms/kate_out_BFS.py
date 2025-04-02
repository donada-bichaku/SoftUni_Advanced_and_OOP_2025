from collections import deque


def is_exit(r, c, rows, cols):
    # A cell is an exit if it lies on the boundary.
    return r == 0 or r == rows - 1 or c == 0 or c == cols - 1


def bfs_longest(maze, start_row, start_col):
    rows, cols = len(maze), len(maze[0])
    longest_exit = -1

    # Each state is a tuple: (row, col, moves, visited)
    # We use a frozenset for visited so that the state is hashable.
    initial_state = (start_row, start_col, 0, frozenset({(start_row, start_col)}))
    queue = deque([initial_state])

    while queue:
        r, c, moves, visited = queue.popleft()

        # If this state is an exit (and we're not at the starting cell), record it.
        if moves != 0 and is_exit(r, c, rows, cols):
            longest_exit = max(longest_exit, moves)

        # Explore neighbors (up, down, left, right).
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            # Check bounds, ensure not a wall, and not already visited in this path.
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#' and (nr, nc) not in visited:
                # Create a new visited set for this branch.
                new_visited = visited.union({(nr, nc)})
                queue.append((nr, nc, moves + 1, new_visited))

    return longest_exit


def main():
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

    result = bfs_longest(maze, start_row, start_col)

    if result == -1:
        print("Kate cannot get out")
    else:
        print(f"Kate got out in {result} moves")


if __name__ == "__main__":
    main()
