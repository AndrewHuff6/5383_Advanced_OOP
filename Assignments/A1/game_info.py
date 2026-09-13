# Tracks the current game state - down, distance, field position, and possession.
class GameState:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.possession = home_team
        self.down = 1
        self.yards_to_go = 10
        self.field_position = 25  # yards from the possessing team's own end zone
        self.quarter = 1

    def other_team(self):
        return self.away_team if self.possession is self.home_team else self.home_team

    # Turnover (interception or turnover on downs) or opposing team scores a touchdown
    def change_possession(self):
        self.possession = self.other_team()
        self.field_position = max(0, 100 - self.field_position)
        self.down = 1
        self.yards_to_go = 10

    # Resets the next drive at the 25 yard line, 1st down and 10 yards to go
    def reset_drive(self):
        self.field_position = 25
        self.down = 1
        self.yards_to_go = 10

    # Updates down, distance, and field position after a play's yardage is known
    # Returns True if the play resulted in a first down, False otherwise
    def advance(self, yards_gained):
        self.field_position += yards_gained
        self.yards_to_go -= yards_gained

        # If the offense exceeds the required yardage for a first down, reset the down and distance
        if self.yards_to_go <= 0:
            self.down = 1
            self.yards_to_go = 10
            return True

        # If the offense does not gain enough yardage for a first down, increment the down
        else:
            self.down += 1
            # If the offense has reached 4th down and has not gained enough yardage for a first down, change possession
            if self.down > 4:
                self.change_possession()
                return False

    # Determines if the current field position is a touchdown (75 yards or more)
    def is_touchdown(self):
        return self.field_position >= 75

    # Determines if the current field position is a safety (0 yards or less)
    def is_turnover_on_downs(self):
        return self.down > 4