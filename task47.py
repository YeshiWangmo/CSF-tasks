# Define a function to calculate factorial
def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Get user input and convert it to an integer
user_number = int(input("Enter a number: "))

# Calculate the factorial of the user_number
factorial = calculate_factorial(user_number)

# Display the factorial
print("The factorial of", user_number, "is", factorial)