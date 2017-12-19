"""
GIL - Global Interpreter Lock

The mechanism used by the CPython interpreter to assure that only one thread executes Python bytecode at a time.
https://docs.python.org/3/glossary.html#term-global-interpreter-lock
"""
import time
from threading import Thread
import math
from multiprocessing.pool import Pool

import platform
print(platform.python_implementation())


def countdown(n):
    start_time = time.time()
    while n > 0:
        math.sin(n)
        n -= 1
    print("Time: " + str((time.time() - start_time)))


N = 10000000

print("\nnormal...")
countdown(N)

print("\nmultiprocessing...")
with Pool(2) as poll:
    results = poll.map(countdown, [N, N])

print("\nthreading...")
t1 = Thread(target=countdown, args=(N,))
t2 = Thread(target=countdown, args=(N,))
t1.start()
t2.start()
t1.join()
t2.join()
print("\ndone!")
