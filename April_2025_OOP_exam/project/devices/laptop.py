from project.devices.base_device import BaseDevice


class Laptop(BaseDevice):
    def repair(self):
        # TODO: do we need to check on is_func == false?
        if not self.is_functional:
            new_durability = self.durability + 50
            if new_durability > 100:
                new_durability = 100
            self.durability = new_durability
            self.is_functional = True


    def __init__(self, serial_number: str, durability: int, is_functional: bool):
        super().__init__(serial_number, durability, is_functional, "Laptop")

