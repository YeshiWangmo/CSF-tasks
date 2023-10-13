user_name = input("Please enter your name: ")
vowels = 'aeiou'
i = 0
found_vowel = False

while i < len(user_name) and not found_vowel:
    if user_name[i].lower() in vowels:
        found_vowel = True
    i += 1

print(found_vowel)