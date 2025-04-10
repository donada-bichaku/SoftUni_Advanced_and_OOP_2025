from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    @property
    def store_type(self):
        return "FurnitureStore"

    def store_stats(self):
        result = f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
        result += self.get_estimated_profit() + "\n"
        result += "**Furniture for sale:\n"
        furniture_for_sale = {}
        for product in self.products:
            furniture_for_sale.setdefault(product.model, []).append(product.price)
        sorted_furniture = sorted(furniture_for_sale.items(), key=lambda x: x[0])
        if sorted_furniture:
            result += "\n".join(f"{model}: {len(prices)}pcs, average price: {sum(prices) / len(prices):.2f}" for model, prices in sorted_furniture)

        return result.strip()

    def __init__(self, name: str, location: str):
        super().__init__(name, location, 50)


