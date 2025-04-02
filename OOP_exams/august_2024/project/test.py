# Initialize the BattleManager
from project.battle_manager import BattleManager

battle_manager = BattleManager()

# Add zones
print(battle_manager.add_zone("RoyalZone", "001"))
print(battle_manager.add_zone("PirateZone", "002"))
print()

# Add battleships
print(battle_manager.add_battleship("RoyalBattleship", "RoyalOne", 50, 50))
print(battle_manager.add_battleship("RoyalBattleship", "RoyalTwo", 0, 45))
print(battle_manager.add_battleship("PirateBattleship", "PirateOne", 50, 50))
print(battle_manager.add_battleship("PirateBattleship", "PirateTwo", 70, 60))
print(battle_manager.add_battleship("RoyalBattleship", "RoyalThree", 100, 100))
print(battle_manager.add_battleship("PirateBattleship", "PirateFour", 90, 90))
print(battle_manager.add_battleship("PirateBattleship", "PirateFive", 90, 90))
print(battle_manager.add_battleship("PirateBattleship", "PirateSix", 90, 90))
print(battle_manager.add_battleship("PirateBattleship", "PirateSeven", 90, 90))
print(battle_manager.add_battleship("PirateBattleship", "PirateEight", 90, 90))
print(battle_manager.add_battleship("PirateBattleship", "PirateNine", 90, 90))
print()

# Retrieve battleships and zones
royal_zone = battle_manager.zones[0]
pirate_zone = battle_manager.zones[1]

royal_one = battle_manager.ships[0]
royal_two = battle_manager.ships[1]
pirate_one = battle_manager.ships[2]
pirate_two = battle_manager.ships[3]

# Add ships to zones
print(battle_manager.add_ship_to_zone(royal_zone, royal_one))
print(battle_manager.add_ship_to_zone(royal_zone, pirate_one))
print(battle_manager.add_ship_to_zone(pirate_zone, pirate_one))
print(battle_manager.add_ship_to_zone(pirate_zone, royal_two))
print(battle_manager.add_ship_to_zone(pirate_zone, battle_manager.ships[3]))
print(battle_manager.add_ship_to_zone(pirate_zone, battle_manager.ships[4]))
print(battle_manager.add_ship_to_zone(pirate_zone, battle_manager.ships[5]))
print(battle_manager.add_ship_to_zone(pirate_zone, battle_manager.ships[6]))
print(battle_manager.add_ship_to_zone(pirate_zone, battle_manager.ships[7]))
print(battle_manager.add_ship_to_zone(pirate_zone, battle_manager.ships[8]))
print(battle_manager.add_ship_to_zone(pirate_zone, battle_manager.ships[9]))
print(battle_manager.add_ship_to_zone(pirate_zone, battle_manager.ships[10]))
print()

# Remove a battleship
print(battle_manager.remove_battleship("RoyalTwo"))
print(battle_manager.remove_battleship("Nonexistent"))
print()

# Start battle in RoyalZone
print(battle_manager.start_battle(royal_zone))
print()

# Start battle in PirateZone
print(battle_manager.start_battle(pirate_zone))
print()

# Start another battle in RoyalZone
print(battle_manager.start_battle(royal_zone))
print()

# Retrieve updated statistics
print(battle_manager.get_statistics())
print()

# Remove a battleship
print(battle_manager.remove_battleship("RoyalThree"))
print(battle_manager.remove_battleship("RoyalOne"))
print(battle_manager.remove_battleship("PirateOne"))
print(battle_manager.remove_battleship("PirateTwo"))
print(battle_manager.remove_battleship("PirateThree"))
print(battle_manager.get_statistics())
print()
