import random

# Initialize the secret number
secret_number= int(input("enter the secret number:"))


# Main game loop
while True:
    # Ask the user for their guess
    guess = int(input("Guess a number between 1 and 100: "))

    # Provide feedback based on the user's guess
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations, you guessed the correct number!")
        break
