getal = 1
getalSom = 0
getallen = -1

while getal != 0:
    getal = int(input("Geef een getal: "))
    getalSom += getal
    getallen += 1

print("Er zijn",getallen,"getallen ingevoerd, de som is:",getalSom)
