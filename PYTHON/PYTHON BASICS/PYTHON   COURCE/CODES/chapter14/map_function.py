l1=["2","3","54","68"]
# for i in range(len(l1)):
#     l1[i]=int(l1[i])
# l1[2]=l1[2]+1
# print(l1[2]) #this is way we use to typecast all the no in list
#using map function
l1=list(map(int,l1))
print(l1)
# def sqr(a):
#     return a*a
l3=[2,3,5,4,8]
l2=list(map(lambda x:x*x,l3))
print(l2)
def sqr1(a):
    return a*a
def cube(a):
    return a*a*a 
functions=[sqr1,cube]
for i in range(5):
    val =list(map( lambda x:x(i),functions))
    print(val)