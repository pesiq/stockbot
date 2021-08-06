
import stocksigns as ss


def getStreamList():
    streamList = ""
    for symbol in ss.symbolList:
        streamList += f'{symbol}@{ss.streamTypeList[0]}{ss.klinePeriod[0]}/'
    streamList = streamList[:-1]
    return streamList


def getAll():
    return "!miniTicker@all"


websocketURI = f'wss://stream.binance.com:9443/stream?streams={getStreamList()}'
allStreamURI = 'wss://stream.binance.com:9443/ws/!ticker@arr'
allStreamMiniURI = 'wss://stream.binance.com:9443/ws/!miniTicker@arr'

botApi = ''

if __name__ == "__main__":
    s = getStreamList()
    print(s)
    s = getAll()
    print(s)
