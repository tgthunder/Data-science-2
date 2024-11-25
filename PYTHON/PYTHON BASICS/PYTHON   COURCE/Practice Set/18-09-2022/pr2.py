def fac(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return fac(n-2)*fac(n-1)*fac(n)


m=int(input("Enter the number:"))

print(fac(m))