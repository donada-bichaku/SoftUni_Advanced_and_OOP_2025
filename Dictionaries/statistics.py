shop_statistics = {}

while True:
    stat = input().split(": ")

    if len(stat) == 1:
        break

    key, val = stat
    if key in shop_statistics:
        shop_statistics[key] += int(val)
    else:
        shop_statistics[key] = int(val)

print(f"Products in stock:")
for key, val in shop_statistics.items():
    print(f"- {key}: {val}")

print(f"Total Products: {len(shop_statistics)}"
      f"\nTotal Quantity: {sum(shop_statistics.values())}")