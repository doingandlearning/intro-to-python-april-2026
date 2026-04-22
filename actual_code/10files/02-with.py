file = open("test.txt")

line = file.readline()
while line:
    obj, colour = line.split(":")
    if "e" in obj:
        print(line.strip())
    line = file.readline()

file.close()

with open("test.txt") as file:
    line = file.readline()
    while line:
        obj, colour = line.split(":")
        if "e" in obj:
            print(line.strip())
        line = file.readline()
