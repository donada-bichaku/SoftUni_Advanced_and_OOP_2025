rows, cols = [int(x) for x in input().split(", ")]

matrix = [[int(el) for el in input().split(", ")] for _ in range(rows)]

max_sum = float('-inf')
sub_matrix = None

for row in range(rows-1):
    for col in range(cols-1):
        sum = matrix[row][col] + matrix[row][col+1] + matrix[row+1][col] + matrix[row+1][col+1]
        if sum > max_sum:
            max_sum = sum
            sub_matrix_start = [row, col]

# print(max_sum, sub_matrix_start)
[print(' '.join(str(matrix[row][col]) for col in range(sub_matrix_start[1], sub_matrix_start[1] + 2)))
 for row in range(sub_matrix_start[0], sub_matrix_start[0] + 2)]

print(max_sum)
