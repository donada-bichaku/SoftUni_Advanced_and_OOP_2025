rows, cols = [int(el) for el in input().split()]

matrix = [[el for el in input().split()] for row in range(rows)]

found_matrices = 0

for r in range(rows - 1):
    for c in range(cols - 1):
        top_left = matrix[r][c]
        top_right = matrix[r][c+1]
        bottom_left = matrix[r+1][c]
        bottom_right = matrix[r+1][c+1]
        # if matrix[r][r] == matrix[r][r+1] == matrix[r+1][r] == matrix[r+1][r+1]:
        if top_right == top_left == bottom_right == bottom_left:
            found_matrices += 1

print(found_matrices)

