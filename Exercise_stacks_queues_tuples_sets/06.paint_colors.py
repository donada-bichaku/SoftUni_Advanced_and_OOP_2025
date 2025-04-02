from collections import deque

string_to_match = deque(input().split())

colors = {"red", "yellow", "blue", "orange", "purple", "green"}

result = []

secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

while string_to_match:
    first = string_to_match.popleft()
    last = string_to_match.pop() if string_to_match else ''

    for color in (first + last, last + first):
        if color in colors:
            result.append(color)
            break
    else:
        for el in (first[:-1], last[:-1]):
            if el:
                string_to_match.insert(len(string_to_match)//2, el)

for color in set(secondary_colors.keys()).intersection(result):
    if not secondary_colors[color].issubset(result):
        result.remove(color)

print(result)





