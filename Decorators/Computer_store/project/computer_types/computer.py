import math
from abc import ABC, abstractmethod


class Computer(ABC):

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor: str = None
        self.ram: int = None
        self.price: int = 0


    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model name cannot be empty.")
        self.__model = value


    def configure_computer(self, processor: str, ram: int):

        self.check_processor(processor)
        self.check_ram(ram)

        self.processor = processor
        self.ram = ram

        self.price = (int(math.log2(ram)) * 100) + self.PROCESSORS[processor]

        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."

    @staticmethod
    def is_power_of_two(n):
        return n > 0 and (n & (n - 1)) == 0

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"

    @abstractmethod
    def check_processor(self, processor: str):
        pass

    @abstractmethod
    def check_ram(self, ram: int):
        pass

