# Get the number from the user
num = int(input("Enter a number: "))

# Generate the multiplication table for the number
i = 1
while i <= 20:
    product = num * i
    print(f"{num} * {i} = {product}")
    i += 1