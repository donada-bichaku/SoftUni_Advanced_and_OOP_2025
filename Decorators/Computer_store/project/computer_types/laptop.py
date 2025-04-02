from project.computer_types.computer import Computer


class Laptop(Computer):

    PROCESSORS = {"AMD Ryzen 9 5950X": 900,
                  "Intel Core i9-11900H": 1050,
                  "Apple M1 Pro": 1200,
                  }

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)


    def check_processor(self, processor: str):
        if processor not in self.PROCESSORS:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")

    def check_ram(self, ram: int):
        if not (ram <= 64 and self.is_power_of_two(ram)):
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

