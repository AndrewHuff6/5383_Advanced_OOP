# Football Game Simulation using Python
# Andrew Huff - 5383 Advanced OOP

# imports all position players to driver
from players import QuarterBack, RunningBack, WideReceiver, Deflineman, LineBacker, CornerBack   
from team_info import Team
from game_info import GameState
# from play_game import .

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

# TEAM ONE INFO
# Players on Offense
qb1 = QuarterBack("Andrew")
rb1 = RunningBack("John")
wr1 = WideReceiver("Mike")

# Players on Defense
dl1 = Deflineman("James")
lb1 = LineBacker("David")
cb1 = CornerBack("Chris")

# Create team objects for home teams
home_team = Team("Home Team", [qb1, rb1, wr1], [dl1, lb1, cb1])

# TEAM TWO INFO

# Players on Offense
qb2 = QuarterBack("Tom")
rb2 = RunningBack("Jerry")
wr2 = WideReceiver("Sam")

# Players on Defense
dl2 = Deflineman("Bob")
lb2 = LineBacker("Steve")
cb2 = CornerBack("Alex")

# Create team objects for away team
away_team = Team("Away Team", [qb2, rb2, wr2], [dl2, lb2, cb2])

# Display roster information for both teams
print(f"{home_team.name} - Offense:")
for player in home_team.offense_players:
    # Do not want to print ALL attributes of the players
    print(f" Player Name: {player.name}, Position: {player.position}")
 
print(f"{home_team.name} - Defense:")
for player in home_team.defense_players:
    # Do not want to print ALL attributes of the players
    print(f" Player Name: {player.name}, Position: {player.position}")

print("\n") # for visual purposes
 
print(f"{away_team.name} - Offense:")
for player in away_team.offense_players:
    # Do not want to print ALL attributes of the players
    print(f" Player Name: {player.name}, Position: {player.position}")
 
print(f"{away_team.name} - Defense:")
for player in away_team.defense_players:
    # Do not want to print ALL attributes of the players
    print(f" Player Name: {player.name}, Position: {player.position}")

game_state = GameState(home_team, away_team)

print("-" * 41)
print("Game setup complete! Starting the game...\n")
print(f"Down: {game_state.down}, Yards to go: {game_state.yards_to_go}, Field position: {game_state.field_position}, Possession: {game_state.possession.name}\n")
