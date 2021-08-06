import json
import time
import asyncio
import websockets
import numpy as np
import pandas as pd


import constants


class Kline:
    def __init__(self, op, cp, high, low):
        self.open_price = op
        self.close_price = cp
        self.high = high
        self.low = low

    def update(self, cp, high, low):
        self.close_price = cp
        self.high = high
        self.low = low

    def reset(self, op, cp, high, low):
        self.open_price = op
        self.close_price = cp
        self.high = high
        self.low = low


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


async def main():
    async with websockets.connect(constants.websocketURI) as client:
        flag = False
        while True:
            data = json.loads(await client.recv())
            # print(data)
            body = data['data']['k']
            symbol = data['data']['s']
            timestamp = data['data']['E']
            kline_open = body['t']
            kline_close = body['T']
            kline_interval = body['i']
            first_trade_id = body['f']
            last_trade_id = body['L']
            open_price = float(body['o'])
            close_price = float(body['c'])
            high_price = float(body['h'])
            low_price = float(body['l'])
            base_asset_vol = body['v']
            trade_amount = body['n']
            isClosed: bool = body['x']
            quote_asset_vol = body['q']
            taker_base_ass_vol = body['V']
            taker_quote_ass_vol = body['Q']
            # time_axis_close.append(timestamp)
            if flag:
                temp = Kline(open_price, close_price, high_price, low_price)
                values_kline.append(temp)
                values_kline_close.append(temp.close_price)
                values_kline_open.append(temp.open_price)
                values_kline_high.append(temp.high)
                values_kline_low.append(temp.low)
                updateSMA()
                time_axis.append(kline_close)
                print(data)
                log_kline()
            # print(values_kline_close)
            # print(time_axis_close)
            flag = isClosed


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
