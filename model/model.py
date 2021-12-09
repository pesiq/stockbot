import csv

import keras.layers
import tensorflow as tf
from utils import WORK_DIR
from historicData import getKlines
import numpy as np
import os

checkpoint_path = "checkpoints /cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)


DATA = None  # kline information
LABEL = None  # label


def train():
    model = tf.keras.models.Sequential()

    model.add(keras.layers.Flatten())

    model.add(keras.layers.Dense(256, activation=tf.nn.relu))
    model.add(keras.layers.Dense(256, activation=tf.nn.relu))

    model.add(tf.keras.layers.Dense(2, activation=tf.nn.softmax))

    model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

    model.fit(DATA, LABEL, epochs=4)

    model.save("models/model1")


if __name__ == '__main__':
    with open(f'{WORK_DIR}/output/stamps.csv', 'r') as true, open(f'{WORK_DIR}/output/false.csv') as false:
        treader = csv.reader(true)
        freader = csv.reader(false)
        for sign, time, interval in reader:
            time += '000'
            # print(sign, time, interval)
            print(getKlines(sign, time, interval))
    train()

