from functools import reduce
a = int(input("Enter the value of a: "))
d = int(input("Enter the value of d: "))
n = int(input("Enter the value of n: "))

x=[]
 
for i in range(1,n+1):
    terms = a + (i-1)*d
    x.append(terms)

print(f"The arithmatic prograssion is {x}")

m=list(map(lambda k:k*k,x))
print(f"The square of arithmatic progression is {m}")

n=reduce(lambda x,y:x+y,m)

print("The sum of squares of terms in the seris is ",n)


