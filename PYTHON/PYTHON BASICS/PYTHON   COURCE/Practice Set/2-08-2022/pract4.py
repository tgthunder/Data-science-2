#4. Write a Python function to calculate the nth term of the Fibonacci sequence.


def fibonancci(n):
    a = 0
    b = 1
    print(a,b,end=" ")
    for i in range(n):
        nextnum = a+b
        a = b
        b = nextnum
        print(nextnum,end=" ")

fibonancci(5)