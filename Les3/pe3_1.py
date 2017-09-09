score = input('Geef je score: ')
if int(score) > 15:
    print('Gefeliciteerd!')
    print('Met een score van '+score+' ben je geslaagd!')

#Wat gebeurt er als je de tweede print()-opdracht niet recht onder de eerste zou plaatsen
#maar bijvoorbeeld recht onder de ‘i’ van het if-statement?
#   Als de 4e lijn onder de i van if (lijn 2) zou beginnen, dan zou je
#   'Met een score van '+score+' ben je geslaagd!' ook zien als je niet een score boven de 15 geeft.
