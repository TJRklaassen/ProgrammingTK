import datetime
hardlopers = open('hardlopers.txt', 'a')

name = ''

print('Typ bij het invullen van de naam "stop" om het programma te eindigen.\n')

while name != 'stop':
    name = input('Naam hardloper: ')
    if name != 'stop':
        time = datetime.datetime.today().strftime("%a %d %b %Y, %H:%M:%S, ")
        hardlopers.write(time+name+'\n')

print('\nAlle hardlopers zijn toegevoegd.')

hardlopers.close()
