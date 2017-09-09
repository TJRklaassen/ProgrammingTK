def kwadraten_som(grondgetallen):
    totaal = 0
    for getal in grondgetallen:
        if getal > 0:
            totaal += getal**2
    return totaal

lst = [1,4,5,-25,3,2]
print(kwadraten_som(lst))
