# fibonancci generator
def fibonancci(n):
    if n==0:
        yield 0

    elif n==1:
        yield 1

    else:
        yield fibonancci(n-1)+fibonancci(n-2)

a=fibonancci(10)
print(a)


