longest_intersection = set()

for _ in range(int(input())):
    first, second = input().split("-")
    start1, end1 = map(int, (first.split(",")))
    set1 = set(range(start1, end1 + 1))
    start2, end2 = map(int,(second.split(",")))
    set2 = set(range(start2, end2 + 1))
    intersection = set1.intersection(set2)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")

# solution 2
# longest_intersection = set()
#
# for _ in range(int(input())):
#     first, second = [el.split(",") for el in input().split("-")]
#
#     set1 = set(range(int(first[0]), int(first[1]) + 1))
#     set2 = set(range(int(second[0]), int(second[1]) + 1))
#
#     intersection = set1.intersection(set2)
#
#     if len(intersection) > len(longest_intersection):
#         longest_intersection = intersection
#
# print(f"Longest intersection is "
#       f"{list(longest_intersection)} "
#       f"with length {len(longest_intersection)}")
