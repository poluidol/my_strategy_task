from unitCreators.unitCreator import UnitCreator
from units.unit import Unit, GroundUnit, AirUnit
from units.undeadUnits.dragon import Dragon
from units.undeadUnits.skeleton import Skeleton


class UndeadUnitCreator(UnitCreator):

    def give_ground_unit(self) -> Unit:
        new_dark_ground_unit: GroundUnit = Skeleton()
        return new_dark_ground_unit

    def give_air_unit(self) -> Unit:
        new_dark_air_unit: AirUnit = Dragon()
        return new_dark_air_unit
