guest_num = int(input())
invited = set()
showed_up = set()

for _ in range(guest_num):
    reservation_code = input()
    invited.add(reservation_code)

while True:
    came = input()
    if came == "END":
        break
    showed_up.add(came)

print(len(invited-showed_up))
print(f"{chr(10).join(sorted(invited - showed_up))}")
