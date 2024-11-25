# # Logical errors in python

# def increament(sal):
#     sal=sal+sal*15/100
#     return sal

# print(increament(2500))





a,b=[int(x) for x in input("Enter 2 numbers: ").split(',')]
c=15
try:

    c=a/b
except Exception as e:
    print(e)
print(c)

