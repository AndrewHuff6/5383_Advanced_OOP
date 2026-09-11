# Python file for the players in the game

# Super class definition for all players in the game.
class Player:
    def __init__(self, name, position, speed, strength, stamina):
        self.name = name
        self.position = position
        self.strength = strength
        self.speed = speed
        self.stamina = stamina

# Quarterback class definition for the QBs in the game.
class QuarterBack(Player):
    def __init__(self, name, speed=60, strength=70, stamina=75):
        super().__init__(name, "Quarterback", speed, strength, stamina)

    def hello(self):
        pass

# Running back class definition for all RBs in the game.
class RunningBack(Player):
    def __init__(self, name, speed=80, strength=90, stamina=85):
        super().__init__(name, "Running back", speed, strength, stamina)

# Wide receiver class definition for all WRs in the game.
class WideReceiver(Player):
    def __init__(self, name, speed=90, strength=65, stamina=80):
        super().__init__(name, "Wide receiver", speed, strength, stamina)

# Defensive lineman class definition for all DLs in the game.
class Deflineman(Player):
    def __init__(self, name, speed=55, strength=95, stamina=70):
        super().__init__(name, "D-Lineman", speed, strength, stamina)

# Linebacker class definition for all LBs in the game.
class LineBacker(Player):
    def __init__(self, name, speed=70, strength=90, stamina=75):
        super().__init__(name, "Linebacker", speed, strength, stamina)

# Cornerback class definition for all CBs in the game.
class CornerBack(Player):
    def __init__(self, name, speed=90, strength=70, stamina=75):
        super().__init__(name, "Cornerback", speed, strength, stamina)