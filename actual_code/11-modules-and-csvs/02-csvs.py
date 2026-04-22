import csv

def write_song(song):
    with open('songs.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(song)

write_song(["Love Me Do", 1962])
write_song(["I want to hold your hand", 1963])
write_song(["She loves you", 1963])
write_song(["Yesterday", 1965])