import csv
import json
import time
import asyncio
import websockets

import statUtils as su
import URIs

uri = URIs.websocketURI


async def main():
    try:
        with open(f'{su.WORK_DIR}/output/kline.csv', "w", newline='') as kline, \
                open(f'{su.WORK_DIR}/output/graph.csv', "w", newline='') as graph:
            kf = csv.writer(kline, dialect='excel')
            gf = csv.writer(graph, dialect='excel')
            async with websockets.connect(uri) as client:
                print(f'Connecting to {uri}')
                while True:
                    data = json.loads(await client.recv())
                    parsed = su.responseParse(data)
                    if parsed:
                        gf.writerow([*parsed[0:2], *parsed[2]])
                        kf.writerow([*parsed[0:2], *parsed[3]])
                        print('Logged')
    except ConnectionAbortedError as e:
        print(f'Connection aborted with {uri}')
        print(e)
    except ConnectionRefusedError as e:
        print('Connection refused')
        print(f'Host uri: {uri}')
        print(e)
    except ConnectionError as e:
        print('Connection timed out')
        print(f'Host uri: {uri}')
        print(e)
    except StopAsyncIteration as e:
        print('Async function was terminated')
        print(e)
    except KeyboardInterrupt as e:
        print('Interrupted by user')
        print('Finishing up...')
        print(e)
    except Exception as e:
        print('Unknown error')
        print(e)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
