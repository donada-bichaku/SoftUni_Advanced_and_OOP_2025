def set_cover(universe, sets):
    chosen_sets = []

    while universe:
        best_set = max(sets, key=lambda s: len(universe.intersection(s))) # assumption is that universe contains all elements, all sets are subsets of the universe
        chosen_sets.append(best_set)
        universe -= best_set

    return chosen_sets


universe = set(int(el) for el in input().split(", "))
num_sets = int(input())
sets = [{int(x) for x in input().split(", ")} for _ in range(num_sets)]


result = set_cover(universe, sets)

for i in range(len(result)):
    result[i] = sorted(result[i])

print(f"Sets to take ({len(result)}):")

[print("{ " + f"{', '.join(str(x) for x in s)}" + " }") for s in result]