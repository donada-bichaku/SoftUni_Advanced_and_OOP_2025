from typing import List
from project.clients.base_client import BaseClient
from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.base_plant import BasePlant
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant


class FlowerShopManager:
    def __init__(self):
        self.income = 0.0
        self.plants: List[BasePlant] = []
        self.clients: List[BaseClient] = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        if plant_type == "Flower":
            plant = Flower(plant_name, plant_price, plant_water_needed, plant_extra_data)
        elif plant_type == "LeafPlant":
            plant = LeafPlant(plant_name, plant_price, plant_water_needed, plant_extra_data)
        else:
            raise ValueError("Unknown plant type!")

        self.plants.append(plant)

        return f"{plant.name} is added to the shop as {plant.__class__.__name__}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type == "RegularClient":
            self.duplicate_client_phone(client_phone_number)
            client = RegularClient(client_name, client_phone_number)
        elif client_type == "BusinessClient":
            self.duplicate_client_phone(client_phone_number)
            client = BusinessClient(client_name, client_phone_number)
        else:
            raise ValueError("Unknown client type!")

        self.clients.append(client)
        return f"{client.name} is successfully added as a {client.__class__.__name__}."


    def duplicate_client_phone(self, phone_number):

        for client in self.clients:
            if client.phone_number == phone_number:
                raise ValueError("This phone number has been used!")

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        client = next((c for c in self.clients if c.phone_number == client_phone_number), None)
        if client is None:
            raise ValueError("Client not found!")

        plants = [plant for plant in self.plants if plant.name == plant_name]
        if len(plants) == 0:
            raise ValueError("Plants not found!")

        if len(plants) < plant_quantity:
            return "Not enough plant quantity."

        plants_to_remove = plants[:plant_quantity]

        for plant in plants_to_remove:
            self.plants.remove(plant)

        income = sum(plant.price for plant in plants_to_remove) * (1 - client.discount/100)
        self.income += income

        client.update_total_orders()
        client.update_discount()

        return f"{plant_quantity}pcs. of {plant_name} plant sold for {income:.2f}"

    def remove_plant(self, plant_name:str):
        plant = next((p for p in self.plants if p.name == plant_name), None)
        if plant is None:
            return "No such plant name."

        self.plants.remove(plant)
        return f"Removed {plant.plant_details()}"

    def remove_clients(self):
        clients_to_remove = [client for client in self.clients if client.total_orders == 0]

        for client in clients_to_remove:
            self.clients.remove(client)

        return f"{len(clients_to_remove)} client/s removed."

    def shop_report(self):

        result = (["~Flower Shop Report~", f"Income: {self.income:.2f}",
                  f"Count of orders: {sum([c.total_orders for c in self.clients])}",
                  f"~~Unsold plants: {len(self.plants)}~~"])

        if self.display_unsold_flowers() != "":
            result.append(self.display_unsold_flowers())

        result.append(f"~~Clients number: {len(self.clients)}~~")

        if self.display_all_clients() != "":
            result.append(self.display_all_clients())



        return "\n".join(result)

    def display_unsold_flowers(self):
        result = ""
        plant_dict = {}

        for plant in self.plants:
            plant_dict[plant.name] = plant_dict.get(plant.name, 0) + 1

        sorted_plants = sorted(plant_dict.items(), key=lambda kvp: (-kvp[1], kvp[0]))
        for key, value in sorted_plants:
            result += f"{key}: {value}\n"

        return result.rstrip()

    def display_all_clients(self):
        result = ""
        sorted_clients = sorted(self.clients, key=lambda client: (-client.total_orders, client.phone_number))
        for client in sorted_clients:
            result += f"{client.client_details()}\n"

        return result.rstrip()









