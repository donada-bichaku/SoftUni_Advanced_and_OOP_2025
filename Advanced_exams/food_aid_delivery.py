from collections import deque

food_weight = list(map(int, input().split()))
food_req = deque(map(int, input().split()))
target = int(input())
fulfilled_req = 0

while food_weight and food_req:
    curr_pack = food_weight.pop()
    curr_req = food_req.popleft()
    if curr_pack == curr_req:
        fulfilled_req +=1
    elif curr_pack > curr_req:
        leftover = curr_pack -  curr_req - 1
        if leftover > 0 and len(food_weight) > 0:
            food_weight[-1] += leftover
        elif leftover > 0 and len(food_weight) == 0:
            food_weight.append(leftover)
        fulfilled_req += 1
    elif curr_pack < curr_req:
        leftover_req = curr_req - curr_pack
        food_req.append(leftover_req)

if fulfilled_req >= target:
    print(f"Food relief success! Daniel helped {fulfilled_req} charity points.")
elif fulfilled_req < target and fulfilled_req > 0:
    print(f"Daniel made a difference! He helped {fulfilled_req} charity points.")
elif fulfilled_req == 0:
    print("Daniel could not help much this time. He will try again next week.")

if food_weight:
    print(f"Remaining food packages: " + "; ".join(str(el) for el in food_weight[::-1]))
if food_req:
    print(f"Unmet food requests: " + "; ".join(str(el) for el in food_req))
