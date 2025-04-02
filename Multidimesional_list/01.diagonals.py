rows = int(input())

matrix = [[int(el) for el in input().split(", ")] for row in range(rows)]

primary_diagonal = []
secondary_diagonal = []

for row in range(rows):
    primary_diagonal.append(matrix[row][row])
    b = matrix[row][rows - row - 1]
    secondary_diagonal.append(b)

#another way
# primary_diagonal = [matrix[r][r] for r in range(rows)]
# secondary_diagonal = [matrix[r][rows-r-1] for r in range(rows)]

print("Primary diagonal:", ', '.join(str(el) for el in primary_diagonal) + ".",
      f"Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(el) for el in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
