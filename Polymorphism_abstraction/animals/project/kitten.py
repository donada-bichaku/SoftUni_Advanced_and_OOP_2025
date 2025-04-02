from project.cat import Cat


class Kitten(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Female")

    @property
    def sound(self):
        return "Meow"