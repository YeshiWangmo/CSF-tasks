grade = input("Enter your grade:")
grade =int(grade)

if grade >= 90:
    print("A")
if 80 <= grade <= 89:
    print("B")
if 70<= grade<= 79:
    print("C")
if grade < 70:
    print("F")