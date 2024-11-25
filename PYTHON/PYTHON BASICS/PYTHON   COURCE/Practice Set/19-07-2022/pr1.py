# l=['Sudarshan',12,12.65,True,None]
lst=list(range(10))
for i in lst:
    print(i)
lst[1]=45
for i in lst:
    print(i)
print(lst)
lst[1:2]=19,36
print(lst)
lst.sort()
print(lst)
