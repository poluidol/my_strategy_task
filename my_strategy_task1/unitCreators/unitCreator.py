from abc import ABC
from units.unit import Unit


class UnitCreator(ABC):

    def give_ground_unit(self) -> Unit:
        pass

    def give_air_unit(self) -> Unit:
        pass

