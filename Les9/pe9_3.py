import csv

with open('gamers.csv', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    getalMax = 0

    for row in reader:
        if int(row[2]) > getalMax:
            naamMax = row[0]
            datumMax = row[1]
            getalMax = int(row[2])

    print("De hoogste score is: {} op {} behaald door {}".format(getalMax,datumMax,naamMax))
