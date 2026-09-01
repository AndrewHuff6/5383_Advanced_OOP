# Base template in character creation for a fighting game.
# Andrew Huff - 9/1/26

import random

class Gon:
    def __init__(self):
        self.name = "Gon"
        self.health = 100
        self.attack_power = 20

    def heal(self, extra_hp):
        self.health = self.health + extra_hp

    def attack(self):
        return self.attack_power + random.randint(-5,5)

gon = Gon()