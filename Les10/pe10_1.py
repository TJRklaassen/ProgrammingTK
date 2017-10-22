import xmltodict

with open('producten.xml') as f:
    producten = xmltodict.parse(f.read())

for i in producten['artikelen']['artikel']:
    print(i['naam'])
