# Tracks the current game state - down, distance, field position, and possession.

import random

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
        self.field_position += yards_gained # update the new field position
        self.yards_to_go -= yards_gained    # update the yards_to_go to gain a first down

        # If the offense exceeds the required yardage for a first down, reset the down and distance
        if self.yards_to_go <= 0:
            self.down = 1
            self.yards_to_go = 10
            return True
        # If the offense does not gain enough yardage for a first down, increment the down
        else:
            self.down += 1
            return False

    # Determines if the current field position is a touchdown (75 yards or more)
    def is_touchdown(self):
        return self.field_position >= 75

    # Determines if the current field position is a safety (0 yards or less)
    def is_turnover_on_downs(self):
        return self.down > 4

     # Runs a single play: picks run or pass, achieve play end, and updates game state
    def run_play(self):
        offense = self.possession   # offense is in possesion of the football
        defense = self.other_team() # defense does not have possesion of the football
 
        play_call = random.choice(["run", "pass"])
 
        # Determine the play call type, and execute accordingly
        if play_call == "run":
            yards = self._resolve_run(offense.get_rb(), defense.get_dl(), defense.get_lb())
        else:
            yards = self._resolve_pass(offense.get_qb(), offense.get_wr(),
                                        defense.get_dl(), defense.get_cb())
 
        # Evaluate total yardage gain or loss
        self._process_result(yards)
 
    # RB tries to get past the D-lineman, then the linebacker gets a shot at the tackle
    # Claude assistance was used in order to determine run play logic
    def _resolve_run(self, rb, dl, lb):
        # Initial case 
        # If the running back is tackled by the defensive lineman
        if not rb.run(dl):
            yards = random.randint(-2, 2)
            print(f"{rb.name} is stopped at the line for {yards} yards.")
            return yards
 
        # If the linebacker tackles the running back, determine yardage gain
        if lb.tackle(rb):
            yards = random.randint(1, 5)
            print(f"{rb.name} breaks the first tackle but is brought down after {yards} yards.")
        else:
        # If the running back breaks through both the DL and LB tackles, big gain
            yards = random.randint(10, 30)
            print(f"{rb.name} breaks through for a big gain of {yards} yards!")
        return yards
 
    # DL gets a sack chance first, then QB throws, then CB tries to tackle after the catch
    # Claude assistance was used in order to determine pass completion situations
    def _resolve_pass(self, qb, wr, dl, cb):
        # If the defensive lineman sacks the quarterback
        if dl.sack(qb):
            yards = random.randint(-8, -2)     # medium loss on the play for offense
            print(f"{qb.name} is sacked for a loss of {abs(yards)} yards!")
            return yards
 
        # If the quarterback is NOT sacked, implies the pass is thrown to the wide receiver
        distance, caught = qb.throw(wr, cb, self.yards_to_go)
 
        # If the pass is not caught by the wide receiver, incomplete and end the play (hence return 0)
        if caught == False:
            print(f"  {distance} pass to {wr.name} falls incomplete.")
            return 0
 
        # Creating a tuple in order to determine how many yards are gained based on the pass distance
        yard_ranges = {"short": (2, 8), "medium": (8, 18), "long": (18, 40)}
        # Choose a distance gained from the tuple listed above
        yards = random.randint(*yard_ranges[distance])
 
        # If the corner back tackles the wide receiver, assuming he is immediately tackled
        if cb.tackle(wr):
            yards = min(yards, random.randint(1, 5))
            print(f"{distance} pass to {wr.name}, tackled after {yards} yards.")
        else:
        # If the cornerback does NOT tackle the wide receiver
            print(f"{distance} pass to {wr.name}, tackle missed, gains {yards} yards!")
        return yards
 
    # Applies yardage to game state and handles touchdowns or turnovers on downs
    # Private method so the game_info could be updated within this class
    def _process_result(self, yards):
        offense = self.possession   # offense is in possesion of the football
        first_down = self.advance(yards) # defense does not have possesion of the football
 
        # If a touchdown is scored, update the score, reset the drive, then change possesion
        if self.is_touchdown():
            print(f"  TOUCHDOWN, {offense.name}!\n")
            offense.add_score(7)
            self.reset_drive()
            self.change_possession()
            return
 
        # If a first down is achieved, print message
        if first_down:
            print(f"  First down, {offense.name}!\n")
        # If a turnover is achieved, print message and change the possesion
        elif self.is_turnover_on_downs():
            print(f"  Turnover on downs. {self.other_team().name} takes over.\n")
            self.change_possession()
        else:
            print()  # blank line for readability between plays
 
    # Runs a set number of plays, used to represent one quarter
    def play_quarter(self, num_plays=6):
        for _ in range(num_plays):
            self.run_play()
 
    # Runs the full game across all quarters
    # Defaults - 4 quarters in a regular game, let's say 6 total plays per quarter
    def play_game(self, quarters=4, plays_per_quarter=6):
        for q in range(1, quarters + 1):
            self.quarter = q
            print(f"QUARTER {q}")
            self.play_quarter(plays_per_quarter)
 
    # Display the final score of the game for each team
    def final_score(self):
        print("\nFinal Score:")
        print(f"  {self.home_team.name}: {self.home_team.score}")
        print(f"  {self.away_team.name}: {self.away_team.score}")