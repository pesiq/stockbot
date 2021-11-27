import json
import os

path = os.path.dirname(os.path.abspath(__file__))


def getallsymbols():
    result = set()
    with open(f'{path}/loc/exchangeInfo.json', 'r') as file:
        data = json.load(file)
        # print(data['symbols'][0])
        for symbol in data['symbols']:
            result.add(symbol['baseAsset'])

    # print(result)
    return list(result)


if __name__ == '__main__':
    print(path)
    List = getallsymbols()
    print(List)
    print(len(List))
