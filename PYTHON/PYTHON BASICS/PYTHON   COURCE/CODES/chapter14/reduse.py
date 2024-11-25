from functools import reduce
import functools


l=[1,3,2,4,5]
num=0
for i in l:
    num=num+i
print(num)
# insted of this we can use reduce function
# n=reduce(lambda x,y:x+y,l)
# print(n)
l=reduce(lambda x,y:x+y,l)
print(l)

print(dir(functools))
