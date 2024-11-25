# Display stars in rows
for i in range(1,11):
    for j in range(1,i+1):
        print("*",end="")
    print()       
# display equilateral triangle from n=40
n=40
for i in range(1,11):
    print(''*n, end='')
    print('*'*(i))
    n-=1