# Input: sequence of numbers and target number
sequence = list(map(int, input().split()))
target = int(input())

# Initialize an empty set to track seen numbers
seen = set()

# Iterate through the sequence and find pairs
for number in sequence:
    complement = target - number
    if complement in seen:
        print(f"{complement} + {number} = {target}")
    seen.add(number)  # Add the current number to the set
