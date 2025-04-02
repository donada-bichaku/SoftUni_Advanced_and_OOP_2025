#from collections import deque
from collections import deque

# numbers = deque(input().split())
#
# while numbers:
#     print(numbers.pop(), end=" ")


numbers = deque(input().split())

numbers.reverse()
# print(' '.join(numbers))
print(*numbers)