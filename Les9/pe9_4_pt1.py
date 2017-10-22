import csv

with open('producten.csv', 'w',newline='') as f:
    fieldnames = ['Artikelnummer','Artikelcode','Naam','Voorraad','Prijs']
    writer = csv.DictWriter(f, delimiter=';', fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Artikelnummer':121, 'Artikelcode':'ABC123', 'Naam':'Highlight pen', 'Voorraad':231, 'Prijs':0.56})
    writer.writerow({'Artikelnummer':123, 'Artikelcode':'PQR678', 'Naam':'Nietmachine', 'Voorraad':587, 'Prijs':9.99})
    writer.writerow({'Artikelnummer':128, 'Artikelcode':'ZYX163', 'Naam':'Bureaulamp', 'Voorraad':34, 'Prijs':19.95})
    writer.writerow({'Artikelnummer':137, 'Artikelcode':'MLK709', 'Naam':'Monitorstandaard','Voorraad':66, 'Prijs':32.50})
    writer.writerow({'Artikelnummer':271, 'Artikelcode':'TRS665', 'Naam':'Ipad hoes', 'Voorraad':155, 'Prijs':19.01})
