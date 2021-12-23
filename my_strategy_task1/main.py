from unitCreators.unitCreator import UnitCreator
from unitCreators.AllianceUnitCreator.allianceUnitCreator import \
    AllianceUnitCreator
from unitCreators.UndeadUnitCreator.undeadUnitCreator import UndeadUnitCreator
from raceAbilities.alliance.potion import AllianceAbilityPotion
from raceAbilities.undead.rage import UndeadAbilityRage
from units.group.CompoundUnits import CompoundUnits
from control.userControl import UserControl
from control.commands.commands import MoveUnit
from player.player import Player
from observers.concreteObservers.lvlup_observer import LvlupObserver


def main():
    dark_barracks: UnitCreator = UndeadUnitCreator()
    new_undead_ground_unit = dark_barracks.give_ground_unit()
    new_air_unit = dark_barracks.give_air_unit()

    print(new_undead_ground_unit.say())
    print(new_air_unit.say())

    alliance_barracks: UnitCreator = AllianceUnitCreator()
    new_alliance_ground_unit = alliance_barracks.give_ground_unit()

    print(new_alliance_ground_unit.give_hp())

    new_alliance_ground_unit = AllianceAbilityPotion(new_alliance_ground_unit)

    print(new_alliance_ground_unit.give_hp(),
          new_alliance_ground_unit.give_armor(),
          new_alliance_ground_unit.give_attack())

    new_alliance_ground_unit.ability()

    print(new_alliance_ground_unit.give_hp(),
          new_alliance_ground_unit.give_armor(),
          new_alliance_ground_unit.give_attack())

    new_undead_ground_unit = UndeadAbilityRage(new_undead_ground_unit)

    print(new_undead_ground_unit.give_hp(),
          new_undead_ground_unit.give_armor(),
          new_undead_ground_unit.give_attack())

    new_undead_ground_unit.ability()

    print(new_undead_ground_unit.give_hp(),
          new_undead_ground_unit.give_armor(),
          new_undead_ground_unit.give_attack())

    new_select = CompoundUnits()

    new_select.add_unit(new_undead_ground_unit)
    new_select.add_unit(new_alliance_ground_unit)
    print(new_select.get_hp())

    new_select.delete_unit(new_alliance_ground_unit)
    print(new_select.get_hp())

    print("position: ")
    print("oldpos: ", new_alliance_ground_unit.give_pos_x(),
          new_alliance_ground_unit.give_pos_y())

    new_user_control = UserControl()
    new_user_control.set_on_start(MoveUnit(100, 100, new_alliance_ground_unit))
    new_user_control.execute()
    print("newpos: ", new_alliance_ground_unit.give_pos_x(),
          new_alliance_ground_unit.give_pos_y())

    print("observer: ")
    new_observer = LvlupObserver()
    new_observer2 = LvlupObserver()
    new_player = Player()
    new_player.attach_object(new_observer)
    new_player.attach_object(new_observer2)
    new_player.lvlup()


if __name__ == '__main__':
    main()
