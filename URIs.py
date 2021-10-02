import stocksigns as ss


def getStreamList(par):
    streamList = ""
    if par:
        for symbol in ss.symbolList:
            streamList += f'{symbol}@{ss.streamTypeList[0]}{ss.klinePeriod[0]}/'
        streamList = streamList[:-1]
    else:
        for symbol in ss.importedSymbolList:
            streamList += f'{symbol}@{ss.streamTypeList[0]}{ss.klinePeriod[0]}/'
        streamList = streamList[:-1]
    return streamList


def getAll():
    return "!miniTicker@all"


websocketURI = f'wss://stream.binance.com:9443/stream?streams={getStreamList(False)}'
allStreamURI = 'wss://stream.binance.com:9443/ws/!ticker@arr'
allStreamMiniURI = 'wss://stream.binance.com:9443/ws/!miniTicker@arr'

botApi = ''

if __name__ == "__main__":
    s = getStreamList(False)
    print(s)
    s = getAll()
    print(s)
