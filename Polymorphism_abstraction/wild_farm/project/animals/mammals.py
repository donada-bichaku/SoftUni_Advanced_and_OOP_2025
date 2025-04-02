from typing import Type, List

from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit, Seed


class Mouse(Mammal):
    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit]

    @property
    def gained_weight(self) -> float:
        return 0.10

class Cat(Mammal):
    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def food_that_eats(self):
        return [Meat, Vegetable]

    @property
    def gained_weight(self) -> float:
        return 0.30

class Dog(Mammal):
    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self) -> float:
        return 0.40

class Tiger(Mammal):
    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self) -> float:
        return 1.00