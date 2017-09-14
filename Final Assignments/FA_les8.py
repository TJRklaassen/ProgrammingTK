def inlezen_beginstation(stations):
    'Vraagt naar het beginstation en controleert of dit een station in het traject(list "stations") is'
    while True:
        beginstation = input("Wat is je beginstation? : ")
        if beginstation in stations:
            return beginstation
        else:
            print("Deze trein komt niet in",beginstation)

def inlezen_eindstation(stations):
    'Vraagt naar het eindstation en controleert of dit een station in het traject(list "stations") is'
    while True:
        eindstation = input("Wat is je eindstation? : ")
        if eindstation in stations:
            return eindstation
        else:
            print("Deze trein komt niet in",eindstation)

def omroepen_reis(stations,beginstation,eindstation):
    'Gebruikt het begin -en eindstation en de list "stations" om alle reisgegevens te berekenen en te printen'
    beginNummer = stations.index(beginstation)+1
    eindNummer = stations.index(eindstation)+1
    afstand = eindNummer - beginNummer

    print("\nHet beginstation {} is het {}e station in het traject.".format(beginstation,beginNummer))
    print("Het eindstation {} is het {}e station in het traject.".format(eindstation,eindNummer))
    print("De afstand bedraagt",afstand,"station(s).")
    print("De prijs van het kaartje is",afstand*5,"euro.\n")
    print("Jij stapt in de trein in:",beginstation)

    for station in stations:                                            #Gaat langs alle stations in het traject
        stationNummer = stations.index(station)+1

        if stationNummer > beginNummer and stationNummer < eindNummer:  #Checkt of het station tussen het begin -en eindstation zit en als dat zo is, wordt deze geprint als tussenstation
            print("-",station)

    print("Jij stapt uit in:",eindstation)

stations = ['Schagen','Heerhugowaard','Alkmaar','Castricum','Zaandam','Amsterdam Sloterdijk','Amsterdam Centraal','Amsterdam Amstel','Utrecht Centraal',"'s-Hertogenbosch",'Eindhoven','Weert','Roermond','Sittard','Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations)
omroepen_reis(stations,beginstation,eindstation)
