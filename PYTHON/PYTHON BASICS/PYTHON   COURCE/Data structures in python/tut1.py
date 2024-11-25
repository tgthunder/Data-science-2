# Arrays
from array import *
arr1=array("i",[1,23,34,54])
arr1[2]=12
print(arr1)
for element in arr1:
    print(element)
print("This is for unicode character")
# creating an unicode array
arr2=array("u",['a','c','k','m'])
for char in arr2:
    print(char)

# creating one array from another array
a=array("f",[1.2,-34,45,76])
print(a)
b=array(a.typecode,(i*3 for i in a))
for elements in b:
    print(elements)

# accessing elements of array using index
print("accessing elements of array using index")

x=array("i",[12,43,75,1,9])

n=len(x)
for i in range(n):
    print(x[i],end=" ")

print()
# slicing an array
print("slicing an array")
y=array("i",[2,6,5,8,9,54,98,21,34])
for i in y[1:5]:
    print(i)

#Processing an array
m=array("i",[12,4,3,65,87])
m.append(32)
print(m)
m.fromlist([9,56,8])
print(m)
m.tolist()
print(m)
m.itemsize()
print(m)
