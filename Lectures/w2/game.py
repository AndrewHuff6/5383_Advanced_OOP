# Base template in character creation for a fighting game.
# Andrew Huff - 9/1/26

import random
import time

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def heal(self, extra_health_points):
        self.health = self.health + extra_health_points

    def attack(self):
        return self.attack_power + random.randint(1,5)

    def special_attack(self):
        pass
    
    def apply_damage(self, damage):
        self.health = self.health - damage

    def is_dead(self):
        if self.health <= 0:
            return True
        return False

    def show_status(self):
        print(self.name)


# Uses the super class init to create Gon
class Gon(Character):
    def __init__(self):
        super().__init__("Gon", 100, 20)
    
    def special_attack(self):
        print("This is Gon's special attack")
        return 20


# Uses the super class init to create Hisoka
class Hisoka(Character):
    def __init__(self):
        super().__init__("Hisoka", 120, 40)
        self.manuver = True

    def special_attack(self):
        print("This is Hisoka's special attack")
        return 30

    def is_dodging(self):
        return self.manuver

# Game class
class Game():
    def __init__(self, gon, hisoka):
        self.gon = gon
        self.hisoka = hisoka

    def gon_turn(self):
        # give gon a turn to attack
            option = input("Gon Attack Option: ")
            damage = 0  # default damage if no valid option is chosen
            if option == "1":
                damage = self.gon.attack()
            elif option == "2":
                damage = self.gon.special_attack()
            else:
                print("You missed your chance!")
            #self.gon.show_status()

    def start(self):
        while True:
            
            # below is to let the CPU choose a random attack for gon
            # damage = random.choice([self.gon.attack(), self.gon.special_attack()])

            # initialize damage variable to 0 before gon's turn to prevent undefined variable error
            damage = 0  # default damage if no valid option is chosen
            self.gon_turn()

            # calculate damage
            self.hisoka.apply_damage(damage)

            # check if hisoka is still alive
            if self.hisoka.is_dead():
                print("Gon is the winner!") # end the game
                break

            time.sleep(1) # wait a second before hisoka attacks

            # give hisoka a turn is he's still alive
            hisoka_option = random.choice(["1", "2", "3"])
            damage = 0  # default damage if no valid option is chosen
            if hisoka_option == "1":
                damage = self.hisoka.attack()
            elif hisoka_option == "2":
                damage = self.hisoka.special_attack()
            else:
                print("Hisoka missed!")

            # apply the damage to gon
            self.gon.apply_damage(damage)

            # check if gon is still alive
            if self.gon.is_dead():
                print("Hisoka is the winner!")
                break

        print("Game Over")    

# create the characters
gon = Gon()
hisoka = Hisoka()
game = Game(gon, hisoka)

# start the game
game.start()