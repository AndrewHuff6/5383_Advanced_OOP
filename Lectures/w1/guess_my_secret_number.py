import random

secret = int(random.randint(1,6))
guess = int(input("Guess a number: "))
count = 0

if secret != guess:
    if guess > secret:
        print("Too high!")
        count += 1
    elif guess < secret:
        print("Too low!")
        count += 1
else:
    count += 1
    print(f"You guessed correctly! It took you {count} guesses.")

#for i in range(3):
#    pass
