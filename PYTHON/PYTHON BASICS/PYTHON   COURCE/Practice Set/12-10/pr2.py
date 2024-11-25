x= [1,2,3,5]
y = [23,45,66,7]
print(x+y)

t1 = ('Sudarshan',11,34.67,None)
print(type(t1))
for i in t1:
    print(i)
print(t1.count('Sudarshan'))
print(t1.index(11))
fruitlist=[]
n =int(input("How many fruits you want:"))
i=1
for i in range(n):
    print(f"Enter your fruit {i}:")
    fruitlist.append(input())
    i+=1
print("Your fruitlist is:",fruitlist)

