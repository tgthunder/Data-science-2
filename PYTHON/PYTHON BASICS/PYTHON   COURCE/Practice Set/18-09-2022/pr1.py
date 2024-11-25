import math
a=math.factorial(5)
print(a)

def combination(n,r):
    n=int(input("Enter no:"))
    r=int(input("Enter no:"))
    print(f"Your given n={n}")
    return (math.factorial(n))/(math.factorial(n-r))

# print(combination(5,4))
combination()

    
