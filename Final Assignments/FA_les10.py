import xmltodict

with open('stations.xml') as f:             #Opent het XML bestand
    stations = xmltodict.parse(f.read())    #Maakt station een dictonairy met de gegevens uit het XML bestand

print("Dit zijn de codes en types van de 4 stations:")
for i in stations['Stations']['Station']:           #Itereert langs elk station
    print("{:4} - {}".format(i['Code'],i['Type']))  #De :4 in de eerste {} is ervoor zodat alles er geordender uitziet en onder elkaar staat

print("\nDit zijn alle stations met één of meer synoniemen:")
for i in stations['Stations']['Station']:
    if i['Synoniemen'] != None:             #Zorgt ervoor dat de synoniemen alleen geprint worden als die bestaan.
        print("{:4} - {}".format(i['Code'],i['Synoniemen']['Synoniem']))

print("\nDit is de lange naam van elk station:")
for i in stations['Stations']['Station']:
    print("{:4} - {}".format(i['Code'],i['Namen']['Lang']))
