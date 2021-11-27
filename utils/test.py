import sys

import funcanalysis as fa
from utils import buldgraph as bg

MAIN_DIR = '/'.join(sys.argv[0].split('/')[:-2])


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
