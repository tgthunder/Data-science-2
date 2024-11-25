# # there are two types of functions
# # 1. built in function (there are so many built in function in python)



# a=12
# b=5
# c=sum((a,b))      #built in function sum
# print(c)


# # 2. user defined function
# def funct1():
#     print("you are in function 1")
# funct1() 
# #user defined  takes input 
# def funct2(a,b):
#     print("addition is ",a+b)
# funct2(4,5)    
# funct2(12,10)
# def funct3(a):
#     return a*a
# c=int(input("Enter a number:"))
# print("Suare of given number is ",funct3(c))




def sum(a,b):
    return a+b

b,c=[int(x) for x in input("Enter two inputs by seperating by comma").split(',')]

print(sum(b,c))