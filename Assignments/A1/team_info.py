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

    # Getter method to return the QB position
    def get_qb(self):
        return self.offense_players[0]

    # Getter method to return the RB postion
    def get_rb(self):
        return self.offense_players[1]

    # Getter method to return the WR position
    def get_wr(self):
        return self.offense_players[2]

    # Getter method to return the DL position
    def get_dl(self):
        return self.defense_players[0]
    
    # Getter method to return the LB position
    def get_lb(self):
        return self.defense_players[1]

    # Getter method to return the CB position
    def get_cb(self):
        return self.defense_players[2]

    # Simple method that edits the previous score of the team by adding points to it
    def update_score(self, points):
        self.score += points
        