from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

presents = {
    "Doll": {"needed": 150, },
    "Wooden train": {"needed": 250, },
    "Teddy bear": {"needed": 300, },
    "Bicycle": {"needed": 400, },
}

while materials and magic:
    curr_material = materials.pop() if magic[0] or not materials[-1] else 0 # 3
    curr_magic = magic.popleft() if curr_material or not magic[0] else 0 # 0

    if not curr_magic: # if
        continue

    magic_level = curr_material * curr_magic
    if magic_level < 0:
        materials.append(curr_material + curr_magic)
    else:
        found_match = False
        for toy, attributes in presents.items():
            if attributes["needed"] == magic_level:
                attributes["created"] = attributes.get("created", 0) + 1
                found_match = True
        if not found_match:
            materials.append(curr_material + 15)

if (presents["Doll"].get("created", 0) > 0 and presents["Wooden train"].get("created", 0) > 0) \
        or (presents["Teddy bear"].get("created", 0) > 0 and presents["Bicycle"].get("created", 0) > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")

if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for toy, attributes in sorted(presents.items()):
    if attributes.get("created", 0) > 0:
        print(f"{toy}: {attributes.get('created')}")
                



