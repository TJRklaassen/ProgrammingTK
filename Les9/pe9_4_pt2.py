import csv

with open('producten.csv', newline='') as f:
    reader = csv.DictReader(f, delimiter=';')
    prijsMax = 0
    voorraadMin = None
    voorraadTotaal = 0

    for row in reader:
        if float(row['Prijs']) > prijsMax:
            prijsMax = float(row['Prijs'])
            naam_prijsMax = row['Naam']

        if voorraadMin == None or int(row['Voorraad']) < voorraadMin:
            voorraadMin = int(row['Voorraad'])
            artikelnummer_voorraadMin = row['Artikelnummer']

        voorraadTotaal += int(row['Voorraad'])

    print("Het duurste artikel is {} en die kost {:.2f} Euro".format(naam_prijsMax,prijsMax))
    print("Er zijn slechts {} exemplaren in voorraad van het product met nummer {}".format(voorraadMin,artikelnummer_voorraadMin))
    print("In totaal hebben wij {} producten in ons magazijn liggen".format(voorraadTotaal))
