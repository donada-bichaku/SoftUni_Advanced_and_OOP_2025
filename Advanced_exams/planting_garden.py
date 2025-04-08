def plant_garden(space, *args, **kwargs):
    garden_plants = args
    planted = {}
    allowed_plants = [el[0] for el in garden_plants]
    requested = dict(sorted(kwargs.items(), key=lambda x: x[0]))
    for plant, amount in requested.items():
        if space == 0:
            break

        if plant in allowed_plants:
            needed_space = next(filter(lambda x: x[0] == plant, garden_plants))
            can_plant = int(space // needed_space[1])
            quantity_planted = min(amount, can_plant)

            if quantity_planted > 0:
                space -= quantity_planted * needed_space[1]
                planted[plant] = quantity_planted

    partial_plant = False
    for plant, amount in requested.items():
        if plant in allowed_plants:
            if planted.get(plant, 0) < amount:
                partial_plant = True
                break

    if partial_plant:
        result = "Not enough space to plant all requested plants!\n"
    else:
        result = f"All plants were planted! Available garden space: {space:.1f} sq meters.\n"
    result += f"Planted plants:\n"
    for plant in sorted(planted):
        result += f"{plant}: {planted[plant]}\n"

    return result.strip()





# print(plant_garden(49.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
