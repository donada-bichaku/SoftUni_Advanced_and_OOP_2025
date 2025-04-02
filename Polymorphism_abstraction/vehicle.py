from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self.consumption_inc)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    @abstractmethod
    def refuel(self, fuel: float):
        pass

    @property
    @abstractmethod
    def consumption_inc(self):
        pass

class Car(Vehicle):

    @property
    def consumption_inc(self):
        return 0.9

    def refuel(self, liters):
        self.fuel_quantity += liters

class Truck(Vehicle):
    TANK_PERC_FILL = 0.95

    @property
    def consumption_inc(self):
        return 1.6

    def refuel(self, liters):
        self.fuel_quantity += liters * self.TANK_PERC_FILL


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

