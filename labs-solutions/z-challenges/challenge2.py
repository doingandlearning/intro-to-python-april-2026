low = 0
in_range = 0
high = 0

while True:
    value = input("Enter signal strength (or 'done' to finish): ")
    if value.lower() == 'done':
        break
    if value.replace('.', '', 1).isdigit():
        signal = float(value)
        if signal < 2.5:
            print("Too low")
            low += 1
        elif signal > 4.0:
            print("Too high")
            high += 1
        else:
            print("In range")
            in_range += 1
    else:
        print("Invalid input.")

print("\nSummary:")
print("Too low:", low)
print("In range:", in_range)
print("Too high:", high)
