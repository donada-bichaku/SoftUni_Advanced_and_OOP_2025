dimension = 3

rows, cols = [int(el) for el in input().split()]

matrix = [[int(el) for el in input().split()] for row in range(rows)]
max_sum = float('-inf')

biggest_matrix = []

for row in range(rows - dimension +1):
    for col in range(cols - dimension +1):
        curr_sum = 0
        curr_matrix = []
        for d in range(dimension):
            row_to_take = row+d
            last_col = col+dimension
            line = matrix[row_to_take][col:last_col]
            curr_sum += sum(line)
            curr_matrix.append(line)
        if curr_sum > max_sum:
            max_sum = curr_sum
            biggest_matrix = [curr_matrix[i] for i in range(dimension)]

print(f"Sum = {max_sum}")
[print(*row) for row in biggest_matrix]
