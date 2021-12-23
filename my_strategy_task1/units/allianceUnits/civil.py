from units.unit import GroundUnit
from config.unitStats.alliance import civil_stats


class Civil(GroundUnit):
    def __init__(self):
        super().__init__()

        self.attack = civil_stats.attack
        self.hp = civil_stats.hp
        self.armor = civil_stats.armor

    def say(self) -> str:
        return "O Hi Mark, Im a Civil"
