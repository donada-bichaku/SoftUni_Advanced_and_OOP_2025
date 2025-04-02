from project.battleships.base_battleship import BaseBattleship


class PirateBattleship(BaseBattleship):
    INIT_AMMUNITION = 80

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, self.INIT_AMMUNITION)

    def attack(self):
        self.ammunition -= 10
        if self.ammunition < 0:
            self.ammunition = 0
