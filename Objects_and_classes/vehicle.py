class Vehicle:

    """
    This class creates vehicles
    """

    def __init__(self, mileage):
        self.mileage = int(input())


v1 = Vehicle(0)
print(v1.mileage)
