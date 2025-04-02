from collections import deque

green_duration = int(input())
free_window = int(input())

car_queue = deque()
successful_cars = 0
flag = True

while flag:
    text = input()
    if text == "END":
        break
    elif text == "green":
        current_green_duration = green_duration
#        current_free_window =
        while current_green_duration > 0 and car_queue:
            current_car = car_queue.popleft()
            if len(current_car) <= current_green_duration:
                current_green_duration -= len(current_car)
                successful_cars += 1
            else:
                current_green_duration -= len(current_car)
                left = current_car[current_green_duration:]
                if len(left) > free_window:
                    print(f"A crash happened! \n{current_car} was hit at {left[free_window]}.")
                    flag = False
                    break
                else:
                    successful_cars += 1
    else:
        car_queue.append(text)

if flag == True:
    print(f"Everyone is safe. \n{successful_cars} total cars passed the crossroads.")
