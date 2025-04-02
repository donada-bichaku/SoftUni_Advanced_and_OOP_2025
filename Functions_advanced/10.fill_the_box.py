from collections import deque


def fill_the_box(height, length, width, *args):
    finish = args.index("Finish")
    cubes = deque(args[:finish])
    box_space = height * length * width
    while cubes.copy():
        curr_cube = cubes.popleft()
        if curr_cube <= box_space:
            box_space -= curr_cube
        else:
            cubes.appendleft(curr_cube - box_space)
            return f"No more free space! You have {sum(cubes)} more cubes."
    return f"There is free space in the box. You could put {box_space} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(2, 2, 2, 40, "Finish", 2, 15, 30))

