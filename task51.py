# Step 1: Get user inputs
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Step 2: Initialize sum to 0
sum = 0

# Step 3: Calculate the sum of all numbers between num1 and num2
for i in range(num1, num2 + 1):
    sum += i

# Step 4: Print the final sum
print("The sum of all numbers between", num1, "and", num2, "is", sum)
