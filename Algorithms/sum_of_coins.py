def choose_coins(coins, target):
    coins.sort(reverse=True)
    idx = 0
    used_coins = {}

    while target > 0 and idx < len(coins):
        count_current_coins =  target // coins[idx]
        target = target % coins[idx]
        if count_current_coins > 0:
            used_coins[coins[idx]] = count_current_coins

        idx += 1

    if target != 0:
        result = "Error"
    else:
        result = f"Number of coins it took: {sum(used_coins.values())}\n"

        for coin, quantity in used_coins.items():
            result += f"{quantity} coins with value {coin}\n"
    return result


coins = [int(el) for el in input().split(", ")]
target = int(input())

print(choose_coins(coins, target))
