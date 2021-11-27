import websockets

from URI import WS_URI

uri = WS_URI.websocketURI


async def main():
    try:
            async with websockets.connect(uri) as client:
                print(f'Connecting to {uri}')


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
    pass