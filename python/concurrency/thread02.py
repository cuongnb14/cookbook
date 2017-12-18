"""
The interpreter remains running until all threads terminate. For long-running threads
or background tasks that run forever, you should consider making the thread daemonic.

Daemonic threads can't be joined. However, they are destroyed automatically when the  main thread terminates.
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
t.daemon = True
t.start()
time.sleep(2)
print("done!")
