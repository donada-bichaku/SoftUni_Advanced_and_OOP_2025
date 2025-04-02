stack = []

map_functions = {
    1: lambda x: stack.append(x[1]),
    2: lambda x: stack.pop() if stack else None,
    3: lambda x: print(max(stack)) if stack else None,
    4: lambda x: print(min(stack)) if stack else None,
}

for i in range(int(input())):
    numbers_data = [int(x) for x in input().split()]
    command = numbers_data[0]
    map_functions[command](numbers_data)


# print(*stack[::-1], sep=", ")
# print(*[stack.pop() for num in stack])
stack.reverse()
print(*stack, sep=", ")