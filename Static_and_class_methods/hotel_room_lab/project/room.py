class Room:
    def __init__(self, number: int, capacity: int):
        self.guests = 0
        self.is_taken = False
        self.number = number
        self.capacity = capacity

    def take_room(self, people: int):
        if self.is_taken or self.capacity < people:
            return f"Room number {self.number} cannot be taken"
        self.is_taken = True
        self.guests += people

    def free_room(self):
        if not self.is_taken:
            return f"Room number {self.number} is not taken"

        self.is_taken = False
        self.guests = 0

