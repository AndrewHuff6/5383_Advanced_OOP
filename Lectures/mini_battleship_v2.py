# New and improved version of mini battleship
# Current issue(s)
# 1. The rows and columns are backwards
# 2. The indexing is thrown off


import random

# Function to display the boad
# Accepts the board state as a parameter
def display_board(board):
    for row in board:
        print(" ".join(row))

# Generate random placement of a 1 by 1 battleship
cpu_x = random.randint(1,5)
cpu_y = random.randint(1,5)

# Create the board
board = []
for row in range(5):
    board.append(['.','.','.','.','.'])

# Display the original board
display_board(board)

# Gameplay loop
print(cpu_x, cpu_y)
for i in range(2):
    # Grab the user's coords
    user_x = int(input("Enter your x-coordinate guess: "))
    user_y = int(input("Enter your y-coordinate guess: "))

    # Compare user coords to cpu coords
    if cpu_x == user_x and cpu_y == user_y:
        board[user_x][user_y] = "H"
        # Display the map
        display_board(board)
        break
    else:
        board[user_x][user_y] = "M"
        # Display the map
        display_board(board)