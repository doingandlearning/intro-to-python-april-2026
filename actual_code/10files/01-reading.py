file = open("test.txt", encoding="utf-8")

# .read()
contents = file.read()  # loads the whole the file as one big string.
print(contents)
print(type(contents))

# .readlines()
file.seek(0)
contents = file.readlines()
print(contents)
print(type(contents))

print(contents)

for l in contents:
    object, colour = l.split(":")
    if "e" in object:
        print(l.strip())


# .readline()
file.seek(0)
line = file.readline()
while line:
    object, colour = line.split(":")
    if "e" in object:
        print(line.strip())
    line = file.readline()

file.close()