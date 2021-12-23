from units.unit import AirUnit
from config.unitStats.undead import dragon_stats


class Dragon(AirUnit):
    def __init__(self):
        super().__init__()

        self.attack = dragon_stats.attack
        self.hp = dragon_stats.hp
        self.armor = dragon_stats.armor

    def say(self) -> str:
        return "AAaaaAAAA Im a Dragon"