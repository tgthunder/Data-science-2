import time
from functools import lru_cache


@lru_cache(maxsize=32)
def some_work(n):
    time.sleep(n)
    return n
    
if __name__=='__main__':
    print(" now running Some work ")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(9)
    print("Done")
    some_work(3)
    print("called again")