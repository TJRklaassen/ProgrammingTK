woordLengte = 0

while woordLengte != 4:
    woord = input("Geef een string van vier letters: ")
    woordLengte = len(woord)
    if woordLengte != 4:
        print("{} heeft {} letters".format(woord,len(woord)))

print("Inlezen van coorecte string: {} is geslaagd".format(woord))

#SIDENOTE: Er staat in de opdracht dat je een break-statement moet gebruiken, maar hier zie ik geen nut voor
