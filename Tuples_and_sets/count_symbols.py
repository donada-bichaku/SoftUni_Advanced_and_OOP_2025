# frequency_of_char = {}
#
# for ch in input():
#     if ch in frequency_of_char:
#         frequency_of_char[ch] += 1
#         continue
#     frequency_of_char[ch] = 1
#
# for key in sorted(frequency_of_char):
#     print(f"{key}: {frequency_of_char[key]} time/s")

# solution 2
frequency_of_char = {}

for ch in input():
    frequency_of_char[ch] = frequency_of_char.get(ch, 0) + 1

print(*[f"{key}: {value} time/s" for key, value in sorted(frequency_of_char.items())], sep="\n")
