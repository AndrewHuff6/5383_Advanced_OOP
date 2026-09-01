# First Version - done on 8/27/26
# Andrew Huff

import random

cpu_x = random.randint(1,5)
cpu_y = random.randint(1,5)

for i in range(3):
    # Grab the user's coords
    user_x = int(input("Enter your x-coordinate guess: "))
    user_y = int(input("Enter your y-coordinate guess: "))

    # Compare user coords to cpu coords
    if cpu_x == user_x and cpu_y == user_y:
        print("Hit!")
        print("------")
    else:
        print("Miss.")
        print("------")
