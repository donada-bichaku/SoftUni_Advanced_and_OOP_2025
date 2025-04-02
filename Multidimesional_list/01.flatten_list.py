lines = input().split("|")

matrix = [[el for el in line.split()] for line in lines]

print(*[el for row in matrix[::-1] for el in row])

#solution 2
# lines = input().split("|")
#
# sub_lists = []
#
# for sub_string in sub_lists:
#     sub_lists.extend(sub_string.split())
#
# print(*sub_lists)




