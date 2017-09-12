studentencijfers = [[95,92,86],[66,75,54],[89,72,100],[34,0,0]]

def gemiddelde_per_student(studentencijfers):
    gemiddelde = []

    for i in studentencijfers:
        gemiddelde.append(sum(i)/3)

    return gemiddelde

def gemiddelde_van_alle_studenten(studentencijfers):
    som = 0

    for i in studentencijfers:
        som += sum(i)

    return som

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))
