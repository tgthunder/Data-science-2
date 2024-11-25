'''

Itrable - __iter__() or __getitem__()
Itrator - __next__()
Iteration -

'''

for i in range(10):
    print(i)


def gen(n):
    for i in range(n):
        yield i

g=gen(10)
print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for loop automatically stop the itration

k="HArry"     # strings are iterable
ier = iter(k)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())


