from collections import deque

bee_queue = deque(int(el) for el in input().split())
honey_stack = [int(el) for el in input().split()]
honey_operator = deque(input().split())

honey_functions = {
    "+": lambda bee, honey: made_honey.append(bee + honey),
    "-": lambda bee, honey: made_honey.append(abs(bee - honey)),
    "*": lambda bee, honey: made_honey.append(bee * honey),
    "/": lambda bee, honey: made_honey.append(bee / honey) if honey != 0 else None,
}

made_honey = []

while bee_queue and honey_stack:
    curr_bee = bee_queue.popleft()
    curr_honey = honey_stack.pop()
    if curr_bee <= curr_honey:
        honey_functions[honey_operator.popleft()](curr_bee, curr_honey)
    else:
        bee_queue.appendleft(curr_bee)

print(f"Total honey made: {sum(made_honey)}")

if bee_queue:
    print(f"Bees left: {', '. join(str(bees) for bees in bee_queue)}")
if honey_stack:
    print(f"Nectar left: {', '. join(str(honey) for honey in honey_stack)}")

