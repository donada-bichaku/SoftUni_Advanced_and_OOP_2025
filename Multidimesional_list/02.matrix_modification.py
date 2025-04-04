rows = int(input())
matrix = [[int(el) for el in input().split(" ")] for row in range(rows)]

OPERATIONS = {"Add": lambda x, y: x+y,
              "Subtract": lambda x, y: x-y,
              }

def check_valid_coordinates(row, col):
    return (0 <= row <= len(matrix) - 1 and 0 <= col <= len(matrix[0]))

while True:
     _input = input()

     if _input == "END":
         break

     command, row, col, value = _input.split()

     if not check_valid_coordinates(int(row), int(col)):
         print("Invalid coordinates")
         continue

     cell_to_modify = matrix[int(row)][int(col)]

     matrix[int(row)][int(col)] = OPERATIONS[command](cell_to_modify, int(value))

print("\n".join(" ".join(str(el) for el in row) for row in matrix))





