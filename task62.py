# Step 1: Define an empty list
user_inputs = []

# Step 2: Get three user inputs and append them to the list
for i in range(3):
    number = int(input("Enter a number: "))
    user_inputs.append(number)

# Step 3: Define a function that checks if all numbers are even
def is_even(user_inputs):
    return all(number % 2 == 0 for number in user_inputs)

# Step 4: Call the function with user_inputs as an argument and print the result
print(is_even(user_inputs))