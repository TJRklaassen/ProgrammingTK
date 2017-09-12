def seizoen(maand):
    if maand == 12 or maand < 3:
        return 'winter'
    elif maand < 6:
        return 'lente'
    elif maand < 9:
        return 'zomer'
    else:
        return 'herfst'

seizoen = seizoen(int(input('Geef het cijfer van de maand: ')))
print('Het is',seizoen)
