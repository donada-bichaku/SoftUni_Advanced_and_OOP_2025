from collections import deque

tank_gas = 0
trip = 0

pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])
pumps_data_copy = pumps_data.copy()

while pumps_data_copy:
    petrol, distance = pumps_data_copy.popleft()
    tank_gas += petrol
    if tank_gas >= distance:
        tank_gas -= distance
    else:
        trip += 1
        tank_gas = 0
        pumps_data.rotate(-1)
        pumps_data_copy = pumps_data.copy()

print(trip)