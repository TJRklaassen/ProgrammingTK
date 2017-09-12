kaartnummers = open('Kaartnummers.txt')
lines = 0
kaartHoogste = 0
regelHoogste = 0

for line in kaartnummers:
    lines += 1
    nummer = int(line.split(', ')[0])
    if nummer > kaartHoogste:
        kaartHoogste = nummer
        regelHoogste = lines

print('Deze file telt',lines,'regels')
print('Het grootste kaartnummer is',kaartHoogste,'en dat staat op regel',regelHoogste)

kaartnummers.close
