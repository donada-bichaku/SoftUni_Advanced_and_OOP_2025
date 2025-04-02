rows = int(input())

matrix = [[el for el in input()] for row in range(rows)]
find = input()


for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == find:
            print(f"({row}, {col})")
            exit()
else:
    print(f"{find} does not occur in the matrix")


