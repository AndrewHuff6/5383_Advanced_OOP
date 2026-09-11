# Football Game Simulation using Python
# Andrew Huff - 5383 Advanced OOP

# imports all position players to driver
from players import QuarterBack, RunningBack, WideReceiver, Deflineman, LineBacker, CornerBack   
# from play_game import .
# from team_info import .

# BEGINNING OF PROGRAM RUN
print("Welcome to Andrew's Football Game Simulator!")
choice = input("Press space -> enter to start the game...")

# Determine whether to start the game or exit based on user input
if choice != " ":
    print("Goodbye!")
else:
    print("-" * 41)
    print("Let's play some football!")
    print("Creating teams...")
    print("-" * 41)

# Create a list of players for the game
offense_players = []
defense_players = []

# Players on Offense
qb = QuarterBack("Andrew")
rb = RunningBack("John")
wr = WideReceiver("Mike")

# Players on Defense
dl = Deflineman("James")
lb = LineBacker("David")
cb = CornerBack("Chris")

offense_players.append(qb)  # Add the quarterback to the offense players list
offense_players.append(rb)  # Add the running back to the offense players list
offense_players.append(wr)  # Add the wide receiver to the offense players list

defense_players.append(dl)  # Add the defensive lineman to the defense players list
defense_players.append(lb)  # Add the line backer to the defense players list
defense_players.append(cb)  # Add the corner back to the defense players list

print("Offense:")
for player in offense_players:
    print(f" Player Name: {player.name}, Position: {player.position}, Speed: {player.speed}, Strength: {player.strength}, Stamina: {player.stamina}")

print("Defense:")
for player in defense_players:
    print(f" Player Name: {player.name}, Position: {player.position}, Speed: {player.speed}, Strength: {player.strength}, Stamina: {player.stamina}")