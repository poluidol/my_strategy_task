from unitCreators.unitCreator import UnitCreator
from units.unit import Unit, GroundUnit, AirUnit
from units.allianceUnits.griffin import Griffin
from units.allianceUnits.civil import Civil


class AllianceUnitCreator(UnitCreator):

    def give_ground_unit(self) -> Unit:
        new_alliance_ground_unit: GroundUnit = Civil()
        return new_alliance_ground_unit

    def give_air_unit(self) -> Unit:
        new_alliance_air_unit: AirUnit = Griffin()
        return new_alliance_air_unit
