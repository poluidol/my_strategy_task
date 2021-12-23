from game_object import GameObject


class Unit(GameObject):
    def __init__(self):
        self.hp = 0
        self.armor = 0
        self.attack = 0
        self.pos_x = 0
        self.pos_y = 0
        self.owner_id = 0

    def say(self) -> str:
        pass

    def give_hp(self):
        return self.hp

    def give_armor(self):
        return self.armor

    def give_attack(self):
        return self.attack

    def give_pos_x(self):
        return self.pos_x

    def give_pos_y(self):
        return self.pos_y

    def give_owner_id(self):
        return self.owner_id

    def change_hp(self, change):
        self.hp += change

    def change_armor(self, change):
        self.armor += change

    def change_attack(self, change):
        self.attack += change

    def change_pos_x(self, change):
        self.pos_x += change

    def change_pos_y(self, change):
        self.pos_y += change







class GroundUnit(Unit):
    def say(self) -> str:
        pass


class AirUnit(Unit):
    def say(self) -> str:
        pass
