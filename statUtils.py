import json
import numpy as np
import csv


time_axis = []
values_kline = []
values_kline_close = []
values_kline_open = []
values_kline_high = []
values_kline_low = []
values_SMA_7 = []
values_SMA_25 = []
values_SMA_99 = []


def log_kline():
    print(f'{time_axis = }')
    print(f'{values_kline_open = }')
    print(f'{values_kline_close = }')
    print(f'{values_kline_high = }')
    print(f'{values_kline_low = }')
    print(f'{values_SMA_7 = }')
    print(f'{values_SMA_25 = }')
    print(f'{values_SMA_99 = }')


def updateSMA():
    if len(values_kline) > 7:
        accumulator = 0.0
        for i in range(-1, -8, -1):
            accumulator += values_kline_close[i]
        accumulator /= 7
        values_SMA_7.append(accumulator)
    else:
        values_SMA_7.append(np.nan)

    if len(values_kline) > 25:
        accumulator = 0.0
        for i in range(-1, -26, -1):
            accumulator += values_kline_close[i]
        accumulator /= 25
        values_SMA_25.append(accumulator)
    else:
        values_SMA_25.append(np.nan)

    if len(values_kline) > 99:
        accumulator = 0.0
        for i in range(-1, -100, -1):
            accumulator += values_kline_close[i]
        accumulator /= 99
        values_SMA_99.append(accumulator)
    else:
        values_SMA_99.append(np.nan)


# TODO update local global vars, generate a point to add to csv
def generatePoint(obj):
    pass


# TODO parse response into an object of arrays for further processing:
# ['symbol', 'timestamp', 'point: bool', graphvars: [closing_price, volume, ], klinevars: [open, close, high, low]]
def responseParse(data, flag):
    body = data['data']['k']           # shortcut to body of json
    symbol = data['data']['s']         # stock name
    timestamp = data['data']['E']      # timestamp of the cline response
    kline_open = body['t']             # at what time the cline was opened
    kline_close = body['T']            # at what time kline has closed
    kline_interval = body['i']         # kline interval (fixed because of the query)
    first_trade_id = body['f']         # trade id (irrelevant -> might delete)
    last_trade_id = body['L']          # trade id (irrelevant -> might delete)
    open_price = float(body['o'])      # price of base asset against quote asset at the time of cline opening (const)
    close_price = float(body['c'])     # price of base asset against quote asset at the time of cline closing (var)
    high_price = float(body['h'])      # highest price during opened cline (var)
    low_price = float(body['l'])       # lowest price during open cline (var)
    base_asset_vol = body['v']         # volume of trade on base asset (var)
    trade_amount = body['n']           # number of trades during opened cline
    isClosed: bool = body['x']         # turns to true when cline closes
    quote_asset_vol = body['q']        # volume of quote asset (quote is paid bu the buyer) (var)
    taker_base_ass_vol = body['V']     # maker taker order book fuckery
    taker_quote_ass_vol = body['Q']    # maker taker order book fuckery

    graph_values = [close_price, trade_amount, base_asset_vol, quote_asset_vol]
    kline_values = [kline_open, kline_close, open_price, close_price, low_price, high_price]
    result = [symbol, timestamp, isClosed, graph_values, kline_values]