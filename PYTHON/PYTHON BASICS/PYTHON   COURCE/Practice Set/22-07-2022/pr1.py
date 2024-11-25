# def function():
#     a=1
#     a+=1
#     print(a)
# function()



# a=1
# def function():
#     b=2
#     a=45
#     print("a is ",a)
#     print("b is ",b)
# function()
# print(a)

# a=1
# def function():
    
#     global a 
#     print("Global a is ",a)
#     a=23
#     print("Modified a is ",a)
# function()
# print(a)

# a=1
# def function():
#     a=2
#     x=globals()['a']
#     print("Global a is ",x)
#     print("Local a is ",a)
# function()
# print(a)

# def calculate(lst):
#     """To find Total and sum"""
#     n=len(lst)
#     sum=0
#     for i in lst:
#         sum+=i
#         avg=sum/n
#         return sum,avg
# print("Enter the numbers seperated by ,")

# lst=[int(x) for x in input().split(",")]

# x,y=calculate(lst)

# print("The sum is ",x)
# print("The average is ",y)


# a=int(input("Enter the number:"))
# b=lambda x:x*x
# print("The square of given number is:",b(a))

# a,b=[int(x) for x in input().split(",")]
# c=lambda x,y:x+y
# print("The sum of two numbers is:",c(a,b))

# f=lambda x,y:x if x>y else y
# a,b=[int(x) for x in input("Enter two numbers: ").split(",")]

# print("Bigger number is:",f(a,b))

# if a>b:
#     print("a is grater ")
# else:
#     print("b is greater ")




# def is_even(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# lst=[10,20,30,40,50,55,31]

# lst1=list(filter(is_even,lst))
# print(lst1)

# lst=[1,2,3,4,5,6,7,8]

# # lst1=list(map(lambda x:x*x,lst)) 
# # print(lst1)   
# for i in lst:
#     print(f"The sqare of element {i} is:{i*i}")

from functools import reduce
lst=[1,34,65,78,99,54]
a=reduce(lambda x,y:x+y,lst)
print(a)