import math
from collections import deque
from math import floor

num_stack = deque()

for el in input().split():
    if el == "*":
        while len(num_stack) > 1:
            num_stack.appendleft(num_stack.popleft() * num_stack.popleft())

    elif el == "/":
        while len(num_stack) > 1:
            num_stack.appendleft(floor(num_stack.popleft() / num_stack.popleft()))

    elif el == "-":
        while len(num_stack) > 1:
            num_stack.appendleft(num_stack.popleft() - num_stack.popleft())

    elif el == "+":
        while len(num_stack) > 1:
            num_stack.appendleft(num_stack.popleft() + num_stack.popleft())

    else:
        num_stack.append(int(el))
        

print(*num_stack)
