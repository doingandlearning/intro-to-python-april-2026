flights = {'London': ('EY123', 'Monday', '12:00', 'Geneva'),
           'Geneva': ('AI454', 'Tuesday', '13:00', 'London'),
           'Dublin': ('BA987', 'Wednesday', '14:00', 'Dublin'),
           'Seville': ('SA527', 'Thursday', '11:00', 'Cardiff'),
           'Cardiff': ('WA129', 'Friday', '10:00', 'Dublin')}


# 1. Reverse lookup by destination
destination_map = {}
for city, (flight_no, day, time, dest) in flights.items():
    if dest not in destination_map:
        destination_map[dest] = []
    destination_map[dest].append((city, flight_no))
print("Flights by destination:", destination_map)

# 2. Find flights by day
target_day = input("Enter a day to search for flights: ")
for city, (flight_no, day, time, dest) in flights.items():
    if day.lower() == target_day.lower():
        print(f"{city} → {dest} at {time} [{flight_no}]")

# 3. Simulate timezone adjustments (fixed example without random)
offsets = {'London': +1, 'Geneva': +2, 'Dublin': 0, 'Seville': +1, 'France': +2}
print("Adjusted times (UTC approximation):")
for city, (flight_no, day, time, dest) in flights.items():
    hour, minute = map(int, time.split(":"))
    utc_hour = hour - offsets.get(city, 0)
    print(f"{city}: departs at {utc_hour:02d}:{minute:02d} UTC")

# 4. Update a flight
update_city = input("City to update flight for: ")
if update_city in flights:
    new_time = input("New time (HH:MM): ")
    new_dest = input("New destination: ")
    flight_no, day, _, _ = flights[update_city]
    flights[update_city] = (flight_no, day, new_time, new_dest)
    print("Updated flight:", flights[update_city])
else:
    print("City not found.")

# 5. Connecting flights within 2 hours
def parse_time(time_str):
    h, m = map(int, time_str.split(":"))
    return h * 60 + m

print("Connecting flights:")
for city1, (f1, d1, t1, mid) in flights.items():
    for city2, (f2, d2, t2, dest) in flights.items():
        if city2 == mid:
            arrival = parse_time(t1)
            departure = parse_time(t2)
            if 0 < departure - arrival <= 120:
                print(f"{city1} → {mid} → {dest}")
