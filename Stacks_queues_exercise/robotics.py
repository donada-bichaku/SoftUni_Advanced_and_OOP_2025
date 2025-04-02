from datetime import datetime, timedelta
from collections import deque

robots_dump = input()
robots = {}

for robot in robots_dump.split(";"):
    name, time_needed = robot.split("-")
    robots[name] = [int(time_needed), 0]

factory_time = datetime.strptime(input(), '%H:%M:%S')

products = deque()

while True:
    product = input()

    if product == "End":
        break

    products.append(product)

while products:
    factory_time += timedelta(seconds=1)

    product = products.popleft()

    free_robots = []
    for name, robot_info in robots.items():
        if robot_info[1] > 1:
            robot_info[1] -= 1
        else:
            robot_info[1] -= 1
            free_robots.append(name)

    if not free_robots:
        products.append(product)
        continue

    robot_name = free_robots[0]
    robots[robot_name][1] = robots[robot_name][0]
    print(f"{robot_name} - {product} [{factory_time.time()}]")




