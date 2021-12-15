import csv
import random

import numpy as np
import tensorflow as tf

from historicData import getKlines
from utils import WORK_DIR
from utils import printProgressBar


TEMP = []
DATA = []  # kline information
LABEL = []  # label


MODEL_VER = 5


def test():
    model = tf.keras.models.load_model(f'{WORK_DIR}/models/model{MODEL_VER}')

    for index, datapoint in enumerate(DATA):
        print(np.argmax(model.predict(datapoint)))
        print(LABEL)

if __name__ == '__main__':
    with open(f'{WORK_DIR}/../output/stamps.csv', 'r') as true, open(f'{WORK_DIR}/../output/false.csv') as false:
        treader = csv.reader(true)
        freader = csv.reader(false)

        for point in freader:
            TEMP.append((point, 0))

        for point in treader:
            TEMP.append((point, 1))

    random.shuffle(TEMP)
    i = 0
    for point, label in TEMP:
        printProgressBar(i, 40)
        sign, time, interval = point
        time += '000'
        klines, _ = getKlines(sign, time, interval)
        DATA.append(klines)
        LABEL.append(label)
        i += 1
    DATA = np.array(DATA)
    DATA = tf.keras.utils.normalize(DATA, axis=1).reshape(DATA.shape[0], -1)

    test()
