infile = open('tickersymbols.txt')
ticker = infile.readlines()
infile.close()
tickerDict = {}

def maak_ticker(tickerDict):
    for lines in ticker:
        tickerDict[lines.split(":")[0]] = lines.split(":")[1].replace("\n","")

    return tickerDict

def vind_key(tickerDict,invoer):
    for key in tickerDict:
        if invoer in tickerDict.values():
            return key

tickerDict = maak_ticker(tickerDict)

while True:
    invoerBedrijf = input("Enter Company name: ")
    if invoerBedrijf in tickerDict.keys():
        print("Ticker symbol:",tickerDict[invoerBedrijf])
        break
    else:
        print("There is no such Ticker symbol!")

while True:
    invoerTicker = input("Enter Ticker symbol: ")
    if invoerTicker in tickerDict.values():
        print("Company name:",vind_key(tickerDict,invoerTicker))
        break
    else:
        print("There is no such Company name!")
