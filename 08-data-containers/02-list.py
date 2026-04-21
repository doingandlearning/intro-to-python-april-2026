empty_list = []
empty_list = list()

print(empty_list)
print(type(empty_list))

beatles = ["John", "Paul", "George", "Ringo"]
print(beatles[0])
print(beatles[1:])
print(tuple(beatles))

print("Kevin" in beatles)
for band_member in beatles:
    print(band_member)

beatles.count("Kevin")
beatles.index("John")

# CRUD -> Create, Read, Update, Delete

# Create
beatles.append("Ivan") # a single element to my list!
print(beatles)

beatles.extend(["Maylinn", "Yosri", "Natalia"])
print(beatles)

beatles.insert(0, "Emile")
print(beatles)

# Reading
print(beatles[4])
print(beatles[-1])


# Updating
beatles[5] = "Basak"
print(beatles)
print(beatles.pop(0))
print(beatles)

# Delete
del beatles[4:]
print(beatles)
beatles.append("John")

# amount = beatles.count("John")
#
# for _ in range(amount):
#     beatles.remove("John")

# while "John" in beatles:
#     beatles.remove("John")

unique_beatles = []

for beatle in beatles:
    if beatle not in unique_beatles:
        unique_beatles.append(beatle)

print(beatles)
print(unique_beatles)


