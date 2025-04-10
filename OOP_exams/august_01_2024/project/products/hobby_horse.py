from project.products.base_product import BaseProduct


class HobbyHorse(BaseProduct):
    def discount(self):
        self.price *= 0.8

    def __init__(self, model: str, price: float):
        super().__init__(model, price, 'Wood/Plastic', 'Toys')
