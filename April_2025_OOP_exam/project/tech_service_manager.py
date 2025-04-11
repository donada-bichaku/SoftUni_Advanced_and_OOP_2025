from typing import List

from project.devices.base_device import BaseDevice
from project.devices.laptop import Laptop
from project.devices.smartphone import Smartphone
from project.devices.smartwatch import Smartwatch
from project.repair_shop import RepairShop


class TechServiceManager:

    VALID_DEVICES = {"Laptop": Laptop, "Smartphone": Smartphone, "Smartwatch": Smartwatch}

    def __init__(self):
        self.devices: List[BaseDevice] = []
        self.repair_shops: List[RepairShop] = []

    def add_device(self, device_type: str, serial_number: str, durability: int, is_functional: bool):
        if device_type not in self.VALID_DEVICES.keys():
            raise ValueError("Invalid device type!")
        device = self.VALID_DEVICES[device_type](serial_number, durability, is_functional)

        device.check_functionality()
        self.devices.append(device)

        return f"{device_type} is successfully added."

    def add_repair_shop(self, name: str, device_types: tuple):
        if not any(device_type in self.VALID_DEVICES for device_type in device_types):
            raise ValueError("No valid device type!")

        shop = RepairShop(name, device_types)
        self.repair_shops.append(shop)
        return f"{name} is successfully added as a repair shop."

    def send_for_repair(self, repair_shop_name: str, device_type: str):
        shop = next(filter(lambda s: s.name == repair_shop_name, self.repair_shops))
        if device_type not in shop.device_types:
            return "The shop cannot repair this device type."

        devices = [device for device in self.devices if device.device_type == device_type and device.is_functional == False]
        if len(devices) == 0:
            return f"There is no {device_type} that needs repair."
        device = devices[0]
        self.devices.remove(device)
        shop.pending_devices.append(device)
        return f"{device.serial_number} was sent for repair to {repair_shop_name}."

    def process_repairs(self, repair_shop: RepairShop):
        result = repair_shop.repair()
        return result

    def receive_repaired_devices(self, repair_shop: RepairShop):
        count = 0
        for device in repair_shop.repaired_devices:
            self.devices.append(device)
            count += 1

        repair_shop.repaired_devices = []

        return f"Received {count} repaired devices."

    def tech_service_status(self):
        functional_dev = [device for device in self.devices if device.is_functional]
        malfunctioning = [device for device in self.devices if not device.is_functional]
        result = "***Tech Service***\n"
        result += f"Total number of functional devices: {len(functional_dev)}\n"
        result += f"Total number of malfunctioning devices: {len(malfunctioning)}\n"
        result += f"Repair shops count: {len(self.repair_shops)}\n"

        if self.repair_shops:
            sorted_shops = sorted(self.repair_shops, key=lambda shop: shop.name)
            result += "\n".join(f"@{shop.status()}" for shop in sorted_shops)

        return result.strip()






