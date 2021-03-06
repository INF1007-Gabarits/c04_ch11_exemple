import random


class ShortSword:
    def __init__(self):
        self.damage = 15
        self.breaking_prob = 0.20
        self.resistance = 30
        self.is_broken = False

    def get_is_broken(self, damage_taken: int):
        if damage_taken > self.resistance and 0 <= random.random() < self.breaking_prob:
            self.is_broken = True

        return self.is_broken
