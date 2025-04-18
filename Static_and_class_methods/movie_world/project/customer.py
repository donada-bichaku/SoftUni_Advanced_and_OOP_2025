from typing import List
from project.dvd import DVD


class Customer:
    def __init__(self, name: str, age: int, _id: int):
        self.name = name
        self.age = age
        self.id = _id
        self.rented_dvds: List[DVD] = []

    def __repr__(self):
        return (f"{self.id}: {self.name} of age {self.age} has "
                f"{len(self.rented_dvds)} rented DVD's ({' '.join(dvd.name for dvd in self.rented_dvds)})")
