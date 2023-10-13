# Step 1: Get user inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Step 2: Initialize the sum variable
sum = 0

# Step 3: Use a while loop to calculate the sum
current_number = num1
while current_number <= num2:
    sum += current_number
    current_number += 1

# Step 4: Display the final sum
print("The sum of all numbers between", num1, "and", num2, "is", sum)