# Step 1: Define a variable and get the name from the user
user_name = input("Please enter your name: ")

# Step 2: Initialize a counter variable
vowel_count = 0

# Step 3: Use a for loop to iterate over each character in the name
for char in user_name:
    # Step 4: Check if the character is a vowel
    if char.lower() in 'aeiou':
        # Step 5: Increment the counter if the character is a vowel
        vowel_count += 1

# Step 6: Print the counter
print("The number of vowels in your name is: ", vowel_count)