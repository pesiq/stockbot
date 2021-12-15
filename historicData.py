import requests

from URI import REST_URI
from URI.stocksigns import DEBUG
from utils import parseResponseREST

uri = REST_URI.RESTURI

LIMIT = 100
START = 1502928000


def getKlines(symbol=DEBUG.upper(), timestamp=None, interval="1h", limit=LIMIT):
    try:
        params = dict(symbol=symbol,
                      limit=limit,
                      interval=interval)
        if timestamp is not None:
            params['startTime'] = timestamp
        r = requests.get(uri, params=params)
        if r.status_code == 200:
            return parseResponseREST(r)
        else:
            return symbol, 0

    except ConnectionError as e:
        print('Network problem')
        print(e)
    except TimeoutError as e:
        print('Request timed out')
        print(e)
    except KeyboardInterrupt as e:
        print('Interrupted by user')
        print('Finishing up...')
        print(e)
        exit(-1)
    except Exception as e:
        print('Unknown error')
        print(e)


if __name__ == '__main__':
    getKlines()
