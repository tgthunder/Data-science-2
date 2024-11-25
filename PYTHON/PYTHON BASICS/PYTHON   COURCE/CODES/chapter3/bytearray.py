#Bytearray Datatype
list=[12,23,54,60,48]
x=bytearray(list)
print(x)
x[0]=34
x[3]=29
for item in x:
    print(item)