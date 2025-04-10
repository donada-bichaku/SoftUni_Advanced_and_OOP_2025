from project.stores.base_store import BaseStore


class ToyStore(BaseStore):
    @property
    def store_type(self):
        return "ToyStore"

    def store_stats(self):
        result = f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
        result += self.get_estimated_profit() + "\n"
        result += "**Toys for sale:\n"
        toys_for_sale = {}
        for product in self.products:
            toys_for_sale.setdefault(product.model, []).append(product.price)
        sorted_toys = sorted(toys_for_sale.items(), key=lambda x: x[0])
        if sorted_toys:
            result += "\n".join(f"{model}: {len(prices)}pcs, average price: {sum(prices)/len(prices):.2f}" for model, prices in sorted_toys)

        return result.strip()

    def __init__(self, name: str, location: str):
        super().__init__(name, location, 100)


