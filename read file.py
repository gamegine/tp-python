import csv
with open('autolib-disponibilite-temps-reel.csv', 'r') as csvfile:
#csvfile = open('autolib-disponibilite-temps-reel.csv', 'r')
    for row in csv.reader(csvfile, delimiter=';'):
        if row[12].startswith("75"):
            print(row[1],row[12])