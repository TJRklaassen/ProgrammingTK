import random

def laad_kluizen():
    'Telkens als de lijst gerefreshed moet worden vanaf het bestand kluizen.txt, kan deze functie gebruikt worden'
    kluizenIn = open('kluizen.txt')
    list = kluizenIn.readlines()
    kluizenIn.close()
    return list

list = laad_kluizen()
listNR = []
listPIN = []

for line in list:         #Voegt alle losse kluisnummers en PIN-codes van kluizen.txt in hun bijbehorende list
    listNR.append(int(line.split(',')[0]))
    listPIN.append(int(line.split(',')[1]))

def nieuwe_kluis(listNR):
    'Deze functie geeft een beschikbare kluis met een nieuwe PIN-code'
    if 12-len(listNR) > 0:                                       #Checkt of er kluizen vrij zijn
        for i in range(12):                                      #Gaat langs alle kluizen van 0 tot 11 (dit wordt 1 tot 12 in de if statement)
            if i+1 not in listNR:                                #Hier kijkt hij telkens of de kluis vrij is
                kluizenAppend = open('kluizen.txt','a')

                pin = random.randint(1000,9999)
                kluizenAppend.write("{},{}\n".format(i+1,pin))   #Voegt het nieuwe kluisnummer + PIN-code toe aan kluizen.txt in het juiste formaat
                print("Kluisnummer: {}\nPIN-code: {}\n".format(i+1,pin))

                kluizenAppend.close()
                return i+1,pin
    else:
        print("Er zijn geen kluizen beschikbaar\n")
        return 0,0

def kluis_openen(listNR,listPIN):
    'Deze functie opent de kluis indien de juiste PIN-code is ingevoerd'
    pin = int(input("Voer uw 4-cijferige kluiscode in om de kluis te openen\n"))
    if pin in listPIN:
        print("Kluis",listNR[listPIN.index(pin)],"is geopend\n")
    else:
        print("Dat is niet een geldige PIN-code\n")

def kluis_teruggeven(listNR,listPIN,list):
    'Deze functie wordt gebruikt om een kluis weer vrij te geven door uit kluizen.txt te halen'
    pin = int(input("Voer uw 4-cijferige kluiscode in om de kluis terug te geven\n"))

    if pin in listPIN:                      #Checkt of de ingevoerde PIN-code in de lijst staat
        nummer = listPIN.index(pin)
        lineDelete = "{},{}\n".format(listNR[nummer],listPIN[nummer])      #Geeft aan welke regel verwijderd moet worden uit kluizen.txt
        kluizenReplace = open('kluizen.txt','w')                           #Maakt kluizen.txt leeg en staat klaar er opnieuw in te schrijven

        for line in list:                       #Gaat langs alle regels in de lijst
            if line!=lineDelete:                #Als de regel niet overeenkomt met lineDelete dan
                kluizenReplace.write(line)      #wordt hij opnieuw geschreven in kluizen.txt, lineDelete zal dus nooit opnieuw geschreven worden
        kluizenReplace.close()
        print("Uw kluis is succesvol teruggegeven\n")
        return pin
    else:
        print("Dat is niet een geldige PIN-code\n")

def kluizen_vrij(list):
    'Deze functie geeft weer of en hoeveel kluizen er nog vrij zijn.'
    if 12-len(list) == 1:
        print("Er is nog 1 kluis vrij\n")
    elif 12-len(list) == 0:
        print("Er zijn geen kluizen beschikbaar\n")
    else:
        print("Er zijn nog",12-len(list),"kluizen vrij\n")

while True:
    keuze = int(input("Maak uw keuze\n"
                      "1: Ik wil een nieuwe kluis\n"
                      "2: Ik wil mijn kluis openen\n"
                      "3: Ik geef mijn kluis terug\n"
                      "4: Ik wil weten hoeveel kluizen nog vrij zijn\n"
                      "5: Ik wil stoppen\n"))

    if keuze == 1:
        nieuwNR,nieuwPIN = nieuwe_kluis(listNR)
        if nieuwNR != 0:
            listNR.append(nieuwNR)
            listPIN.append(nieuwPIN)
            list = laad_kluizen()
    elif keuze == 2:
        kluis_openen(listNR,listPIN)
    elif keuze == 3:
        pin = kluis_teruggeven(listNR,listPIN,list)
        if pin != None:
            listNR.remove(listNR[listPIN.index(pin)])       #Haalt het verwijderde kluisnummer ook uit de lijst
            listPIN.remove(listPIN[listPIN.index(pin)])
    elif keuze == 4:
        kluizen_vrij(listNR)
    elif keuze == 5:
        print("Programma beëindigd")
        break
    else:
        print("Dat is geen juiste keuze!")
