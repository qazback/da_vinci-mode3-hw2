import random

def prompt_positive_integer(message):
    while True:
        try:
            number = int(input(message))
            if number <= 0:
                raise ValueError
            return number
        except ValueError:
            print("Please enter a positive integer.")

# Prompt for the level
level = prompt_positive_integer("Enter a level: ")

# Generate a random number
target_number = random.randint(1, level)

# Guessing loop
while True:
    # Prompt for the user's guess
    guess = prompt_positive_integer("Enter your guess: ")

    # Compare the guess with the target number
    if guess < target_number:
        print("Too small!")
    elif guess > target_number:
        print("Too large!")
    else:
        print("Just right!")
        break
