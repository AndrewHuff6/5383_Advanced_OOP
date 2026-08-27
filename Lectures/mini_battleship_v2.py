# New and improved version of mini battleship
# Andrew Huff 8/27/26

import random

# Function to display the boad
# Accepts the board state as a parameter
def display_board(board):
    for row in board:
        print(" ".join(row))

#----------------------#
#                      #
# BEGINNING OF PROGRAM #
#                      #
#----------------------#

# Generate random placement of a 1 by 1 battleship
cpu_x = random.randint(1,5)
cpu_y = random.randint(1,5)

# Create the board - a 5 by 5 grid
board = []
for column in range(1,6): 
    board.append(['.','.','.','.','.'])

# Determines how many guesses the user has to find the battleship
guesses = 5

# Display the original board
display_board(board)

# Gameplay loop
# print(cpu_x, cpu_y)
for column in range(guesses):
    # Grab the user's coords
    user_x = int(input("Enter your x-coordinate guess (1-5): "))
    user_y = int(input("Enter your y-coordinate guess (1-5): "))

    # Compare user coords to cpu coords
    if cpu_x == user_x and cpu_y == user_y:
        board[user_y - 1][user_x - 1] = "H" # accounts for the indexing issue
        # Display the updated board
        display_board(board)
        print("Congratulations! You sunk my battleship!")
        break
    else:
        board[user_y - 1][user_x - 1] = "M" # accounts for the indexing issue
        # Display the updated board, try again
        display_board(board)
        guesses -= 1
        # For grammatical correctness
        if guesses > 1:
            print(f"You have {guesses} guesses left.")
        elif guesses == 1:
            print(f"You have {guesses} guess left.")
        else:
            print("You have no guesses left - Game over.")
            print(f"The battleship was at {cpu_x}, {cpu_y}.")