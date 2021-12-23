class CompoundUnits:
    def __init__(self):
        self.unitObjects = []

    def add_unit(self, unit):
        self.unitObjects.append(unit)

    def get_hp(self):
        sum_hp = 0
        for elem in self.unitObjects:
            sum_hp += elem.give_hp()
        return sum_hp

    def get_armor(self):
        sum_armor = 0
        for elem in self.unitObjects:
            sum_armor += elem.give_armor()
        return sum_armor

    def get_attack(self):
        sum_attack = 0
        for elem in self.unitObjects:
            sum_attack += elem.give_attack()
        return sum_attack

    def change_pos_x(self, change):
        for elem in self.unitObjects:
            elem.pos_x += change

    def change_pos_y(self, change):
        for elem in self.unitObjects:
            elem.pos_y += change

    def delete_unit(self, unit):
        self.unitObjects.pop(self.unitObjects.index(unit))
