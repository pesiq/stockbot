# [1 if pair[1] > 0.58 else 0 for pair in TEMP]

import numpy as np
import tensorflow as tf

from historicData import getKlines
from utils import WORK_DIR
from utils import printProgressBar

from URI import stocksigns

if __name__ == '__main__':
    signs = [t.upper() for t in stocksigns.symbolList]
    size = len(signs)
    DATA = []
    errors = 0
    failed = []
    print('Connecting')
    for i, sign in enumerate(signs):
        printProgressBar(i, size)
        klines, _ = getKlines(sign)
        if isinstance(klines, str):
            errors += 1
            failed.append(klines)
        else:
            DATA.append(klines)
    print('Data collected, errors:')
    print(errors)
    print(failed)

    DATA = np.array(DATA)
    DATA = tf.keras.utils.normalize(DATA, axis=1).reshape(DATA.shape[0], -1)
    print('Data normalized')
    model = tf.keras.models.load_model(f'{WORK_DIR}/models/model4')
    print('Model loaded')
    TEMP = model.predict(DATA)
    print('Predictions made')
    result = [1 if pair[1] > 0.60 else 0 for pair in TEMP]
    print(result)
