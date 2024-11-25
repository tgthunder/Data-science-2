from sys import maxsize
import time
from functools import lru_cache
# using this we can save time lru_cache is decorator

@lru_cache(maxsize=10)
def some_task(n):
    # some task taking n seconds
    time.sleep(n)
    return n

if __name__ =='__main__':
    print("Now running some work")
    some_task(3)
    print("Done...... calling again")
    some_task(3)
    print("calling again")
