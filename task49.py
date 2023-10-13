import random

# Generate a random secret number between 1 and 100
secret_number = int(input("enter the secret number:"))

# Initialize a variable to keep track of the number of guesses
guesses = 0

# Start a loop that will continue until the user guesses the correct number
for i in range(100):
    # Ask the user for their guess
    guess = int(input("Guess a number between 1 and 100: "))
    guesses += 1

    # If the guess is too high, print a message and continue the loop
    if guess > secret_number:
        print("Too high!")
    # If the guess is too low, print a message and continue the loop
    elif guess < secret_number:
        print("Too low!")
    # If the guess is correct, print a message and break the loop
    else:
        print(f"Congratulations! You guessed the secret number in {guesses} attempts.")
        break
