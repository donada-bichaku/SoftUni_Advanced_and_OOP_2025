from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    def __init__(self, name: str):
        self.name = name
        self.income = 0.0
        self.products = []
        self.stores = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type == "Chair":
            product = Chair(model, price)
        elif product_type == "HobbyHorse":
            product = HobbyHorse(model, price)
        else:
            raise Exception("Invalid product type!")

        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in ('FurnitureStore', 'ToyStore'):
            raise Exception(f"{store_type} is an invalid type of store!")
        if store_type == "FurnitureStore":
            store = FurnitureStore(name, location)
        elif store_type == 'ToyStore':
            store = ToyStore(name, location)

        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        if store.store_type == "FurnitureStore":
            products = [p for p in products if p.sub_type == 'Furniture']
        elif store.store_type == "ToyStore":
            products = [p for p in products if p.sub_type == 'Toys']

        if not products:
            return "Products do not match in type. Nothing sold."

        store.products.extend(products)
        for p in products:
            self.products.remove(p)
            self.income += p.price
        store.capacity -= len(products)

        return f"Store {store.name} successfully purchased {len(products)} items."

    def unregister_store(self, store_name: str):
        try:
            store = next(filter(lambda s: s.name==store_name, self.stores))
        except StopIteration:
            raise Exception("No such store!")

        if len(store.products) > 0:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."

    def discount_products(self, product_model: str):
        products = [product for product in self.products if product.model == product_model]
        for p in products:
            p.discount()

        return f"Discount applied to {len(products)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        try:
            store = next(filter(lambda x: x.name == store_name, self.stores))
        except StopIteration:
            return "There is no store registered under this name!"

        return store.store_stats()

    def statistics(self):
        result = f"Factory: {self.name}\n" + f"Income: {self.income:.2f}\n" + "***Products Statistics***\n" + f"Unsold Products: {len(self.products)}. Total net price: {sum([p.price for p in self.products]):.2f}\n"

        unsold = {}
        for product in self.products:
            unsold[product.model] = unsold.get(product.model, 0) + 1
        sorted_unsold = sorted(unsold.items(), key=lambda x: x[0])
        result += "\n".join(f"{p}: {q}" for p, q in sorted_unsold)

        result += f"\n***Partner Stores: {len(self.stores)}***\n"
        store_names = sorted([s.name for s in self.stores])
        result += "\n".join(store_names)

        return result.strip()






