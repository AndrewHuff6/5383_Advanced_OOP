# Python file for the players in the game

# Random introduces margin of error for the simulated players
import random

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
    def __init__(self, name, speed=80, strength=70, stamina=75, accuracy=80):
        super().__init__(name, "Quarterback", speed, strength, stamina)
        self.accuracy = accuracy

    def throw_distance(self, yards_to_go):
        if yards_to_go <= 4:
            # Short pass is more likely for short yardage situations
            weights = {"short": 0.4, "medium": 0.4, "long": 0.2}
        elif yards_to_go <= 10:
            # Medium pass is more likely for medium yardage situations
            weights = {"short": 0.3, "medium": 0.5, "long": 0.2}
        else:
            # Long pass is more likely for long yardage situations
            weights = {"short": 0.1, "medium": 0.3, "long": 0.6}
        
        distances = list(weights.keys())
        chances = list(weights.values())
        return random.choices(distances, chances, k=1)[0]

    # Quarterback specific function to pass the ball to a receiver
    # yards_to_go is set to 10, since Offense starts with 1st and 10
    # Note: Wanted to call "pass", but pass is a reserved word already :-/
    def throw(self, receiver, defender, yards_to_go=10):
        distance = self.throw_distance(yards_to_go)

        # Modify the quarterback's accuracy based on the distance of the throw
        if distance == "short":
            accuracy_modifier = 5
        elif distance == "medium":
            accuracy_modifier = 0
        else: 
            accuracy_modifier = -5

        ball_placement = self.accuracy + accuracy_modifier + random.randint(-5, 5) # random reduced considering accuracy modifier
        # Determine if the receiver catches the ball based on the ball placement and the defender's coverage ability
        is_caught = receiver.catch(ball_placement, defender)

        # Return the distance of the throw and whether the receiver caught the ball
        return distance, is_caught


# Running back class definition for all RBs in the game.
class RunningBack(Player):
    def __init__(self, name, speed=80, strength=90, stamina=85):
        super().__init__(name, "Running back", speed, strength, stamina)

    def run(self, defender):
        run_chance = self.speed + random.randint(-10,10)
        if run_chance > defender.speed:
            return True # may change to a more complex calculation later, but for now, this is fine
        else:
            return False # may change to a more complex calculation later, but for now, this is fine

# Wide receiver class definition for all WRs in the game.
class WideReceiver(Player):
    def __init__(self, name, speed=90, strength=65, stamina=80, catch_ability=85):
        super().__init__(name, "Wide receiver", speed, strength, stamina)
        self.catch_ability = catch_ability

    def catch(self, ball_placement, defender):
        catch_chance = self.speed + self.catch_ability + ball_placement + random.randint(-10,10)
        if catch_chance > defender.speed + defender.coverage_ability:
            return True # may change to a more complex calculation later, but for now, this is fine
        else:
            return False # may change to a more complex calculation later, but for now, this is fine


# Defensive lineman class definition for all DLs in the game.
class Deflineman(Player):
    def __init__(self, name, speed=55, strength=95, stamina=70, pressure_ability=85):
        super().__init__(name, "D-Lineman", speed, strength, stamina)
        self.pressure_ability = pressure_ability

    def sack(self, quarterback):
        sack_chance = self.pressure_ability + random.randint(-10,10)
        if sack_chance > quarterback.speed:
            return True # may change to a more complex calculation later, but for now, this is fine
        else:
            return False # may change to a more complex calculation later, but for now, this is fine

# Linebacker class definition for all LBs in the game.
class LineBacker(Player):
    def __init__(self, name, speed=70, strength=90, stamina=75, tackle_ability=80):
        super().__init__(name, "Linebacker", speed, strength, stamina)
        # Position-specific attributes for the linebacker
        self.tackle_ability = tackle_ability

    # Linebacker specific function to tackle the running back
    def tackle(self, rb):
        tackle_chance = self.tackle_ability + random.randint(-10,10)
        if tackle_chance > rb.speed:
            return True # may change to a more complex calculation later, but for now, this is fine
        else:
            return False # may change to a more complex calculation later, but for now, this is fine

# Cornerback class definition for all CBs in the game.
class CornerBack(Player):
    def __init__(self, name, speed=90, strength=70, stamina=75, coverage_ability=75, tackle_ability=70):
        super().__init__(name, "Cornerback", speed, strength, stamina,)
        # Position-specific attributes for the cornerback
        self.coverage_ability = coverage_ability
        self.tackle_ability = tackle_ability

    def tackle(self, wide_receiver):
        tackle_chance = self.tackle_ability + random.randint(-10,10)
        if tackle_chance > wide_receiver.speed:
            return True # may change to a more complex calculation later, but for now, this is fine
        else:
            return False # may change to a more complex calculation later, but for now, this is fine