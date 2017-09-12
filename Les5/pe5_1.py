def convert(tempCelsius):
    return tempCelsius * 1.8 + 32

def table():
    print('{0:8}{1:5}'.format('  F','  C'))
    for temp in range(-30,41,10):
        tempFahrenheit = convert(temp)
        print('{0:5.5}{1:8.5}'.format(tempFahrenheit,float(temp)))

table()
