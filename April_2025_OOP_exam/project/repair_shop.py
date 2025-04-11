from typing import List

from project.devices.base_device import BaseDevice


class RepairShop:
    def __init__(self, name: str, device_types: tuple):
        self.name = name
        self.device_types = device_types
        self.pending_devices: List[BaseDevice] = []
        self.repaired_devices: List[BaseDevice] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Invalid repair shop name!")
        self.__name = value

    @property
    def device_types(self):
        return self.__device_types

    @device_types.setter
    def device_types(self, value):
        if len(value) < 1:
            raise ValueError("No device types provided!")
        self.__device_types = value

    def repair(self):
        #TODO: is it guaranteed that all need to repaired? or if they are not malfunctioning they should not be counted?
        repaired_count = 0
        still_pending = []
        for device in self.pending_devices:
            device.repair()
            if device.is_functional:
                self.repaired_devices.append(device)
                repaired_count += 1
            else:
                still_pending.append(device)

        self.pending_devices = still_pending
        return f"Repaired {repaired_count} device/s."

    def status(self):
        return f"{self.name} has {len(self.pending_devices)} devices pending for repair and {len(self.repaired_devices)} devices repaired."

