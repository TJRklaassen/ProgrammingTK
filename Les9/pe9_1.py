bedrag = 4356

try:
    personen = int(input("Hoeveel personen gaan er op reis?"))

    if personen < 0:
        print("Negatieve getallen zijn niet toegestaan!")
    else:
        print("Het gemiddelde bedrag per persoon is:",bedrag/personen)

except ZeroDivisionError:
    print("Delen door nul kan niet!")
except ValueError:
    print("Gebruik alleen cijfers voor het invoeren van het aantal!")
except:
    print("Onjuiste invoer!")

