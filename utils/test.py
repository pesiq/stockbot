import sys

from numpy import nan

import funcanalysis as fa
from utils import buldgraph as bg

MAIN_DIR = '/'.join(sys.argv[0].split('/')[:-2])

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
        values_SMA_7.append(nan)

    if len(values_kline) > 25:
        accumulator = 0.0
        for i in range(-1, -26, -1):
            accumulator += values_kline_close[i]
        accumulator /= 25
        values_SMA_25.append(accumulator)
    else:
        values_SMA_25.append(nan)

    if len(values_kline) > 99:
        accumulator = 0.0
        for i in range(-1, -100, -1):
            accumulator += values_kline_close[i]
        accumulator /= 99
        values_SMA_99.append(accumulator)
    else:
        values_SMA_99.append(nan)


def simulateBites(time_axis, sma7, sma25):
    temptime = []
    temp7 = []
    temp25 = []
    for index, tuple in enumerate(zip(time_axis, sma7, sma25)):
        time, s7, s25 = tuple
        temptime.append(time)
        temp7.append(s7)
        temp25.append(s25)
        if index % 5 == 0:
            res = fa.analyse(temp7, temp25, temptime)
            if res:
                print(res)
                bg.plot(temptime, temp7, temp25)
            temptime.clear()
            temp7.clear()
            temp25.clear()


piss = [2, 5, 435, 34, 52, 4, 23, 34, 5, 36, 4, 2, 42, 3, 55345, 634, 43, 523, ]

if __name__ == '__main__':
    print(MAIN_DIR)
