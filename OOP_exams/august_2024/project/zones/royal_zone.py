from project.battleships.pirate_battleship import PirateBattleship
from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):

    INIT_VOL = 10
    def __init__(self, code: str):
        super().__init__(code, self.INIT_VOL)

    def zone_info(self):
        result = ["@Royal Zone Statistics@", f"Code: {self.code}; Volume: {self.volume}",
                  f"Battleships currently in the Royal Zone: {len(self.ships)}, "
                  f"{len([ship for ship in self.ships if isinstance(ship, PirateBattleship)])} out of them are Pirate Battleships."]
        if len(self.ships) > 0:
            result.append(f'#{", ".join(ship.name for ship in self.get_ships())}#')

        return "\n".join(result)




