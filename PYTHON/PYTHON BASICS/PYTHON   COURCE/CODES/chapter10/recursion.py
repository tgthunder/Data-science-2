# n!=n*(n-1)*(n-2)*(n-3)*...........1
# n!=n*(n-1)!
def fact_itrate(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac
    '''parameter n:integer
    return: n*(n-1)*(n-2)......1
    '''
number=int(input("Enter the number:"))
print("Factorial of given number is:",fact_itrate(number))
def fact_recursive(n):
    if n==1:
        return 1
    else:
        return n*(fact_recursive(n-1)) 
# 5*fact_recursive(4)
# 5*4*fact_recursive(3)     this operation will done inside function
# 5*4*3*fact_recursive(2)
# 5*4*3*2*1        
print("Factorial of given number using recuersive method:",fact_recursive(number))           