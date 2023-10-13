user_inputs = []
for i in range(3):
    user_input = input("Enter a number: ")
    user_inputs.append(user_input)


def is_even(user_inputs):
    for num in user_inputs:
        if int(num) % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")


is_even(user_inputs)