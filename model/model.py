import csv
import random

import keras.layers
import numpy as np
import tensorflow as tf

from historicData import getKlines
from utils import WORK_DIR
from utils import printProgressBar


TEMP = []
DATA = []  # kline information
LABEL = []  # label


def train():
    model = tf.keras.models.Sequential()

    # model.add(keras.layers.Flatten())

    model.add(keras.layers.Dense(256, activation=tf.nn.relu, input_dim=1, input_shape=DATA.shape[1:]))
    model.add(keras.layers.Dense(256, activation=tf.nn.relu))

    model.add(tf.keras.layers.Dense(2, activation=tf.nn.softmax))

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(x=DATA, y=LABEL, epochs=5)

    model.save(f'{WORK_DIR}/models/model5')


def test():
    print(DATA)
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
        printProgressBar(i, 60)
        sign, time, interval = point
        time += '000'
        klines, _ = getKlines(sign, time, interval)
        DATA.append(klines)
        LABEL.append(label)
        i += 1
    LABEL = np.array(LABEL)
    DATA = np.array(DATA)
    test()
    DATA = tf.keras.utils.normalize(DATA, axis=1).reshape(DATA.shape[0], -1)
    train()
    test()
