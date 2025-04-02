# solution 1
# rows, columns = [int(el) for el in input().split(", ")]
#
# matrix = [[int(el) for el in input().split()] for _ in range(rows)]
#
# for col in range(columns):
#     sum = 0
#     for row in range(rows):
#         sum += matrix[row][col]
#     print(sum)

# solution 2 - flatten then take with step x for sum
# rows, columns = [int(el) for el in input().split(", ")]
#
# matrix = [[int(el) for el in input().split()] for _ in range(rows)]
#
# flatten_matrix = [el for row in range(rows) for el in matrix[row]]
#
# for col in range(columns):
#     print(sum(flatten_matrix[col::6]))

# NOT A SOLUTION - rotate matrix
# rows, columns = [int(el) for el in input().split(", ")]
#
# matrix = [[int(el) for el in input().split()] for _ in range(rows)]
#
# rotated_matrix = []
#
# flatten_matrix = [el for row in range(rows) for el in matrix[row]]
#
# for col in range(columns):
#     rotated_matrix.append(flatten_matrix[col::6])
#
# print(rotated_matrix)

# NOT A SOLuTION - rotate matrix
rows, columns = [int(el) for el in input().split(", ")]

matrix = [[int(el) for el in input().split()] for _ in range(rows)]
rotated_matrix = []

for col in range(columns):
    rotated_matrix.append([])
    for row in range(rows):
        rotated_matrix[col].append(matrix[row][col])

print(rotated_matrix)
