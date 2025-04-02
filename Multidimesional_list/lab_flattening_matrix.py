# solution 1
# row = int(input())
            # matrix = []
            # for _ in range(row):
            #     matrix.append([int(el) for el in input().split(", ")])
            #
            # print(matrix)
            #
            # flattened_matrix = [el for row in matrix for el in row]

# flattened_matrix = [int(el) for _ in range(row) for el in input().split(", ")]
#
# print(flattened_matrix)

# solution 2
row = int(input())
flattened_matrix = []

for _ in range(row):
    row_data = [int(el) for el in input().split(", ")]
    flattened_matrix.extend(row_data)

print(flattened_matrix)


