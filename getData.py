from historicData import getKlines
from utils import WORK_DIR
from time import sleep
import csv
"""
1595548800000
1633217880002
1637802000
"""
if __name__ == '__main__':
    with open(f'{WORK_DIR}/output/stamps.csv', 'r') as stamps:
        reader = csv.reader(stamps)
        for sign, time, interval in reader:
            time += '000'
            # print(sign, time, interval)
            print(getKlines(sign, time, interval))
            sleep(1)
