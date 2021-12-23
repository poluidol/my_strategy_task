from raceAbilities.abilityDecorator import RaceAbility
from config.abilityConfig.undead import rage_config


class UndeadAbilityRage(RaceAbility):
    def ability(self):
        self.change_hp(rage_config.hp_change)
        self.change_attack(rage_config.attack_chang)
        self.change_armor(rage_config.armor_change)



