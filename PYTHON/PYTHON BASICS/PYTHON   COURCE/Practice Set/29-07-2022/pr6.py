# """
# iterable - __iter__ or __getitem__
# iterator - __next__()
# iteration -

# """

# def gen(n):
#     for i in range(n):
#         yield i

# g= gen(10000)
# print(g)

def forloop(n):
    for i in range(n):
        print(i)

g=forloop(5)

print(g)


s="Sudarshan"
k=20

i=iter(s)
print(i)
# print(iter(k))
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())