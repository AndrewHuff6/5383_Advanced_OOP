# Python file used to store information on each team
# Will store Roster (player objects), score, and side of the ball (offense/defense)

# Super class definition for all teams in the game.
class Team:
    def __init__(self, name, offense_players, defense_players):
        self.name = name
        self.offense_players = offense_players
        self.defense_players = defense_players
        self.score = 0
        # self.side_of_ball = "offense"  # Default side of the ball is offense

    # Getter method to return the list of offensive players
    def get_offense_players(self):
        if self.offense_players[0].position == "Quarterback":
            return self.offense_players[0]
        elif self.offense_players[1].position == "RunningBack":
            return self.offense_players[1]
        elif self.offense_players[2].position == "WideReceiver":
            return self.offense_players[2]
        else:
            return None

    # Getter method to return the list of defensive players
    def get_defense_players(self):
        if self.defense_players[0].position == "Deflineman":
            return self.defense_players[0]
        elif self.defense_players[1].position == "Linebacker":
            return self.defense_players[1]
        elif self.defense_players[2].position == "Cornerback":
            return self.defense_players[2]
        else:
            return None

    # Simple method that edits the previous score of the team by adding points to it
    def update_score(self, points):
        self.score += points
        