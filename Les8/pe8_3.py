def code(invoerstring):
    uitvoer = ""

    for i in invoerstring:
        uitvoer += chr(ord(i)+3)

    return uitvoer

gebruiker = input("Naam: ")
beginstation = input("Beginstation: ")
eindstation = input("Eindstation: ")

print(code(gebruiker+beginstation+eindstation))
