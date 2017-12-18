"""
Basic use threading
"""
import time
from threading import Thread


# Code to execute in an independent thread
def countdown(n):
    while n > 0:
        print('T-minus: ' + str(n))
        n -= 1
        time.sleep(1)


# Create and launch a thread
t = Thread(target=countdown, args=(10,))
t.start()
print("done!")
