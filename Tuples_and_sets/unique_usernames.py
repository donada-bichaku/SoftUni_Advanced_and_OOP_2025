# num_inputs = int(input())
# usernames = set()
#
# for _ in range(num_inputs):
#     usernames.add(input())
#
# print(*usernames, sep="\n")

# solution 2
print(*{input() for _ in range(int(input()))}, sep="\n")