from concurrent.futures import ProcessPoolExecutor
from requests import Session
from requests_futures.sessions import FuturesSession


def callback(future):
    print(type(future))
    response = future.result()
    print(response.json()["args"])


session = FuturesSession(executor=ProcessPoolExecutor(max_workers=10),
                         session=Session())
for i in range(10):
    future_response = session.get('http://httpbin.org/get?foo=' + str(i))
    future_response.add_done_callback(callback)

print("done")
