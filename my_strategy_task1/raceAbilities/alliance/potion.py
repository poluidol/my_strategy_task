from raceAbilities.abilityDecorator import RaceAbility
from config.abilityConfig.alliance import potion_config


class AllianceAbilityPotion(RaceAbility):
    def ability(self):
        self.change_hp(potion_config.hp_change)
