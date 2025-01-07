import random

# Exercise 1: Working with a while loop

# Printing the game rules
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# generate a random number between 1 and 10
number = random.randint(1,10)

# Track whether the user guessed the number
isGuessRight = False

# Create a while loop to handle the game logic
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        
