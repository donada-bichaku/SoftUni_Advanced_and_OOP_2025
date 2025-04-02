from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.guests = 0
        self.rooms: List[Room] = []


    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        try:
            room = next(filter(lambda x: x.number == room_number, self.rooms))
        except StopIteration:
            pass

        result = room.take_room(people)
        if not result:
            self.guests += people

        # return result -> if we wanted to return the result that room can't be taken if people exceed capacity


    def free_room(self, room_number):
        try:
            room = next(filter(lambda x: x.number == room_number, self.rooms))
            people = room.guests
        except StopIteration:
            pass

        result = room.free_room()
        if not result:
            self.guests -= people

        # return result -> if we wanted to return the result


    def status(self):
        result = f"Hotel {self.name} has {self.guests} total guests\n"
        result += f"Free rooms: {', '.join(str(room.number) for room in self.rooms if not room.is_taken)}"
        result += f"\nTaken rooms: {', '.join(str(room.number) for room in self.rooms if room.is_taken)}"

        return result
