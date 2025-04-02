from typing import List, Type

from project.animals.animal import Bird
from project.food import Food, Meat, Seed, Fruit, Vegetable


class Owl(Bird):

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self) -> float:
        return 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):

    @property
    def food_that_eats(self):
        return [Meat, Vegetable, Fruit, Seed]

    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def gained_weight(self) -> float:
        return 0.35