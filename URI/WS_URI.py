import stocksigns as ss


def getStreamList(par):
    streamList = ""
    if par:
        for symbol in ss.SYMBOLS:
            streamList += f'{symbol}@{ss.TYPE[0]}{ss.PERIOD[0]}/'
        streamList = streamList[:-1]
    else:
        for symbol in ss.symbolList:
            streamList += f'{symbol}@{ss.TYPE[0]}{ss.PERIOD[0]}/'
        streamList = streamList[:-1]
    return streamList


def getAll():
    return "!miniTicker@all"


websocketURI = f'wss://stream.binance.com:9443/stream?streams={getStreamList(False)}'
allStreamURI = 'wss://stream.binance.com:9443/ws/!ticker@arr'
allStreamMiniURI = 'wss://stream.binance.com:9443/ws/!miniTicker@arr'

if __name__ == "__main__":
    s = getStreamList(False)
    print(s)
    s = getAll()
    print(s)
