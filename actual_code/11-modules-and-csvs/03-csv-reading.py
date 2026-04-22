import csv

with open('songs.csv') as csvfile:
    reader = csv.reader(csvfile)
    # for _ in range(3):
    #     next(reader) # skip the header row
    next(reader)
    next(reader)
    next(reader)
    for row in reader:
        row[1] = int(row[1])
        print(row)