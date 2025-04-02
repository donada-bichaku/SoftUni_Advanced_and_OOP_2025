# set1 = set(int(x) for x in input().split())
# set2 = set(int(x) for x in input().split())
#
# for _ in range(int(input())):
#     command, set_num, *nums = input().split()
#     if command == "Add":
#         if set_num == "First":
#             set1.update({int(el) for el in nums})
#         else:
#             set2.update({int(el) for el in nums})
#     elif command == "Remove":
#         if set_num == "First":
#             set1 = set1.difference({int(el) for el in nums})
#         else:
#             set2 = set2.difference({int(el) for el in nums})
#     else:
#         print(set1.issubset(set2) or set1.issuperset(set2))
#
# print(*sorted(set1), sep=", ")
# print(*sorted(set2), sep=", ")

# solution 2
set1 = set(int(x) for x in input().split())
set2 = set(int(x) for x in input().split())

for _ in range(int(input())):
    command, set_num, *nums = input().split()
    if command == "Add":
        if set_num == "First":
           [set1.add(int(el)) for el in nums]
        else:
            [set2.add(int(el)) for el in nums]
    elif command == "Remove":
        if set_num == "First":
            [set1.discard(int(el)) for el in nums]
        else:
            [set2.discard(int(el)) for el in nums]
    else:
        print(set1.issubset(set2) or set1.issuperset(set2))

print(*sorted(set1), sep=", ")
print(*sorted(set2), sep=", ")