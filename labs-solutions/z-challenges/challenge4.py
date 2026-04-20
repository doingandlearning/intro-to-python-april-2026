schedule = []

print("Enter events and times (e.g., 'Meeting 09:00'). Type 'done' to finish.")

while True:
    entry = input("> ")
    if entry.lower() == 'done':
        break
    parts = entry.split()
    if len(parts) >= 2:
        time = parts[-1]
        event = ' '.join(parts[:-1])
        schedule.append((time, event))
    else:
        print("Invalid format. Please use 'Event Time'.")

# Sort by time (HH:MM strings sort correctly)
sorted_schedule = sorted(schedule)

print("\nYour Schedule:")
for time, event in sorted_schedule:
    print(f"{time} - {event}")
