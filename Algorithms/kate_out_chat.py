def is_exit(r, c, rows, cols):
    return r == 0 or r == rows - 1 or c == 0 or c == cols - 1


def dfs(maze, r, c, moves, visited):
    rows, cols = len(maze), len(maze[0])

    longest = -1

    if moves != 0 and is_exit(r, c, rows, cols):
        longest = moves

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and maze[nr][nc] != '#':

            visited.add((nr, nc))
            result = dfs(maze, nr, nc, moves + 1, visited)
            if result > longest:
                longest = result
            visited.remove((nr, nc))
    return longest


n = int(input())
maze = []
start_r = start_c = None

for i in range(n):
    row = list(input())
    maze.append(row)
    if 'k' in row:
        start_r, start_c = i, row.index('k')

visited = {(start_r, start_c)}
result = dfs(maze, start_r, start_c, 0, visited)

if result == -1:
    print("Kate cannot get out")
else:
    print(f"Kate got out in {result} moves")


# SOLUTION 2 _ BFS - breadth - first - search

# from collections import deque
#
#
# def is_exit(row, col, n, m):
#     # A cell is an exit if it lies on the boundary of the maze.
#     return row == 0 or row == n - 1 or col == 0 or col == m - 1
#
#
# def bfs(maze, start_row, start_col):
#     n = len(maze)  # number of rows
#     m = len(maze[0])  # number of columns
#     queue = deque()
#     # Initialize queue with starting position and 0 moves.
#     queue.append((start_row, start_col, 0))
#     # Initialize visited set with the starting cell.
#     visited = {(start_row, start_col)}
#
#     while queue:
#         row, col, moves = queue.popleft()
#         # If the current cell is an exit, return the move count.
#         if is_exit(row, col, n, m):
#             return moves
#
#         # Explore the neighbors (up, down, left, right).
#         for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             nr, nc = row + dr, col + dc
#             if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited:
#                 if maze[nr][nc] != '#':  # Only proceed if not a wall.
#                     visited.add((nr, nc))
#                     queue.append((nr, nc, moves + 1))
#
#     # If no exit is found, return None.
#     return None
#
#
# def main():
#     # Read the number of rows.
#     n = int(input().strip())
#     maze = []
#     start_row = start_col = None
#
#     # Read each row of the maze.
#     for i in range(n):
#         # For this exercise, we assume each row is given as a string without spaces.
#         row = list(input().rstrip('\n'))
#         maze.append(row)
#         if 'k' in row:
#             start_row = i
#             start_col = row.index('k')
#
#     # Get the move count for the exit, if any.
#     exit_moves = bfs(maze, start_row, start_col)
#
#     if exit_moves is not None:
#         print(f"Kate got out in {exit_moves} moves")
#     else:
#         print("Kate cannot get out")


# if __name__ == "__main__":
#     main()




