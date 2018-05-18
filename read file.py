import csv
with open('autolib-disponibilite-temps-reel.csv', 'r',encoding="utf8") as csvfile:
#csvfile = open('autolib-disponibilite-temps-reel.csv', 'r')
    ar ={}
    for row in csv.reader(csvfile, delimiter=';'):
        if row[12].startswith("750"):
            #print(row[1],row[12])
            if not row[12] in ar:
                ar[row[12]]=int(row[1])
            else:
                ar[row[12]]+=int(row[1])
    print(ar)