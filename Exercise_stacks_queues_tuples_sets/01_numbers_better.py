set1 = set(int(x) for x in input().split())
set2 = set(int(x) for x in input().split())

commands = {
    "Add First": lambda x: [set1.add(int(el)) for el in x],
    "Add Second": lambda x: [set2.add(int(el)) for el in x],
    "Remove First": lambda x: [set1.discard(int(el)) for el in x],
    "Remove Second": lambda x: [set2.discard(int(el)) for el in x],
    "Check Subset": lambda x: print(set1.issubset(set2) or set1.issuperset(set2)),
}


for _ in range(int(input())):
    action, set_num, *nums = input().split()
    command = action + " " + set_num
    commands[command](nums)

print(*sorted(set1), sep=", ")
print(*sorted(set2), sep=", ")