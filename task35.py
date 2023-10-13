day = input("Enter the day:")
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday":
    print("Weekday")
elif day == "Friday":
    print("TGIF")
elif day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Invalid input")


