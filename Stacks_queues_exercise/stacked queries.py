stack = []

for i in range(int(input())):
    command = [int(x) for x in input().split()]
    if len(command) > 1:
        _, element = command
        stack.append(element)
    elif command[0] == 2:
        if stack:
            stack.pop()
    elif command[0] == 3:
        if stack:
            print(max(stack))
    elif command[0] == 4:
        if stack:
            print(min(stack))

# print(*stack[::-1], sep=", ")

stack.reverse()
print(*stack, sep=", ")