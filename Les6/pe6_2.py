woordenlijst = input("Noem minimaal 10 woorden met spaties ertussen: ").split()
woordenlijst2 = []

for woord in woordenlijst:
    if len(woord) == 4:
        woordenlijst2.append(woord)

for woord in woordenlijst2:
    woordenlijst.remove(woord)

print('De nieuw-gemaakte lijst met alle vier-letter strings is:')
print(woordenlijst2)
