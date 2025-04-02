rows = int(input())

matrix = [[int(el) for el in input().split()] for row in range(rows)]

primary_diagonal = []
secondary_diagonal = []

for row in range(rows):
    primary_diagonal.append(matrix[row][row])
    b = matrix[row][rows - row - 1]
    secondary_diagonal.append(b)

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))

#solution 2
# rows = int(input())
#
# matrix = [[int(el) for el in input().split()] for row in range(rows)]
#
# primary_sum, secondary_sum = 0, 0
#
# for row in range(rows):
#     primary_sum += matrix[row][row]
#     secondary_sum += matrix[row][rows - row - 1]
#
# print(abs(primary_diagonal - secondary_diagonal))


#solution 3
# rows = int(input())
# primary_sum, secondary_sum = 0, 0
#
# for row in range(rows):
#     line = [int(el) for input().split()]
#     primary_sum += line[row]
#     secondary_sum += line[rows - row - 1]
#
# print(abs(primary_diagonal - secondary_diagonal))

