s=set()
print(s)
print(type(s))
l=[1,3,56,76,8,4]
set1=set(l)
print(set1)
# print(type(set1)/)
#operations on sets
set1.add(37)
# print(set1) we can add value once according to property of sets
print(set1)
print(max(set1))
print(min(set1))
print(set1.union({8,9,6}))
print(set1.intersection({3,56}))
set1.remove(4)
print(set1)