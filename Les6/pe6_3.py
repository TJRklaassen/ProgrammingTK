list = "5-9-7-1-7-8-3-2-4-8-7-9".split('-')
list.sort()

for i in range(len(list)):
    list[i] = int(list[i])

print("Gesorteerde list van ints:",list)
print("Grootste getal:",list[-1],"en kleinste getal:",list[0])
print("Aantal getallen:",len(list),"en som van de getllen:",sum(list))
print("Gemiddelde:",sum(list)/len(list))
