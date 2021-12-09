import os
import sys
import json

WORK_DIR = '/'.join(sys.argv[0].split('/')[:-1])


# Print iterations progress
def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=20, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


# create folder in current working dir
def createFolder(name):
    """Creates a folder for a symbol if was not yet created"""
    path = f'{WORK_DIR}\output\{name}'
    create = not os.path.exists(path)
    if create:
        os.mkdir(path)
    return create


#
def parseResponseWS(raw):
    """
    Compiles response into an object and calls for further action
    ['symbol', 'timestamp', 'point: bool',
    graphvars: [closing_price, volume, ],
    klinevars: [open, close, high, low]]
    """
    data = json.loads(raw)
    body = data['data']['k']  # shortcut to body of json
    isClosed: bool = body['x']  # turns to true when cline closes
    if isClosed:
        symbol = data['data']['s']  # stock name
        timestamp = data['data']['E']  # timestamp of the cline response
        kline_open = body['t']  # at what time the cline was opened
        kline_close = body['T']  # at what time kline has closed
        # kline_interval = body['i']       # kline interval (fixed because of the query) (irrelevant)
        # first_trade_id = body['f']       # trade id (irrelevant -> might delete)
        # last_trade_id = body['L']        # trade id (irrelevant -> might delete)
        open_price = float(body['o'])  # price of base asset against quote asset at the time of cline opening (const)
        close_price = float(body['c'])  # price of base asset against quote asset at the time of cline closing (var)
        high_price = float(body['h'])  # highest price during opened cline (var)
        low_price = float(body['l'])  # lowest price during open cline (var)
        base_asset_vol = body['v']  # volume of trade on base asset (var)
        trade_amount = body['n']  # number of trades during opened cline
        quote_asset_vol = body['q']  # volume of quote asset (quote is paid bu the buyer) (var)
        # taker_base_ass_vol = body['V']   # maker taker order book BS
        # taker_quote_ass_vol = body['Q']  # maker taker order book BS

        graph_values = [close_price, trade_amount, base_asset_vol, quote_asset_vol]
        kline_values = [kline_open, kline_close, open_price, close_price, low_price, high_price]
        result = [symbol, timestamp, graph_values, kline_values]
    else:
        result = []
    return result


def parseResponseREST(data):
    """
    Parses REST API json response into a list
    does not return SYMBOL name, should acknowledged in context
    :param data: raw json data
    :return: list [open time, open, high, low, close, volume, close time]
    """
    klines = json.loads(data.text)
    res = []
    time = 0
    for kline in klines:
        res.append(list(map(float, kline[1:6])))
        time = int(kline[6])
    return res, time
