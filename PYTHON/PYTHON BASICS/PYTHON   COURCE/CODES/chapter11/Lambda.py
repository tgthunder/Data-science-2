# lambda or anonymous functions:
# def add(a,b):
#     return a+b
# k=int(input("enter no.1:"))    
# l=int(input("enter no.2:"))
# print("Additon is ",add(k,l))



minus=lambda x,y:x-y
print(minus(9,5))
add=lambda a,b:a+b
print("addition is ",add(2,4))

l=[[1,2], [6,85], [3,76]]
l.sort(key= lambda x:x[1])
print(l)