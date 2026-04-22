empty_set = set()

print(empty_set)
print(type(empty_set))

empty_set.add("France")
empty_set.add("Poland")
empty_set.add("Switzerland")
empty_set.add("Germany")
empty_set.add("Belgium")
empty_set.add("Mexico")
empty_set.add("Mexico")

print(empty_set)
print("France" in empty_set)
empty_set.remove("France")
print("France" in empty_set)

cities_we_want_to_visit = list(set(["Paris", "Rome", "Amsterdam", "Madrid", "Paris", "Amsterdam"]))
cities_we_want_to_visit.sort()
print(cities_we_want_to_visit)
