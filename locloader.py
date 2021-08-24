import json

def getallsymbols():
    result = set()
    with open('./loc/exchangeInfo.json', 'r') as file:
        data = json.load(file)
        # print(data['symbols'][0])
        for symbol in data['symbols']:
            result.add(symbol['baseAsset'])

    # print(result)
    return list(result)


if __name__ == '__main__':
    List = getallsymbols()
    print(len(List))