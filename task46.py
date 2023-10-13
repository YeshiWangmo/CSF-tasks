# Initialize factorial and i
factorial = 1
i = 1

# Get the number from the user
num = int(input("Enter a number: "))

# Calculate the factorial
while i <= num:
    factorial *= i
    i += 1

# Print the result
print("The factorial of", num, "is", factorial)