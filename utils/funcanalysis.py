import numpy as np

from loc import graphdata as gd

np.set_printoptions(suppress=True)

maxDelta = 120
maxGrowthDelta = 80
klineAmount = 15


def calculateDelta(values):
    op = np.round(np.diff(values), decimals=3).astype(float)
    np.insert(op, 0, np.nan)
    # return [True if item > 0 else False for item in op]
    return op


def areIncreasingDeltas(a, b):
    return a > 0 and b > 0


def areIncreasingSegments(a, b):
    return (a[0] - a[-1] < 0) and (b[0] - b[-1] < 0)


def areIntersecting(a, b):
    for p1, p2 in zip(a, b):
        if p1 == p2:
            return True
    return False


def klineIsIncreasing(values):
    pass


def dist(l1, l2):
    result = []
    for pair in zip(l1, l2):
        a, b = pair
        result.append(abs(a - b))
    return result


def analyse(line1, line2, time):
    result = []
    delta1 = calculateDelta(line1)
    delta2 = calculateDelta(line2)
    distance = dist(line2, line1)
    for d1, d2, dis, time in zip(delta1, delta2, distance, time):
        if areIncreasingSegments(line1, line2) and not areIntersecting(line1, line2):
            if areIncreasingDeltas(d1, d2):
                if (dis > 0) and (dis < maxDelta) and (abs(d1 - d2) < maxGrowthDelta):
                    result.append(time)
    return result


if __name__ == '__main__':
    s = analyse(gd.values_SMA_7, gd.values_SMA_25, gd.time_axis)
    print(s)
