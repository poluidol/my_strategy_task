from units.unit import Unit


class RaceAbility(Unit):
    def __init__(self, unit: Unit):
        super().__init__()
        self.unit = unit

    def ability(self):
        pass

    def give_hp(self):
        return self.unit.give_hp()

    def give_armor(self):
        return self.unit.give_armor()

    def give_attack(self):
        return self.unit.give_attack()

    def give_pos_x(self):
        return self.unit.give_pos_x()

    def give_pos_y(self):
        return self.unit.give_pos_y()

    def give_owner_id(self):
        return self.unit.owner_id()

    def change_hp(self, change):
        self.unit.change_hp(change)

    def change_armor(self, change):
        self.unit.change_armor(change)

    def change_attack(self, change):
        self.unit.change_attack(change)

    def change_pos_x(self, change):
        self.unit.change_pos_x(change)

    def change_pos_y(self, change):
        self.unit.change_pos_y(change)

    def say(self) -> str:
        return self.unit.say()



