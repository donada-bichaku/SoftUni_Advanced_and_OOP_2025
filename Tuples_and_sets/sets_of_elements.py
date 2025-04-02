# len1, len2 = map(int,(input().split()))
# set1 = set()
# set2 = set()
#
# for _ in range(len1):
#     el = input()
#     set1.add(el)
#
# for _ in range(len2):
#     el = input()
#     set2.add(el)
#
# print(*set1.intersection(set2), sep="\n")


#solution 2
len1, len2 = [int(x) for x in input().split()]

set1 = {input() for _ in range(len1)}
set2 = {input() for _ in range(len2)}

print(*set1.intersection(set2), sep="\n")