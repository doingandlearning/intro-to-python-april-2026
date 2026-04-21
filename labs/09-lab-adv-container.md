# Lab 9: Advanced Containers (Dictionary-Focused)

This lab focuses mainly on **dictionaries**, with **lists** and **tuples** where useful.

You will practise:

- choosing good dictionary keys and values
- updating and reading dictionary data
- looping through dictionary items
- writing small functions that work with dictionaries

---

## Hints and Tips

- Decide your dictionary shape before writing logic.
- Use `.get()` when a key might not exist.
- Use tuples when a record has a fixed structure.
- Use lists when order matters or when storing many records.
- Keep function jobs clear: compute, then return.

---

## Task 1: Build a Flight Dictionary

Create a dictionary named `flights`.

- Key: city name (string)
- Value: tuple `(flight_number, day, time, destination)`

Use at least 5 entries.

Then:

1. Print all departure cities.
2. Print all flight records.
3. Print the flight record for one city using `.get()`.

<details>
<summary>Solution (Task 1)</summary>

```python
flights = {
    "London": ("EY123", "Monday", "12:00", "Geneva"),
    "Geneva": ("AI454", "Tuesday", "13:00", "London"),
    "Dublin": ("BA987", "Wednesday", "14:00", "Lisbon"),
    "Seville": ("SA527", "Thursday", "11:00", "Cardiff"),
    "Cardiff": ("WA129", "Friday", "10:00", "Dublin"),
}

print("Cities:")
for city in flights:
    print(city)

print("\nRecords:")
for record in flights.values():
    print(record)

print("\nFlight from Dublin:")
print(flights.get("Dublin"))
```

</details>

---

## Task 2: Add, Update, and Remove Flights

Write a function:

`update_schedule(flights)`

Inside the function:

1. Add one new city entry.
2. Update the time for one existing city.
3. Remove one city with `pop()`.
4. Return the updated dictionary.

Then print all city/record pairs clearly.

<details>
<summary>Solution (Task 2)</summary>

```python
def update_schedule(flights):
    flights["Paris"] = ("AF429", "Saturday", "09:00", "London")
    flights["London"] = ("EY123", "Monday", "12:30", "Geneva")
    flights.pop("Cardiff")
    return flights


flights = {
    "London": ("EY123", "Monday", "12:00", "Geneva"),
    "Geneva": ("AI454", "Tuesday", "13:00", "London"),
    "Dublin": ("BA987", "Wednesday", "14:00", "Lisbon"),
    "Seville": ("SA527", "Thursday", "11:00", "Cardiff"),
    "Cardiff": ("WA129", "Friday", "10:00", "Dublin"),
}

updated = update_schedule(flights)
for city, info in updated.items():
    print(f"{city}: {info}")
```

</details>

---

## Task 3: Group Flights by Destination

Write a function:

`group_by_destination(flights)`

Create and return a new dictionary where:

- key = destination city
- value = list of departure cities that fly there

Example output idea:

`{"London": ["Geneva", "Paris"], "Dublin": ["Cardiff"]}`

<details>
<summary>Solution (Task 3)</summary>

```python
def group_by_destination(flights):
    grouped = {}
    for city, record in flights.items():
        destination = record[3]
        if destination not in grouped:
            grouped[destination] = []
        grouped[destination].append(city)
    return grouped


flights = {
    "London": ("EY123", "Monday", "12:00", "Geneva"),
    "Geneva": ("AI454", "Tuesday", "13:00", "London"),
    "Dublin": ("BA987", "Wednesday", "14:00", "London"),
    "Seville": ("SA527", "Thursday", "11:00", "Cardiff"),
    "Cardiff": ("WA129", "Friday", "10:00", "Dublin"),
}

result = group_by_destination(flights)
for destination, cities in result.items():
    print(f"{destination}: {cities}")
```

</details>

---

## Task 4 (Optional): Validate City Queries

Write a function:

`describe_flight(flights, city)`

Rules:

1. If the city exists, return a readable sentence with flight number, day, time, and destination.
2. If it does not exist, return `"No flight found for that city"`.

Ask the user for a city and print the result.

<details>
<summary>Solution (Task 4 Optional)</summary>

```python
def describe_flight(flights, city):
    record = flights.get(city)
    if record is None:
        return "No flight found for that city"

    flight_number = record[0]
    day = record[1]
    time = record[2]
    destination = record[3]
    return f"{city}: {flight_number} on {day} at {time} to {destination}"


flights = {
    "London": ("EY123", "Monday", "12:00", "Geneva"),
    "Geneva": ("AI454", "Tuesday", "13:00", "London"),
    "Dublin": ("BA987", "Wednesday", "14:00", "Lisbon"),
}

query = input("Enter city: ")
print(describe_flight(flights, query))
```

</details>

---

## Reflection

- Which dictionary key/value design worked best for these tasks?
- Where did using tuples make the records cleaner?
- Which function was easiest to reuse and why?
