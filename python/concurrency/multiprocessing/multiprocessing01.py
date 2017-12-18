from multiprocessing.pool import Pool
import time


def countdown(profile):
    n = profile["top"]
    name = profile["name"]
    while n > 0:
        print('{} T-minus: {}'.format(name, n))
        n -= 1
        time.sleep(1)
    return 1


profiles = [
    {"name": "A", "top": 10},
    {"name": "B", "top": 30},
]

with Pool(2) as poll:
    results = poll.map(countdown, profiles)
    print(results)

