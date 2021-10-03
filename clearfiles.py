from statUtils import WORK_DIR
import csv

KLINE_HEADER = ['Sign', 'Time', 'Open time', 'Close time', 'Open', 'Close', 'Low', 'High']
GRAPH_HEADER = ['Sign', 'Time', 'Price', 'Number of trades', 'Base asset volume', 'Quote asset volume']

with open(f'{WORK_DIR}/output/graph.csv', 'w') as f1, open(f'{WORK_DIR}/output/kline.csv', 'w') as f2:
    gf = csv.writer(f1, dialect='excel')
    kf = csv.writer(f2, dialect='excel')
    gf.writerow(GRAPH_HEADER)
    kf.writerow(KLINE_HEADER)