def gemiddelde(sentence):
    words = sentence.split()
    charsTotal = 0
    wordsTotal = 0

    for chars in words:
        charsTotal += len(chars)
        wordsTotal += 1

    print('Het gemiddelde aantal letters van alle woorden uit jouw zin is',charsTotal/wordsTotal)

gemiddelde(input('Typ een willekeurige zin: '))
