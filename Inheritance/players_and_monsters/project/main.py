from project.elf import Elf
from project.hero import Hero
from project.soul_master import SoulMaster

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
print(hero.__class__.__subclasses__())
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__)
print(elf.username)
print(elf.level)
soul = SoulMaster("Soul", 13)
print(soul)
print(soul.__class__.__mro__)
