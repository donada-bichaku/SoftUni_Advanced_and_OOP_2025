from typing import List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer) -> None:
        if self.customer_capacity() > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if self.dvd_capacity() > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd = next(filter(lambda x: x.id == dvd_id, self.dvds))
        customer = next(filter(lambda x: x.id == customer_id, self.customers))

        if dvd.is_rented:
            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"


    def return_dvd(self, customer_id: int, dvd_id: int):
        dvd = next(filter(lambda x: x.id == dvd_id, self.dvds))
        customer = next(filter(lambda x: x.id == customer_id, self.customers))
        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"
        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        # result = []
        # for customer in self.customers:
        #     result.append(str(customer))
        # for dvd in self.dvds:
        #     result.append(str(dvd))

        return "\n".join([*[str(el) for el in self.customers], *[str(el) for el in self.dvds]])

