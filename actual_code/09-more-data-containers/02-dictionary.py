empty_dict = {}
empty_dict = dict()

cities = {
    "Switzerland": "Bern",
    "France": "Paris",
    "Poland": "Warsaw",
    "Netherlands": "Amsterdam",
    "United Kingdom": ["London", "Belfast"]
}

print("Switzerland" in cities)
print("Bern" in cities)

for country in cities:
    print(f"{country}: {cities[country]}")

# Safer way to access the data
print(cities.get("France", "Unknown"))

print(list(cities.keys()))
print(list(cities.values()))
print(list(cities.items()))

cities["Germany"] = "Berlin"
cities["United Kingdom"] = "London"

del cities["United Kingdom"]

print(cities)


for country in cities:
    print(f"{country}: {cities[country]}")

for country, city in cities.items():
    print(f"{country}: {city}")


