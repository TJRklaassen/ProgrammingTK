import time
import csv

while True:
    naam = input("Wat is je achternaam? ")

    if naam == "einde":
        break

    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")
    crdatum = str(time.strftime('%a %d %B %Y at %H:%M', time.localtime()))

    with open('inloggers.csv', 'a', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow([crdatum,voorl,naam,gbdatum,email])
