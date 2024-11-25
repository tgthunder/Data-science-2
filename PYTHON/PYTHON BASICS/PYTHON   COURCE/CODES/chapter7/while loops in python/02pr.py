#Display odd numbers in m and n
m,n=[int(i) for i in input("enter minimum and maximum range: ").split(',')]
x=m
if (x%2)==0:
    
    print(x)
    x=x+1
while x>=m and x<=n:
    print(x)
    x+=2    
