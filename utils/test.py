from utils import buldgraph as bg
import funcanalysis as fa
from loc import graphdata as gd


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


if __name__ == '__main__':
    simulateBites(gd.time_axis, gd.values_SMA_7, gd.values_SMA_25)
