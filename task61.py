def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

user_input = int(input("Please enter a number: "))
print(is_even(user_input))