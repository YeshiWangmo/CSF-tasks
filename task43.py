user_name = input("Please enter your name: ")
vowels = "aeiouAEIOU"

for char in user_name:
    if char in vowels:
        print(True)
        break
else:
    print(False)