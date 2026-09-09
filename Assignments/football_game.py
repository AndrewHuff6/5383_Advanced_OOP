# Football Game Simulation using Python
# Andrew Huff - 5383 Advanced OOP

# Super class definition for all players in the game.
class Player:
    def __init(self, name, position, skill_level):
        self.name = name
        self.position = position
        self.skill_level = skill_level

# BEGINNING OF PROGRAM RUN
print("Welcome to Andrew's Football Game Simulator!")
choice = input("Press space -> enter to start the game...")

if choice != " ":
    print("Goodbye!")
else:
    print("Let's play some football!")
    print("Loading game...")

# Create a list of players for the game
offense_players = []
defense_players = []

# Game loop
while True:
    break  # Placeholder for game logic, to be implemented later
