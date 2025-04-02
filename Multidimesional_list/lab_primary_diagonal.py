# rows = int(input())
#
# matrix = [[int(el) for el in input().split()] for _ in range(rows)]
# sum_diagonal = 0
#
# for row in range(rows):
#     sum_diagonal += matrix[row][row]
#
# print(sum_diagonal)

# solution 2
# rows = int(input())
#
# matrix = [[int(el) for el in input().split()] for _ in range(rows)]
#
# print(sum(matrix[row][row] for row in range(rows)))

# NOT A SOLUTION - the secondary diagonal
rows = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(rows)]
sum_col = 0

print(sum(matrix[row][-1-row] for row in range(rows)))



