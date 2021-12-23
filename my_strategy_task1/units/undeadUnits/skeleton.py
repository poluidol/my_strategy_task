from units.unit import GroundUnit
from config.unitStats.undead import skeleton_stats


class Skeleton(GroundUnit):

    def __init__(self):
        super().__init__()

        self.attack = skeleton_stats.attack
        self.hp = skeleton_stats.hp
        self.armor = skeleton_stats.armor

    def say(self) -> str:
        return "AAaaaAAAA Im a Skeleton"
