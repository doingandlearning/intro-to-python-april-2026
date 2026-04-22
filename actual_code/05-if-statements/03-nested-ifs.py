snowing = input("Is it snowing? (y/n)")
temp = float(input("What's the temperature?"))

if temp < 0:
    print("It's freezing!")
    print("Time for hot chocolate")

if snowing == "y" and temp < 0:
    print("Put on your boots!")

if snowing == "y" or temp < 0:
    print("Sounds like nasty weather")

print("Bye!")