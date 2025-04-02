from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:

    VALID_COMPUTERS = {
        "Desktop Computer": DesktopComputer,
        "Laptop": Laptop
    }

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.VALID_COMPUTERS:
            raise ValueError(f"{ type_computer } is not a valid type computer!")

        comp = self.VALID_COMPUTERS[type_computer](manufacturer, model)
        result = comp.configure_computer(processor, ram)

        self.warehouse.append(comp)
        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):

        options = [c for c in self.warehouse if c.processor == wanted_processor and c.ram >= wanted_ram and c.price <= client_budget]

        if not options:
            raise Exception("Sorry, we don't have a computer for you.")

        computer = options[0]
        profit = client_budget - computer.price
        self.profits += profit

        self.warehouse.remove(computer)

        return f"{computer} sold for {client_budget}$."

