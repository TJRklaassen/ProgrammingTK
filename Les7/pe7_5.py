def namen():
    counter = {}

    while True:
        naam = input("Vul de voornaam van een student in: ")
        if naam != "":
            if naam in counter:
                counter[naam] += 1
            else:
                counter[naam] = 1
        else:
            break

    return counter

counter = namen()

for naam in counter:
    if counter[naam] == 1:
        print("Er is 1 student met de naam",naam)
    else:
        print("Er zijn {} studenten met de naam {}".format(counter[naam],naam))
