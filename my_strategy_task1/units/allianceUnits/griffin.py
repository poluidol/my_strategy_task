from units.unit import AirUnit
from config.unitStats.alliance import griffin_stats


class Griffin(AirUnit):
    def __init__(self):
        super().__init__()

        self.attack = griffin_stats.attack
        self.hp = griffin_stats.hp
        self.armor = griffin_stats.armor

    def say(self) -> str:
        return "O Hi Mark, Im a Lion-Bird"