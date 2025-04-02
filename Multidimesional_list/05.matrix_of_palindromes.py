ch_ascii = 97
rows, cols = [int(el) for el in input().split()]

start = ord('a')

for row in range(start, start+rows):
    for col in range(row, row+cols):
        print(chr(row), chr(col), chr(row), sep="", end=" ")

    print()


# print(chr(start_ascii), rows, cols)

# matrix = [
#     ["aaa", "aba"],
#     ["bbb", "bcb"]
# ]
# print(matrix[0][1][1])