def standaardprijs(afstandKM):
    if afstandKM < 0:
        afstandKM = 0

    if afstandKM > 50:
        return 15+(0.6*afstandKM)
    else:
        return 0.8*afstandKM

def ritprijs(leeftijd,weekendrit,afstandKM):
    prijs = standaardprijs(afstandKM)
    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit == True:
            return prijs * 0.65
        else:
            return prijs * 0.7
    else:
        if weekendrit == True:
            return prijs * 0.6
        else:
            return prijs

km = int(input('Afstand in kilometers: '))
leeftijd = int(input('Leeftijd: '))

if input('Weekendrit? ja/nee: ') == 'ja':
    weekendrit = True
else:
    weekendrit = False

print("De totale prijs van de reis is",'{:.2f}'.format(ritprijs(leeftijd,weekendrit,km)),"euro.")
