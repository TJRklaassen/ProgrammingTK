def wijzig(letterlijst):
    letterlijst.clear()
    letterlijst.append('d')
    letterlijst.append('e')
    letterlijst.append('f')

lijst = ['a','b','c']
print(lijst)
wijzig(lijst)
print(lijst)

#Waarom kun je in de functie niet de opdracht lijst = ['d', 'e', 'f'] geven?
#   Omdat de functie geen informatie buiten zichzelf kan krijgen, behalve de parameter(s) die hij opvraagt.
#Werkt jouw functie ook met een string-parameter? Probeer dit! Waarom werkt het wel/niet?
#   Met een string werkt het niet omdat een string immutable(onaanpasbaar) is.
#Welke rol speelt (im)mutabiliteit in deze vraag?
#   Als een object mutabel is dan kan je hem aanpassen via elke variabele die naar het object verwijst.
#   in dit geval verwijst letterlijst in de functie naar hetzelfde object als lijst.
