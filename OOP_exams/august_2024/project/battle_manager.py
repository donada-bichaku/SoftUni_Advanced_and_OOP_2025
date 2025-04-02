from typing import List

from project.battleships.royal_battleship import RoyalBattleship
from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:
    def __init__(self):
        self.zones: List[BaseZone] = []
        self.ships: List[BaseBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str):
        if zone_type == "RoyalZone":
            self.check_code_exists(zone_code)
            zone = RoyalZone(zone_code)
        elif zone_type == "PirateZone":
            self.check_code_exists(zone_code)
            zone = PirateZone(zone_code)
        else:
            raise Exception("Invalid zone type!")

        self.zones.append(zone)
        return f"A zone of type {zone_type} was successfully added."

    def check_code_exists(self, zone_code):
        if len([zone for zone in self.zones if zone.code == zone_code]) > 0:
            raise Exception("Zone already exists!")


    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type == "RoyalBattleship":
            ship = RoyalBattleship(name, health, hit_strength)
        elif ship_type == 'PirateBattleship':
            ship = PirateBattleship(name, health, hit_strength)
        else:
            raise Exception(f"{ship_type} is an invalid type of ship!")

        self.ships.append(ship)
        return f"A new {ship_type} was successfully added."

    def add_ship_to_zone(self, zone: BaseZone, ship: BaseBattleship):
        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"

        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        if ship.__class__.__name__ == "RoyalBattleship":
            if zone.__class__.__name__ == "RoyalZone":
                ship.is_attacking = True
            else:
                ship.under_attack = True
        else:
            if zone.__class__.__name__ == "RoyalZone":
                ship.under_attack = True
            else:
                ship.is_attacking = True

        zone.ships.append(ship)
        zone.volume -= 1
        ship.is_available = False
        # self.ships.append(ship) # maybe add it to self.ships????
        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        try:
            ship = next(filter(lambda s: s.name == ship_name, self.ships))
        except StopIteration:
            return "No ship with this name!"

        if not ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(ship)
        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: BaseZone):
        ships_1 = [ship for ship in zone.ships if ship.under_attack]
        ships_2 = [ship for ship in zone.ships if ship.is_attacking]

        if len(ships_1) == 0 or len(ships_2) == 0:
            return "Not enough participants. The battle is canceled."

        attacking = sorted(ships_2, key=lambda ship: -ship.hit_strength)
        defending = sorted(ships_1, key=lambda ship: -ship.health)

        attacking[0].attack()
        defending[0].take_damage(attacking[0])

        if defending[0].health <= 0:
            self.ships.remove(defending[0])
            zone.ships.remove(defending[0])
            return f"{defending[0].name} lost the battle and was sunk."


        if attacking[0].ammunition <= 0:
            self.ships.remove(attacking[0])
            zone.ships.remove(attacking[0])
            return f"{attacking[0].name} ran out of ammunition and leaves."

        return "Both ships survived the battle."

    def get_statistics(self):
        available_ships = [s for s in self.ships if s.is_available]
        result = [f"Available Battleships: {len(available_ships)}"]

        if len(available_ships) > 0:
            result.append(f"#{', '.join(s.name for s in available_ships)}#")

        zones = sorted(self.zones, key=lambda z: z.code)
        result.extend(["***Zones Statistics:***", f"Total Zones: {len(zones)}"])
        if len(zones) > 0:
            for zone in zones:
                result.append(zone.zone_info())

        return "\n".join(result)












