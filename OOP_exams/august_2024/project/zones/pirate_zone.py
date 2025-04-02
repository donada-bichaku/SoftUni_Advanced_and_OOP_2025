from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    INIT_VOL = 8
    def __init__(self, code: str):
        super().__init__(code, self.INIT_VOL)


    def zone_info(self):
        result = ["@Pirate Zone Statistics@", f"Code: {self.code}; Volume: {self.volume}",
                  f"Battleships currently in the Pirate Zone: {len(self.ships)}, "
                  f"{len([ship for ship in self.ships if isinstance(ship, RoyalBattleship)])} out of them are Royal Battleships."]
        if len(self.ships) > 0:
            result.append(f'#{", ".join(ship.name for ship in self.get_ships())}#')

        return "\n".join(result)

