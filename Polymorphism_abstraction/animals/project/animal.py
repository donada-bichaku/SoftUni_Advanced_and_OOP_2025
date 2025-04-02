from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def make_sound(self):
        return self.sound

    @property
    @abstractmethod
    def sound(self):
        pass

    def __repr__(self):
        return (f"This is {self.name}. "
                f"{self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}")