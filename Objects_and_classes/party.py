class Party:
    def __init__(self):
        self.people = []


party = Party()

while True:
    user_input = input()
    if user_input == "End":
        break
    party.people.append(user_input)

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
