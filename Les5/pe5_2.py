kaartnummers = open('Kaartnummers.txt')

for line in kaartnummers:
    print(line.split(', ')[1].replace('\n',''),'heeft kaartnummer:',line.split(', ')[0])

kaartnummers.close()
