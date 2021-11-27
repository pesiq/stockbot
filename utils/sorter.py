import csv
import time

from utils import stat_utils as su

# constants
SUBFOLDER = '\sorted'
OP_DIR = su.WORK_DIR + '\output'
SORTED_DIR = OP_DIR + SUBFOLDER


# functions
def sortRaw(name):
    su.createFolder(SUBFOLDER)
    created = set()

    total_lines = 0
    start_time = time.time()
    with open(OP_DIR + f'\{name}.csv', 'r') as file:
        total_lines = sum(1 for line in file)
    elapsed_time = time.time() - start_time
    print(f'Time to count {time.strftime("%H:%M:%S", time.gmtime(elapsed_time))}')

    with open(OP_DIR + f'\{name}.csv', 'r') as raw:
        start_time = time.time()
        reader = csv.reader(raw)
        head = next(reader)
        del head[0]
        for i, line in enumerate(reader):
            sign = line[0]
            del line[0]
            su.createFolder(f'{SUBFOLDER}\{sign}')
            with open(SORTED_DIR + f'\{sign}\{name}.csv', 'a+', newline='') as output:
                writer = csv.writer(output)
                if sign not in created:
                    created.add(sign)
                    writer.writerow(head)
                writer.writerow(line)
            elapsed_time = time.time() - start_time
            ftime = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
            su.printProgressBar(i + 2, total_lines, f'Currently on line {i} out of {total_lines}', f'Complete. Elapsed '
                                                                                                   f'time: {ftime}',
                                length=25)
    return len(created)


# main
if __name__ == '__main__':
    print('Enter name of data source in output folder')
    returned = sortRaw(input())
    print(f'Created {returned} subfolders')
