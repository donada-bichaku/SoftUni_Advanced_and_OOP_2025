
from project.computer_types.computer import Computer


class DesktopComputer(Computer):

    PROCESSORS = {"AMD Ryzen 7 5700G": 500, "Intel Core i5-12600K": 600, "Apple M1 Max": 1800}

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)


    def check_processor(self, processor: str):
        if processor not in self.PROCESSORS:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")


    def check_ram(self, ram: int):
        if not (ram <= 128 and self.is_power_of_two(ram)):
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")


