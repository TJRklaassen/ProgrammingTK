import random

def laad_kluizen():
    kluizenIn = open('kluizen.txt')
    list = kluizenIn.readlines()
    kluizenIn.close()
    return list

list = laad_kluizen()
quit = False
listNR = []
listPIN = []

for line in list:
    listNR.append(int(line.split(',')[0]))
    listPIN.append(int(line.split(',')[1]))

def nieuwe_kluis(listNR):
    if 12-len(listNR) > 0:
        for i in range(12):
            if i+1 not in listNR:
                kluizenAppend = open('kluizen.txt','a')

                pin = random.randint(1000,9999)
                kluizenAppend.write("{},{}\n".format(i+1,pin))
                print("Kluisnummer: {}\nPIN-code: {}\n".format(i+1,pin))

                kluizenAppend.close()
                return i+1,pin
    else:
        print("Er zijn geen kluizen beschikbaar\n")
        return 0,0

def kluis_openen(listNR,listPIN):
    pin = int(input("Voer uw 4-cijferige kluiscode in om de kluis te openen\n"))
    if pin in listPIN:
        print("Kluis",listNR[listPIN.index(pin)],"is geopend\n")
    else:
        print("Dat is niet een geldige PIN-code\n")

def kluis_teruggeven(listNR,listPIN,list):
    pin = int(input("Voer uw 4-cijferige kluiscode in om de kluis terug te geven\n"))

    if pin in listPIN:
        nummer = listPIN.index(pin)
        lineDelete = "{},{}\n".format(listNR[nummer],listPIN[nummer])
        kluizenReplace = open('kluizen.txt','w')

        for line in list:
            if line!=lineDelete:
                kluizenReplace.write(line)
        kluizenReplace.close()
        print("Uw kluis is succesvol teruggegeven\n")
        return pin
    else:
        print("Dat is niet een geldige PIN-code\n")

def kluizen_vrij(list):
    if 12-len(list) == 1:
        print("Er is nog 1 kluis vrij\n")
    elif 12-len(list) == 0:
        print("Er zijn geen kluizen beschikbaar\n")
    else:
        print("Er zijn nog",12-len(list),"kluizen vrij\n")

while not quit:
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
    elif keuze == 2:
        kluis_openen(listNR,listPIN)
    elif keuze == 3:
        list = laad_kluizen()
        pin = kluis_teruggeven(listNR,listPIN,list)
        if pin != None:
            listNR.remove(listNR[listPIN.index(pin)])
            listPIN.remove(listPIN[listPIN.index(pin)])
    elif keuze == 4:
        kluizen_vrij(listNR)
    elif keuze == 5:
        print("Programma beëindigd")
        quit = True
    else:
        print("Dat is geen juiste keuze!")
